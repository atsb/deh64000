"""This module implements an extension to StructArray for state_ts.

This is really only defined in its own module to avoid a circular
import dependency.
"""

from __future__ import absolute_import

import re

from deh9000 import c
from deh9000 import states_parser
from deh9000 import strings
from deh9000.states import *

# Regexp for matching Pointer section headers:
POINTER_HEADER_RE = re.compile(r"\s*Pointer\s+(?P<index>\d+)"
                               r"(\s+\(.*\)\s*)?", re.I)

# Pointer sections only have one "field", matched by this:
POINTER_ASSIGN_RE = re.compile(r"\s*Codep Frame"
                               r"\s*="
                               r"\s*(?P<frame_num>\d+)")


class StatesArray(c.StructArray):
	"""Wrapper around StructArray that adds some extra methods."""

	# The parse() method below needs a set of states to use when assigning
	# new states automatically. If not explicitly provided, this function
	# will be called with to get a set of states. The default is a function
	# that returns an empty set and will fail, but this will be overridden
	# by DehackedFile to link into the garbage collector.
	def get_alloc_states(self):
		return set()

	# The parse() Method below needs to be able to set sprite names
	# automatically when parsing states. This function will be called to
	# map a set of sprite names into sprite numbers. The default here is
	# just a function that looks them up in the sprnames list.
	def assign_sprites(self, names):
		return [strings.sprnames.index(name) for name in names]

	# These states are hard-coded into the Doom source code - bits
	# of code jump to these states.
	HARDCODED_STATES = [
		# p_user.c, p_pspr.c, p_finale.c:P_XYMovement; also p_pspr.c
		S_PLAY,
		# p_mobj.c:P_SpawnPuff
		S_PUFF3,
		# p_mobj.c:P_SpawnBlood
		S_BLOOD2,
		S_BLOOD3,
		# p_user.c, p_pspr.c, p_finale.c:(various)
		S_PLAY_ATK1,
		S_PLAY_ATK2,
		S_PLAY_RUN1,
	]

	def walk(self, index):
		"""Iterate over states in sequence starting from given index.

		Each state in the states array has a "nextstate" field that
		indicates a state that follows it. This function returns a
		generator that yields the index of each state in the sequence,
		ending when the NULL state (0) is reached, a state is reached
		that never ends (tics < 0), or when a state is reached that
		has already been reached.
		"""
		previous_states = set()
		while index != S_NULL:
			yield index
			previous_states.add(index)
			if self[index].tics < 0:
				return
			index = self[index].nextstate
			if index in previous_states:
				return

	def parse(self, defstr, alloc_states=None):
		"""Parse list of states in DECORATE format, copying into array.

		The parameter alloc_states controls which states will be
		allocated to copy the parsed states into the array. If not
		specified, get_alloc_states() will be called to find which
		states are free for reuse. You may need to call
		DehackedFile.reclaim_states() first to free up some states.

		States which are used will be removed from alloc_states.

		Returned is a dictionary mapping from label name to index of
		state representing that label.
		"""
		if alloc_states is None:
			alloc_states = self.get_alloc_states()
		states, labels, sprnames = states_parser.parse(defstr)
		states_parser.remap_sprites(
			states, self.assign_sprites(sprnames))
		old_to_new = states_parser.remap_states(states, self,
		                                        alloc_states)
		return {label: old_to_new[state_id]
		        for label, state_id in labels.items()}


class CodePointers(object):
	"""Class that generates the Code Pointers blocks.

	Dehacked allows modification of the states table's 'action' field
	but it uses a weird mechanism to do so that uses separate blocks
	to the "Frame" blocks used for the rest of the fields.

	Every state which has an action pointer set (ie. in the original
	table) has a "pointer number" assigned to it, and only these states
	can be modified in dehacked patches.
	"""
	def __init__(self, states):
		self.lax_mode = False
		self.states = states
		self._state_to_pointer = {}
		self._action_to_state = {}
		for state_id, state in enumerate(states.original):
			if state.action is not None:
				ptr_id = len(self._state_to_pointer)
				self._state_to_pointer[state_id] = ptr_id
				self._action_to_state[state.action] = state_id
			elif None not in self._action_to_state:
				# We want _action_to_state to contain at least
				# one entry for 'None', so we can null out
				# action pointers if desired.
				self._action_to_state[None] = state_id

	def match_key(self):
		return (CodePointers,)

	def _format_diff(self, ptr_id, state_id):
		state = self.states[state_id]
		return "Pointer %d (Frame %d)\nCodep Frame = %d" % (
			ptr_id, state_id,
			self._action_to_state[state.action])

	def _sanity_check_pointers(self):
		if self.lax_mode:
			return
		for state_id, state in enumerate(self.states):
			assert (state.action is None
			     or state_id in self._state_to_pointer), (
				"State %d has an action pointer, but it isn't "
				"valid to set a pointer on this state in a "
				"Vanilla Dehacked patch. Either use a "
				"different state, or turn on lax mode with "
				"strings.lax_mode = True" % (
					state_id,
				)
			)

	def dehacked_diffs(self, other=None):
		other = other or self.states.original
		self._sanity_check_pointers()
		result = []
		for state_id, state in enumerate(self.states):
			other_state = other[state_id]
			# We need to look up the pointer ID for this state_id.
			# But Vanilla Dehacked (and certain source ports) only
			# allows action pointers to be changed in states that
			# originally had an action pointer. In this case
			# we just generate a fake pointer ID.
			if state.action != other_state.action:
				ptr_id = self._state_to_pointer.get(
					state_id, 100000 + state_id)
				result.append(
					self._format_diff(ptr_id, state_id))
		return result

	@classmethod
	def header_regexp(cls):
		return POINTER_HEADER_RE

	def parse_section(self, stream, index):
		index = int(index)
		for state_id, ptr_id in self._state_to_pointer.items():
			if ptr_id == index:
				to_state = self.states[state_id]
				break
		else:
			stream.exception("invalid pointer ID %d" % index)

		while True:
			line = stream.readline()
			if line.strip() == "":
				break
			m = POINTER_ASSIGN_RE.match(line)
			if not m:
				stream.exception("invalid syntax: %r" % line)
			from_id = int(m.groupdict()["frame_num"])
			to_state.action = self.states[from_id].action

# TODO: Add tests.


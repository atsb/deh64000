
from __future__ import absolute_import
from __future__ import print_function

import re
import unittest

from deh9000 import strings

# Regexp that matches the start of Text sections.
TEXT_HEADER_RE = re.compile(r"\s*Text"
                            r"\s+(?P<from_len>\d+)"
                            r"\s+(?P<to_len>\d+)"
                            r"\s*$", re.I)

class StringReplacements(object):
	"""Class that wraps the functionality of dehacked string replacements.

	Objects of this class behave very similar in API to a dict (all the
	common methods are implemented), except two types of functionality
	are provided.

	Firstly it's possible to do a simple string replacement by setting the
	old and new string. For example:

	  s["Picked up a red skull key."] = "Picked up a pink skull key."

	This is equivalent to:

	  s[strings.GOTREDSKULL] = "Picked up a pink skull key."

	However, it's often tedious to have to specify the whole original
	string like this. So for convenience, it's also possible to do string
	replacements for "standard" strings (those found in strings.py /
	d_englsh.h in the Doom source) just by setting a property:

	  s.GOTREDSKULL = "Picked up a pink skull key."
	"""
	def __init__(self, module=None, base_module=strings):
		self._extras = {}
		self._properties = set()
		self._string_lists = set()
		# Build a reverse mapping from original string back
		# to property name.
		self._reverse_map = {}
		for propname in dir(base_module):
			if propname.startswith("__"):
				continue
			value = getattr(base_module, propname)
			if isinstance(value, str):
				self._reverse_map[value] = propname
				self._properties.add(propname)
			elif isinstance(value, (tuple, list)):
				setattr(self, propname,
				        StringList(self, value))
				self._string_lists.add(propname)
		# Load strings from base_module (strings.py) and then
		# (optionally) overwrite with strings from a modified version
		# if one has been provided.
		self.load_from_module(base_module)
		if module is not None:
			self.load_from_module(module)

	def load_from_module(self, module):
		"""Load strings from the given module.

		It is assumed that the given module is a modified version of
		the strings.py module.
		"""
		# We only overwrite properties that were originally defined
		# in base_module at instantiation time; others are
		# ignored.
		for propname in set(dir(module)) & self._properties:
			value = getattr(module, propname)
			if isinstance(value, str):
				setattr(self, propname, value)

		# Update strings lists from module too:
		for propname in self._string_lists:
			if hasattr(module, propname):
				getattr(self, propname).copy_from(
					getattr(module, propname))

	def __contains__(self, s):
		return s in self._reverse_map or s in self._extras

	def __getitem__(self, s):
		# Options here are:
		# * The string may be a property (ie. standard string of
		#   the type in d_englsh.h). Use the reverse mapping to
		#   find if this is the case, and if so get its value.
		# * May be a non-standard string, like an error message,
		#   that the user set a replacement on. Look up in the
		#   extras map.
		# * If the string hasn't been replaced by the user at all,
		#   just return the same string.
		if s in self._reverse_map:
			propname = self._reverse_map[s]
			return getattr(self, propname)
		else:
			return self._extras.get(s, s)

	def get(self, s):
		return self[s]

	def __setitem__(self, s, replacement):
		# If this is a standard string stored as a property then
		# use the reverse map to look up the property name and
		# overwrite it. Otherwise store in extras map.
		if s in self._reverse_map:
			propname = self._reverse_map[s]
			setattr(self, propname, replacement)
		else:
			self._extras[s] = replacement

	def __len__(self):
		return len(self._reverse_map) + len(self._extras)

	def __iter__(self):
		for s in self._reverse_map:
			yield s
		for s in self._extras:
			yield s

	def iteritems(self):
		for key in self:
			yield key, self[key]
	def iterkeys(self):
		return iter(self)
	def itervalues(self):
		for key in self:
			yield self[key]

	def items(self):
		return list(self.iteritems())
	def keys(self):
		return list(self.iterkeys())
	def values(self):
		return list(self.itervalues())

	def match_key(self):
		return (StringReplacements,)

	def dehacked_diffs(self, other=None):
		other = other or {}
		result = []
		for old, new in sorted(self.iteritems()):
			# Both have the exact same replacement? No need
			# to repeat it.
			if other.get(old, old) == new:
				continue
			header = "Text %d %d\n" % (len(old), len(new))
			result.append(header + old + new)

		return result

	def header_regexp(cls):
	        return TEXT_HEADER_RE

	def parse_section(self, stream, from_len, to_len):
		from_len, to_len = int(from_len), int(to_len)
		from_text = stream.read(from_len)
		to_text = stream.read(to_len)
		self[from_text] = to_text


class StringList(object):
	"""Class for representing a string list based on StringReplacements.

	This is used for the sprite names list (sprnames) and possibly other
	lists of strings. An interface similar to the Python list interface is
	implemented, but nothing is actually stored; instead it is just a
	facade that stores any changes to its contents as modifications stored
	in a StringReplacements object.
	"""
	def __init__(self, string_repls, original):
		self.string_repls = string_repls
		self.original = original

	def __contains__(self, value):
		return value in list(self)

	def __getitem__(self, index):
		s = self.original[index]
		return self.string_repls[s]

	def __setitem__(self, index, newvalue):
		s = self.original[index]
		self.string_repls[s] = newvalue

	def __len__(self):
		return len(self.original)

	def __iter__(self):
		for i in range(len(self)):
			yield self[i]

	def __repr__(self):
		return repr(list(self))

	def copy_from(self, strlist):
		if len(self) != len(strlist):
			raise ValueError(
				"list lengths do not match: %d != %d" % (
					len(self), len(strlist)))
		for i, v in enumerate(strlist):
			self[i] = v

	def index(self, value):
		for i, v in enumerate(self):
			if v == value:
				return i
		else:
			raise ValueError("%r not found in list" % (
				value))

if __name__ == '__main__':
	unittest.main()


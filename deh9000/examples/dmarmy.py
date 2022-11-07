from deh9000 import *

humanoids = (MT_POSSESSED1, MT_POSSESSED2, MT_IMP1, MT_IMP2)
frame_fields = ("spawnstate", "seestate", "painstate", "meleestate",
                "missilestate", "deathstate", "xdeathstate")

def update_monster(mobjtype):
	"""Update the given mobjtype to look like a player."""
	mobj = mobjinfo[mobjtype]

	# Sound like a player.
	mobj.seesound = sfx_None
	mobj.painsound = sfx_plrpain
	mobj.deathsound = sfx_plrdie
	mobj.activesound = sfx_None

dehfile.save("dmarmy.deh")

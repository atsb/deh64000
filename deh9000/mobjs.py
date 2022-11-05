"""Constants and types representing Doom's mobjinfo array.

The mobjinfo array lists the types of thing which exist in Doom (monsters,
decorations, powerups, etc.). In the Doom source code the equivalent
definitions are found in info.h.
"""

from __future__ import absolute_import

from deh9000 import c


class mobjinfo_t(c.Struct):
    """Struct type containing properties for a given thing type.

	Doom has an table of objects of this type named mobjinfo[]. In Dehacked
	these are "Thing" sections. Each represents a type of object that can
	exist in-game, including players, monsters, projectiles, ammo/power-ups
	and decorations.
	"""
    DEHACKED_NAME = "Thing"

    doomednum = c.StructField("ID #")
    spawnstate = c.StructField("Initial frame")
    spawnhealth = c.StructField("Hit points")
    seestate = c.StructField("First moving frame")
    seesound = c.StructField("Alert sound")
    reactiontime = c.StructField("Reaction time")
    attacksound = c.StructField("Attack sound")
    painstate = c.StructField("Injury frame")
    painchance = c.StructField("Pain chance")
    painsound = c.StructField("Pain sound")
    meleestate = c.StructField("Close attack frame")
    missilestate = c.StructField("Far attack frame")
    deathstate = c.StructField("Death frame")
    xdeathstate = c.StructField("Exploding frame")
    deathsound = c.StructField("Death sound")
    speed = c.StructField("Speed")
    radius = c.StructField("Width")
    height = c.StructField("Height")
    mass = c.StructField("Mass")
    damage = c.StructField("Missile damage")
    activesound = c.StructField("Action sound")
    flags = c.StructField("Bits")

    # Which fields are references to entries in the states table?
    state_fields = ("spawnstate", "seestate", "painstate", "meleestate",
                    "missilestate", "deathstate", "xdeathstate")
    # Which fields are references to entries in the S_sfx table?
    sound_fields = ("seesound", "attacksound", "painsound", "deathsound",
                    "activesound")

    def clear_states(self):
        """Clear all the fields in the state_fields array.

		This is useful before calling states.parse() as it will
		free back all states being used by a mobj before redefining
		its states.
		"""
        for f in mobjinfo_t.state_fields:
            setattr(self, f, 0)

    def clear_sounds(self):
        """Clear all the fields in the sound_fields array."""
        for f in mobjinfo_t.sound_fields:
            setattr(self, f, 0)


FRACUNIT = 1 << 16

MF_SPECIAL = 1
MF_SOLID = 2
MF_SHOOTABLE = 4
MF_NOSECTOR = 8
MF_NOBLOCKMAP = 16
MF_AMBUSH = 32
MF_JUSTHIT = 64
MF_JUSTATTACKED = 128
MF_SPAWNCEILING = 256
MF_GRAVITY = 512
MF_DROPOFF = 0x400
MF_PICKUP = 0x800
MF_NOCLIP = 0x1000
MF_NIGHTMARE = 0x2000
MF_FLOAT = 0x4000
MF_TELEPORT = 0x8000
MF_MISSILE = 0x10000
MF_DROPPED = 0x20000
MF_TRIGTOUCH = 0x40000
MF_NOBLOOD = 0x80000
MF_CORPSE = 0x100000
MF_INFLOAT = 0x200000
MF_COUNTKILL = 0x400000
MF_COUNTITEM = 0x800000
MF_SKULLFLY = 0x1000000
MF_NOTDMATCH = 0x2000000
MF_SEETARGET = 0x4000000
MF_COUNTSECRET = 0x8000000
MF_RENDERLASER = 0x10000000
MF_TRIGDEATH = 0x20000000
MF_SHADOW = 0x40000000
MF_NOINFIGHTING = 0x80000000

mobjtype_t = c.Enum([
    "MT_PLAYER",
    "MT_PLAYERBOT1",
    "MT_PLAYERBOT2",
    "MT_PLAYERBOT3",
    "MT_DEMON1",
    "MT_DEMON2",
    "MT_MANCUBUS",
    "MT_POSSESSED1",
    "MT_POSSESSED2",
    "MT_IMP1",
    "MT_IMP2",
    "MT_CACODEMON",
    "MT_BRUISER1",
    "MT_BRUISER2",
    "MT_SKULL",
    "MT_BABY",
    "MT_CYBORG",
    "MT_CYBORG_TITLE",
    "MT_PAIN",
    "MT_RESURRECTOR",
    "MT_CAMERA",
    "MT_DEST_TELEPORT",
    "MT_DEST_PROJECTILE",
    "MT_FAKEITEM",
    "MT_LASERMARKER",
    "MT_PROJ_ROCKET",
    "MT_PROJ_PLASMA",
    "MT_PROJ_BFG",
    "MT_PROJ_LASER",
    "MT_PROJ_IMP1",
    "MT_PROJ_IMP2",
    "MT_PROJ_HEAD",
    "MT_PROJ_BRUISER1",
    "MT_PROJ_BRUISER2",
    "MT_PROJ_BABY",
    "MT_PROJ_FATSO",
    "MT_PROJ_TRACER",
    "MT_PROJ_DART",
    "MT_PROJ_RECTFIRE",
    "MT_PROJ_RECT",
    "MT_SMOKE_GRAY",
    "MT_SMOKE_RED",
    "MT_SMOKE_SMALL",
    "MT_BLOOD",
    "MT_GIB_CRUSHED",
    "MT_TELEPORTFOG",
    "MT_BFGSPREAD",
    "MT_ITEM_ARMOR1",
    "MT_ITEM_ARMOR2",
    "MT_ITEM_BONUSHEALTH",
    "MT_ITEM_BONUSARMOR",
    "MT_ITEM_BLUECARDKEY",
    "MT_ITEM_REDCARDKEY",
    "MT_ITEM_YELLOWCARDKEY",
    "MT_ITEM_YELLOWSKULLKEY",
    "MT_ITEM_REDSKULLKEY",
    "MT_ITEM_BLUESKULLKEY",
    "MT_ITEM_ARTIFACT1",
    "MT_ITEM_ARTIFACT2",
    "MT_ITEM_ARTIFACT3",
    "MT_ITEM_STIMPACK",
    "MT_ITEM_MEDKIT",
    "MT_ITEM_SOULSPHERE",
    "MT_ITEM_INVULSPHERE",
    "MT_ITEM_BERSERK",
    "MT_ITEM_INVISSPHERE",
    "MT_ITEM_RADSPHERE",
    "MT_ITEM_AUTOMAP",
    "MT_ITEM_PVIS",
    "MT_ITEM_MEGASPHERE",
    "MT_AMMO_CLIP",
    "MT_AMMO_CLIPBOX",
    "MT_AMMO_ROCKET",
    "MT_AMMO_ROCKETBOX",
    "MT_AMMO_CELL",
    "MT_AMMO_CELLPACK",
    "MT_AMMO_SHELL",
    "MT_AMMO_SHELLBOX",
    "MT_AMMO_BACKPACK",
    "MT_WEAP_BFG",
    "MT_WEAP_CHAINSAW",
    "MT_WEAP_CHAINGUN",
    "MT_WEAP_LAUNCHER",
    "MT_WEAP_PLASMA",
    "MT_WEAP_SHOTGUN",
    "MT_WEAP_SSHOTGUN",
    "MT_WEAP_LCARBINE",
    "MT_PROP_FIRE",
    "MT_PROP_CANDLE",
    "MT_PROP_BARREL",
    "MT_EXPLOSION1",
    "MT_EXPLOSION2",
    "MT_PROP_TECHLAMP1",
    "MT_PROP_TECHLAMP2",
    "MT_PROP_TORCHBLUE",
    "MT_PROP_TORCHYELLOW",
    "MT_PROP_TORCHRED",
    "MT_PROP_POLEBASELONG",
    "MT_PROP_POLEBASESHORT",
    "MT_PROP_FIREBLUE",
    "MT_PROP_FIRERED",
    "MT_PROP_FIREYELLOW",
    "MT_GIB_MEATSTICK",
    "MT_GIB_MEATHANG",
    "MT_GIB_TORSOHANG",
    "MT_GIB_RIBFLOOR",
    "MT_GIB_TWITCHFLOOR",
    "MT_GIB_BLOODPOOL",
    "MT_GIB_BONEFLOOR",
    "MT_GIB_MEATRIBFLOOR",
    "MT_GIB_MEATRIBCAGE",
    "MT_GIB_CHAINHOOK",
    "MT_GIB_HANGCAGE",
    "MT_GIB_CHAINPINSER",
    "MT_GIB_CHAINARM",
    "MT_GIB_HANGMACE1",
    "MT_GIB_HEADSTICK1",
    "MT_GIB_HEADSTICK2",
    "MT_GIB_DOUBLEMEATSTICK",
    "MT_PROP_STATUE1",
    "MT_PROP_STATUE2",
    "MT_PROP_TECHPOLELONG",
    "MT_PROP_TECHPOLESHORT",
    "MT_PROP_TREESTUMPSMALL",
    "MT_PROP_TREESTUMPLARGE",
    "MT_PROP_TREE",
    "MT_PROP_BLOODYPOLE",
    "MT_GIB_HANGMACE2",
    "MT_GIB_HANGWHITEMEAT",
    "MT_GIB_HANGHEAD",
    "MT_GIB_HANGRIB",
])

mobjtype_t.create_globals(globals())

# To match the Doom source, but if you're really a Python programmer you
# probably shouldn't be using this.
NUMMOBJTYPES = len(mobjtype_t)

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
"MT_PLAYER", # 0
"MT_PLAYERBOT1", # 1
"MT_PLAYERBOT2", # 2
"MT_PLAYERBOT3", # 3
"MT_DEMON1", # 4
"MT_DEMON2", # 5
"MT_MANCUBUS", # 6
"MT_POSSESSED1", # 7
"MT_POSSESSED2", # 8
"MT_IMP1", # 9
"MT_IMP2", # 10
"MT_CACODEMON", # 11
"MT_BRUISER1", # 12
"MT_BRUISER2", # 13
"MT_SKULL", # 14
"MT_BABY", # 15
"MT_CYBORG", # 16
"MT_CYBORG_TITLE", # 17
"MT_PAIN", # 18
"MT_RESURRECTOR", # 19
"MT_CAMERA", # 20
"MT_DEST_TELEPORT", # 21
"MT_DEST_PROJECTILE", # 22
"MT_FAKEITEM", # 23
"MT_LASERMARKER", # 24
"MT_PROJ_ROCKET", # 25
"MT_PROJ_PLASMA", # 26
"MT_PROJ_BFG", # 27
"MT_PROJ_LASER", # 28
"MT_PROJ_IMP1", # 29
"MT_PROJ_IMP2", # 30
"MT_PROJ_HEAD", # 31
"MT_PROJ_BRUISER1", # 32
"MT_PROJ_BRUISER2", # 33
"MT_PROJ_BABY", # 34
"MT_PROJ_FATSO", # 35
"MT_PROJ_TRACER", # 36
"MT_PROJ_DART", # 37
"MT_PROJ_RECTFIRE", # 38
"MT_PROJ_RECT", # 39
"MT_SMOKE_GRAY", # 40
"MT_SMOKE_RED", # 41
"MT_SMOKE_SMALL", # 42
"MT_BLOOD", # 43
"MT_GIB_CRUSHED", # 44
"MT_TELEPORTFOG", # 45
"MT_BFGSPREAD", # 46
"MT_ITEM_ARMOR1", # 47
"MT_ITEM_ARMOR2", # 48
"MT_ITEM_BONUSHEALTH", # 49
"MT_ITEM_BONUSARMOR", # 50
"MT_ITEM_BLUECARDKEY", # 51
"MT_ITEM_REDCARDKEY", # 52
"MT_ITEM_YELLOWCARDKEY", # 53
"MT_ITEM_YELLOWSKULLKEY", # 54
"MT_ITEM_REDSKULLKEY", # 55
"MT_ITEM_BLUESKULLKEY", # 56
"MT_ITEM_ARTIFACT1", # 57
"MT_ITEM_ARTIFACT2", # 58
"MT_ITEM_ARTIFACT3", # 59
"MT_ITEM_STIMPACK", # 60
"MT_ITEM_MEDKIT", # 61
"MT_ITEM_SOULSPHERE", # 62
"MT_ITEM_INVULSPHERE", # 63
"MT_ITEM_BERSERK", # 64
"MT_ITEM_INVISSPHERE", # 65
"MT_ITEM_RADSPHERE", # 66
"MT_ITEM_AUTOMAP", # 67
"MT_ITEM_PVIS", # 68
"MT_ITEM_MEGASPHERE", # 69
"MT_AMMO_CLIP", # 70
"MT_AMMO_CLIPBOX", # 71
"MT_AMMO_ROCKET", # 72
"MT_AMMO_ROCKETBOX", # 73
"MT_AMMO_CELL", # 74
"MT_AMMO_CELLPACK", # 75
"MT_AMMO_SHELL", # 76
"MT_AMMO_SHELLBOX", # 77
"MT_AMMO_BACKPACK", # 78
"MT_WEAP_BFG", # 79
"MT_WEAP_CHAINSAW", # 80
"MT_WEAP_CHAINGUN", # 81
"MT_WEAP_LAUNCHER", # 82
"MT_WEAP_PLASMA", # 83
"MT_WEAP_SHOTGUN", # 84
"MT_WEAP_SSHOTGUN", # 85
"MT_WEAP_LCARBINE", # 86
"MT_PROP_FIRE", # 87
"MT_PROP_CANDLE", # 88
"MT_PROP_BARREL", # 89
"MT_EXPLOSION1", # 90
"MT_EXPLOSION2", # 91
"MT_PROP_TECHLAMP1", # 92
"MT_PROP_TECHLAMP2", # 93
"MT_PROP_TORCHBLUE", # 94
"MT_PROP_TORCHYELLOW", # 95
"MT_PROP_TORCHRED", # 96
"MT_PROP_POLEBASELONG", # 97
"MT_PROP_POLEBASESHORT", # 98
"MT_PROP_FIREBLUE", # 99
"MT_PROP_FIRERED", # 100
"MT_PROP_FIREYELLOW", # 101
"MT_GIB_MEATSTICK", # 102
"MT_GIB_MEATHANG", # 103
"MT_GIB_TORSOHANG", # 104
"MT_GIB_RIBFLOOR", # 105
"MT_GIB_TWITCHFLOOR", # 106
"MT_GIB_BLOODPOOL", # 107
"MT_GIB_BONEFLOOR", # 108
"MT_GIB_MEATRIBFLOOR", # 109
"MT_GIB_MEATRIBCAGE", # 110
"MT_GIB_CHAINHOOK", # 111
"MT_GIB_HANGCAGE", # 112
"MT_GIB_CHAINPINSER", # 113
"MT_GIB_CHAINARM", # 114
"MT_GIB_HANGMACE1", # 115
"MT_GIB_HEADSTICK1", # 116
"MT_GIB_HEADSTICK2", # 117
"MT_GIB_DOUBLEMEATSTICK", # 118
"MT_PROP_STATUE1", # 119
"MT_PROP_STATUE2", # 120
"MT_PROP_TECHPOLELONG", # 121
"MT_PROP_TECHPOLESHORT", # 122
"MT_PROP_TREESTUMPSMALL", # 123
"MT_PROP_TREESTUMPLARGE", # 124
"MT_PROP_TREE", # 125
"MT_PROP_BLOODYPOLE", # 126
"MT_GIB_HANGMACE2", # 127
"MT_GIB_HANGWHITEMEAT", # 128
"MT_GIB_HANGHEAD", # 129
"MT_GIB_HANGRIB", # 130
"MT_MISC2",
"MT_MISC3",
"MT_MISC4",
"MT_MISC5",
"MT_MISC6",
"MT_MISC7",
"MT_MISC8",
"MT_MISC9",
"MT_MISC10",
"MT_MISC11",
"MT_MISC12",
"MT_MISC13",
"MT_MISC14",
"MT_MISC15",
"MT_MISC16",
"MT_MISC17",
"MT_MISC18",
"MT_MISC19",
"MT_MISC20",
"MT_MISC21",
"MT_MISC22",
"MT_MISC23",
"MT_MISC24",
"MT_MISC25",
"MT_MISC26",
"MT_MISC27",
"MT_MISC28",
"MT_MISC29",
"MT_MISC30",
"MT_MISC31",
"MT_MISC32",
"MT_MISC33",
"MT_MISC34",
"MT_MISC35",
"MT_MISC36",
"MT_MISC37",
"MT_MISC38",
"MT_MISC39",
"MT_MISC40",
"MT_MISC41",
"MT_CHAINGUY",
"MT_UNDEAD",
"MT_PROJ_UNDEAD",
"MT_SPIDER",
"MT_TESTA0",
])

mobjtype_t.create_globals(globals())

# To match the Doom source", but if you're really a Python programmer you
# probably shouldn't be using this.
NUMMOBJTYPES = len(mobjtype_t)

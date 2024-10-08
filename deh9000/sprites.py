"""Constants and types for Doom's sprite names table.

In the Doom source code the equivalent definitions are found in info.h.
"""

from __future__ import absolute_import

from deh9000 import c

spritenum_t = c.Enum([
	"SPR_SPOT",
	"SPR_PLAY",
	"SPR_SARG",
	"SPR_FATT",
	"SPR_POSS",
	"SPR_TROO",
	"SPR_HEAD",
	"SPR_BOSS",
	"SPR_SKUL",
	"SPR_BSPI",
	"SPR_CYBR",
	"SPR_PAIN",
	"SPR_RECT",
	"SPR_MISL",
	"SPR_PLSS",
	"SPR_BFS1",
	"SPR_LASS",
	"SPR_BAL1",
	"SPR_BAL3",
	"SPR_BAL2",
	"SPR_BAL7",
	"SPR_BAL8",
	"SPR_APLS",
	"SPR_MANF",
	"SPR_TRCR",
	"SPR_DART",
	"SPR_FIRE",
	"SPR_RBAL",
	"SPR_PUF2",
	"SPR_PUF3",
	"SPR_PUFF",
	"SPR_BLUD",
	"SPR_A027",
	"SPR_TFOG",
	"SPR_BFE2",
	"SPR_ARM1",
	"SPR_ARM2",
	"SPR_BON1",
	"SPR_BON2",
	"SPR_BKEY",
	"SPR_RKEY",
	"SPR_YKEY",
	"SPR_YSKU",
	"SPR_RSKU",
	"SPR_BSKU",
	"SPR_ART1",
	"SPR_ART2",
	"SPR_ART3",
	"SPR_STIM",
	"SPR_MEDI",
	"SPR_SOUL",
	"SPR_PINV",
	"SPR_PSTR",
	"SPR_PINS",
	"SPR_SUIT",
	"SPR_PMAP",
	"SPR_PVIS",
	"SPR_MEGA",
	"SPR_CLIP",
	"SPR_AMMO",
	"SPR_RCKT",
	"SPR_BROK",
	"SPR_CELL",
	"SPR_CELP",
	"SPR_SHEL",
	"SPR_SBOX",
	"SPR_BPAK",
	"SPR_BFUG",
	"SPR_CSAW",
	"SPR_MGUN",
	"SPR_LAUN",
	"SPR_PLSM",
	"SPR_SHOT",
	"SPR_SGN2",
	"SPR_LSRG",
	"SPR_CAND",
	"SPR_BAR1",
	"SPR_LMP1",
	"SPR_LMP2",
	"SPR_A031",
	"SPR_A030",
	"SPR_A032",
	"SPR_A033",
	"SPR_A034",
	"SPR_BFLM",
	"SPR_RFLM",
	"SPR_YFLM",
	"SPR_A006",
	"SPR_A021",
	"SPR_A003",
	"SPR_A020",
	"SPR_A014",
	"SPR_A016",
	"SPR_A008",
	"SPR_A007",
	"SPR_A015",
	"SPR_A001",
	"SPR_A012",
	"SPR_A010",
	"SPR_A018",
	"SPR_A017",
	"SPR_A026",
	"SPR_A022",
	"SPR_A028",
	"SPR_A029",
	"SPR_A035",
	"SPR_A036",
	"SPR_TRE3",
	"SPR_TRE2",
	"SPR_TRE1",
	"SPR_A013",
	"SPR_A019",
	"SPR_A004",
	"SPR_A005",
	"SPR_A023",
	"SPR_SAWG",
	"SPR_PUNG",
	"SPR_PISG",
	"SPR_SHT1",
	"SPR_SHT2",
	"SPR_CHGG",
	"SPR_ROCK",
	"SPR_PLAS",
	"SPR_BFGG",
	"SPR_LASR",
	"SPR_S015",
	"SPR_S016",
	"SPR_S003",
	"SPR_S039",
	"SPR_S025",
	"SPR_S033",
	"SPR_S034",
	"SPR_S035",
	"SPR_S005",
	"SPR_S006",
	"SPR_S007",
	"SPR_S008",
	"SPR_S009",
	"SPR_S010",
	"SPR_S011",
	"SPR_S012",
	"SPR_S013",
	"SPR_S014",
	"SPR_S017",
	"SPR_S018",
	"SPR_S019",
	"SPR_S020",
	"SPR_S021",
	"SPR_S022",
	"SPR_S023",
	"SPR_S024",
	"SPR_S028",
	"SPR_S029",
	"SPR_S031",
	"SPR_S032",
	"SPR_S027",
	"SPR_S036",
	"SPR_S037",
	"SPR_S038",
	"SPR_S040",
	"SPR_S041",
	"SPR_S026",
	"SPR_S002",
	"SPR_S030",
	"SPR_CPOS",
	"SPR_SKEL",
	"SPR_ARCR",
	"SPR_POW1",
	"SPR_SPID",
	"SPR_VFIR",
	"SPR_VILE",
	"SPR_TEST",
])

spritenum_t.create_globals(globals())

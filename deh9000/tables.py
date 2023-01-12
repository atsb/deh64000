"""Python representation of Doom's internal tables.
These are the tables that Dehacked allows the user to edit. These are
intentionally separated from the definitions for the types that they are based
upon. The idea is that one way of generating a dehacked patch is to make a
copy of this file, edit it and then use the built-in functions to compare the
modified version against the original "clean" copy.
"""

from __future__ import absolute_import

from deh9000.actions import *
from deh9000.ammo import *
from deh9000.misc import *
from deh9000.mobjs import *
from deh9000.sounds import *
from deh9000.sprites import *
from deh9000.states import *
from deh9000.states_array import CodePointers, StatesArray
from deh9000.weapons import *

"""Constants and types for Doom's sound effects table.
The S_sfx array lists the different sound effects which play within the game.
In the Doom source code the equivalent definitions are found in sounds.h.
"""

from deh9000 import c

ammodata = c.StructArray(ammodata_t, [
    (10, 200),  # am_clip
    (4, 50),  # am_shell
    (20, 300),  # am_cell
    (1, 50),  # am_misl
])

ammodata.set_object_names([
    "Bullets",
    "Shells",
    "Cells",
    "Rockets",
])

miscdata = deh_misc_t(
    initial_health=100,
    initial_bullets=50,
    max_health=200,
    max_armor=200,
    green_armor_class=1,
    blue_armor_class=2,
    max_soulsphere=200,
    soulsphere_health=100,
    megasphere_health=200,
    god_mode_health=100,
    idfa_armor=200,
    idfa_armor_class=2,
    idkfa_armor=200,
    idkfa_armor_class=2,
    bfg_cells_per_shot=40,
    species_infighting=202,
)

weaponinfo = c.StructArray(weaponinfo_t, [
    (
        # fist
        am_noammo,
        S_PUNCHUP,
        S_PUNCHDOWN,
        S_PUNCH,
        S_PUNCH1,
        S_NULL
    ),
    (
        # pistol
        am_clip,
        S_PISTOLUP,
        S_PISTOLDOWN,
        S_PISTOL,
        S_PISTOL1,
        S_PISTOLFLASH
    ),
    (
        # shotgun
        am_shell,
        S_SGUNUP,
        S_SGUNDOWN,
        S_SGUN,
        S_SGUN1,
        S_SGUNFLASH
    ),
    (
        # chaingun
        am_clip,
        S_CHAINGUP,
        S_CHAINGDOWN,
        S_CHAING,
        S_CHAING1,
        S_CHAINGLIGHT1
    ),
    (
        # missile launcher
        am_misl,
        S_ROCKETLUP,
        S_ROCKETLDOWN,
        S_ROCKETL,
        S_ROCKETL1,
        S_ROCKETLLIGHT1
    ),
    (
        # plasma rifle
        am_cell,
        S_PLASMAGUP1,
        S_PLASMAGDOWN,
        S_PLASMAG,
        S_PLASMAG1,
        S_NULL
    ),
    (
        # bfg 9000
        am_cell,
        S_BFGUP,
        S_BFGDOWN,
        S_BFG,
        S_BFG1,
        S_BFGLIGHT1
    ),
    (
        # chainsaw
        am_noammo,
        S_SAWUP,
        S_SAWDOWN,
        S_SAWA,
        S_SAW1,
        S_NULL
    ),
    (
        # super shotgun
        am_shell,
        S_SSGUP,
        S_SSGDOWN,
        S_SSG,
        S_SSG1,
        S_SSGFLASH
    ),
    (
        # unmaker
        am_shell,
        S_LASERGUP,
        S_LASERGDOWN,
        S_LASERG,
        S_LASERG1,
        S_LASERGLIGHT
    ),
])

weaponinfo.set_object_names([
    "Fists",
    "Pistol",
    "Shotgun",
    "Chaingun",
    "Rocket Launcher",
    "Plasma Gun",
    "BFG 9000",
    "Chainsaw",
    "Super Shotgun",
    "Unmaker",
])

states = StatesArray(state_t, [
    (SPR_SPOT, 0, -1, None, S_NULL),
    (SPR_PLAY, 0, -1, None, S_NULL),
    (SPR_PLAY, 0, 4, None, S_PLAY_RUN2),
    (SPR_PLAY, 1, 4, None, S_PLAY_RUN3),
    (SPR_PLAY, 2, 4, None, S_PLAY_RUN4),
    (SPR_PLAY, 3, 4, None, S_PLAY_RUN1),
    (SPR_PLAY, 4, 12, None, S_PLAY_ATK2),
    (SPR_PLAY, 32773, 6, None, S_PLAY),
    (SPR_PLAY, 6, 4, None, S_PLAY_PAIN2),
    (SPR_PLAY, 6, 4, A_Pain, S_PLAY),
    (SPR_PLAY, 7, 10, None, S_PLAY_DIE2),
    # S_PLAY_DIE2
    (SPR_PLAY, 8, 10, A_Scream, S_PLAY_DIE3),
    # S_PLAY_DIE3
    (SPR_PLAY, 9, 10, A_Fall, S_PLAY_DIE4),
    # S_PLAY_DIE4
    (SPR_PLAY, 10, 10, None, S_PLAY_DIE5),
    # S_PLAY_DIE5
    (SPR_PLAY, 11, 10, None, S_PLAY_DIE6),
    # S_PLAY_DIE6
    (SPR_PLAY, 12, -1, None, S_NULL),
    # S_PLAY_XDIE1
    (SPR_PLAY, 13, 5, None, S_PLAY_XDIE2),
    # S_PLAY_XDIE2
    (SPR_PLAY, 14, 5, A_XScream, S_PLAY_XDIE3),
    # S_PLAY_XDIE3
    (SPR_PLAY, 15, 5, A_Fall, S_PLAY_XDIE4),
    # S_PLAY_XDIE4
    (SPR_PLAY, 16, 5, None, S_PLAY_XDIE5),
    # S_PLAY_XDIE5
    (SPR_PLAY, 17, 5, None, S_PLAY_XDIE6),
    # S_PLAY_XDIE6
    (SPR_PLAY, 18, 5, None, S_PLAY_XDIE7),
    # S_PLAY_XDIE7
    (SPR_PLAY, 19, 5, None, S_PLAY_XDIE8),
    # S_PLAY_XDIE8
    (SPR_PLAY, 20, 5, None, S_PLAY_XDIE9),
    # S_PLAY_XDIE9
    (SPR_PLAY, 21, -1, None, S_NULL),

    # S_PBOT_STND
    (SPR_PLAY, 4, 10, A_Look, S_PBOT_STND),
    # S_PBOT_RUN1
    (SPR_PLAY, 0, 4, A_Chase, S_PBOT_RUN2),
    # S_PBOT_RUN2
    (SPR_PLAY, 1, 4, A_Chase, S_PBOT_RUN3),
    # S_PBOT_RUN3
    (SPR_PLAY, 2, 4, A_Chase, S_PBOT_RUN4),
    # S_PBOT_RUN4
    (SPR_PLAY, 3, 4, A_Chase, S_PBOT_RUN1),
    # S_PBOT_ATK1
    (SPR_PLAY, 4, 4, A_PosAttack, S_PBOT_ATK2),
    # S_PBOT_ATK2
    (SPR_PLAY, 32773, 4, A_PosAttack, S_PBOT_ATK3),
    # S_PBOT_ATK3
    (SPR_PLAY, 4, 4, A_PosAttack, S_PBOT_ATK4),
    # S_PBOT_ATK4
    (SPR_PLAY, 32773, 4, A_PosAttack, S_PBOT_ATK5),
    # S_PBOT_ATK5
    (SPR_PLAY, 4, 4, A_PosAttack, S_PBOT_ATK6),
    # S_PBOT_ATK6
    (SPR_PLAY, 32773, 4, A_PosAttack, S_PBOT_RUN1),
    # S_PBOT_PAIN
    (SPR_PLAY, 6, 4, None, S_PBOT_PAIN2),
    # S_PBOT_PAIN2
    (SPR_PLAY, 6, 4, A_Pain, S_PBOT_RUN1),
    # S_PBOT_PATK1
    (SPR_PLAY, 4, 4, A_PlayAttack, S_PBOT_PATK2),
    # S_PBOT_PATK2
    (SPR_PLAY, 32773, 4, A_PlayAttack, S_PBOT_PATK3),
    # S_PBOT_PATK3
    (SPR_PLAY, 4, 4, A_PlayAttack, S_PBOT_PATK4),
    # S_PBOT_PATK4
    (SPR_PLAY, 32773, 4, A_PlayAttack, S_PBOT_PATK5),
    # S_PBOT_PATK5
    (SPR_PLAY, 4, 4, A_PlayAttack, S_PBOT_PATK6),
    # S_PBOT_PATK6
    (SPR_PLAY, 32773, 4, A_PlayAttack, S_PBOT_RUN1),

    # S_SARG_STND
    (SPR_SARG, 1, 8, A_Look, S_SARG_STND2),
    # S_SARG_STND2
    (SPR_SARG, 3, 8, A_Look, S_SARG_STND),
    # S_SARG_RUN1
    (SPR_SARG, 0, 2, A_Chase, S_SARG_RUN2),
    # S_SARG_RUN2
    (SPR_SARG, 0, 2, A_Chase, S_SARG_RUN3),
    # S_SARG_RUN3
    (SPR_SARG, 1, 2, A_Chase, S_SARG_RUN4),
    # S_SARG_RUN4
    (SPR_SARG, 1, 2, A_Chase, S_SARG_RUN5),
    # S_SARG_RUN5
    (SPR_SARG, 2, 2, A_Chase, S_SARG_RUN6),
    # S_SARG_RUN6
    (SPR_SARG, 2, 2, A_Chase, S_SARG_RUN7),
    # S_SARG_RUN7
    (SPR_SARG, 3, 2, A_Chase, S_SARG_RUN8),
    # S_SARG_RUN8
    (SPR_SARG, 3, 2, A_Chase, S_SARG_RUN1),
    # S_SARG_ATK1
    (SPR_SARG, 4, 8, A_FaceTarget, S_SARG_ATK2),
    # S_SARG_ATK2
    (SPR_SARG, 5, 8, A_FaceTarget, S_SARG_ATK3),
    # S_SARG_ATK3
    (SPR_SARG, 6, 8, A_SargAttack, S_SARG_RUN1),
    # S_SARG_PAIN1
    (SPR_SARG, 7, 2, None, S_SARG_PAIN2),
    # S_SARG_PAIN2
    (SPR_SARG, 7, 2, A_Pain, S_SARG_RUN1),
    # S_SARG_DIE1
    (SPR_SARG, 8, 8, None, S_SARG_DIE2),
    # S_SARG_DIE2
    (SPR_SARG, 9, 8, A_Scream, S_SARG_DIE3),
    # S_SARG_DIE3
    (SPR_SARG, 10, 4, None, S_SARG_DIE4),
    # S_SARG_DIE4
    (SPR_SARG, 11, 4, A_Fall, S_SARG_DIE5),
    # S_SARG_DIE5
    (SPR_SARG, 12, 4, A_OnDeathTrigger, S_SARG_DIE6),
    # S_SARG_DIE6
    (SPR_SARG, 13, -1, None, S_NULL),
    # S_SARG_RUN0
    (SPR_SARG, 0, 1, A_FadeOut, S_SARG_RUN1),
    # S_SARG_ATK0
    (SPR_SARG, 4, 1, A_FadeOut, S_SARG_ATK1),
    # S_SARG_PAIN0
    (SPR_SARG, 7, 1, A_FadeOut, S_SARG_PAIN1),
    # S_SARG_DIE0
    (SPR_SARG, 8, 1, A_FadeIn, S_SARG_DIE1),

    # S_FATT_STND
    (SPR_FATT, 0, 15, A_Look, S_FATT_STND2),
    # S_FATT_STND2
    (SPR_FATT, 1, 15, A_Look, S_FATT_STND),
    # S_FATT_RUN1
    (SPR_FATT, 0, 4, A_Chase, S_FATT_RUN2),
    # S_FATT_RUN2
    (SPR_FATT, 0, 4, A_Chase, S_FATT_RUN3),
    # S_FATT_RUN3
    (SPR_FATT, 1, 4, A_Chase, S_FATT_RUN4),
    # S_FATT_RUN4
    (SPR_FATT, 1, 4, A_Chase, S_FATT_RUN5),
    # S_FATT_RUN5
    (SPR_FATT, 2, 4, A_Chase, S_FATT_RUN6),
    # S_FATT_RUN6
    (SPR_FATT, 2, 4, A_Chase, S_FATT_RUN7),
    # S_FATT_RUN7
    (SPR_FATT, 3, 4, A_Chase, S_FATT_RUN8),
    # S_FATT_RUN8
    (SPR_FATT, 3, 4, A_Chase, S_FATT_RUN9),
    # S_FATT_RUN9
    (SPR_FATT, 4, 4, A_Chase, S_FATT_RUN10),
    # S_FATT_RUN10
    (SPR_FATT, 4, 4, A_Chase, S_FATT_RUN11),
    # S_FATT_RUN11
    (SPR_FATT, 5, 4, A_Chase, S_FATT_RUN12),
    # S_FATT_RUN12
    (SPR_FATT, 5, 4, A_Chase, S_FATT_RUN1),
    # S_FATT_ATK1
    (SPR_FATT, 7, 20, A_FatRaise, S_FATT_ATK2),
    # S_FATT_ATK2
    (SPR_FATT, 32774, 10, A_FatAttack1, S_FATT_ATK3),
    # S_FATT_ATK3
    (SPR_FATT, 7, 10, A_FaceTarget, S_FATT_ATK4),
    # S_FATT_ATK4
    (SPR_FATT, 32774, 10, A_FatAttack2, S_FATT_ATK5),
    # S_FATT_ATK5
    (SPR_FATT, 7, 10, A_FaceTarget, S_FATT_ATK6),
    # S_FATT_ATK6
    (SPR_FATT, 32774, 10, A_FatAttack3, S_FATT_ATK7),
    # S_FATT_ATK7
    (SPR_FATT, 7, 10, A_FaceTarget, S_FATT_RUN1),
    # S_FATT_PAIN
    (SPR_FATT, 8, 3, None, S_FATT_PAIN2),
    # S_FATT_PAIN2
    (SPR_FATT, 8, 3, A_Pain, S_FATT_RUN1),
    # S_FATT_DIE1
    (SPR_FATT, 9, 6, None, S_FATT_DIE2),
    # S_FATT_DIE2
    (SPR_FATT, 10, 6, A_Scream, S_FATT_DIE3),
    # S_FATT_DIE3
    (SPR_FATT, 11, 6, A_Fall, S_FATT_DIE4),
    # S_FATT_DIE4
    (SPR_FATT, 12, 6, None, S_FATT_DIE5),
    # S_FATT_DIE5
    (SPR_FATT, 13, 6, A_OnDeathTrigger, S_FATT_DIE6),
    # S_FATT_DIE6
    (SPR_FATT, 14, -1, None, S_NULL),

    # S_POSS1_STND
    (SPR_POSS, 0, 10, A_Look, S_POSS1_STND2),
    # S_POSS1_STND2
    (SPR_POSS, 1, 10, A_Look, S_POSS1_STND),
    # S_POSS1_RUN1
    (SPR_POSS, 0, 4, A_Chase, S_POSS1_RUN2),
    # S_POSS1_RUN2
    (SPR_POSS, 0, 4, A_Chase, S_POSS1_RUN3),
    # S_POSS1_RUN3
    (SPR_POSS, 1, 4, A_Chase, S_POSS1_RUN4),
    # S_POSS1_RUN4
    (SPR_POSS, 1, 4, A_Chase, S_POSS1_RUN5),
    # S_POSS1_RUN5
    (SPR_POSS, 2, 4, A_Chase, S_POSS1_RUN6),
    # S_POSS1_RUN6
    (SPR_POSS, 2, 4, A_Chase, S_POSS1_RUN7),
    # S_POSS1_RUN7
    (SPR_POSS, 3, 4, A_Chase, S_POSS1_RUN8),
    # S_POSS1_RUN8
    (SPR_POSS, 3, 4, A_Chase, S_POSS1_RUN1),
    # S_POSS1_ATK1
    (SPR_POSS, 4, 10, A_FaceTarget, S_POSS1_ATK2),
    # S_POSS1_ATK2
    (SPR_POSS, 5, 8, A_PosAttack, S_POSS1_ATK3),
    # S_POSS1_ATK3
    (SPR_POSS, 4, 8, None, S_POSS1_RUN1),
    # S_POSS1_PAIN
    (SPR_POSS, 6, 3, None, S_POSS1_PAIN2),
    # S_POSS1_PAIN2
    (SPR_POSS, 6, 3, A_Pain, S_POSS1_RUN1),
    # S_POSS1_DIE1
    (SPR_POSS, 7, 5, None, S_POSS1_DIE2),
    # S_POSS1_DIE2
    (SPR_POSS, 8, 5, A_Scream, S_POSS1_DIE3),
    # S_POSS1_DIE3
    (SPR_POSS, 9, 5, A_Fall, S_POSS1_DIE4),
    # S_POSS1_DIE4
    (SPR_POSS, 10, 5, A_OnDeathTrigger, S_POSS1_DIE5),
    # S_POSS1_DIE5
    (SPR_POSS, 11, -1, None, S_NULL),
    # S_POSS1_XDIE1
    (SPR_POSS, 12, 5, None, S_POSS1_XDIE2),
    # S_POSS1_XDIE2
    (SPR_POSS, 13, 5, A_XScream, S_POSS1_XDIE3),
    # S_POSS1_XDIE3
    (SPR_POSS, 14, 5, A_Fall, S_POSS1_XDIE4),
    # S_POSS1_XDIE4
    (SPR_POSS, 15, 5, None, S_POSS1_XDIE5),
    # S_POSS1_XDIE5
    (SPR_POSS, 16, 5, None, S_POSS1_XDIE6),
    # S_POSS1_XDIE6
    (SPR_POSS, 17, 5, None, S_POSS1_XDIE7),
    # S_POSS1_XDIE7
    (SPR_POSS, 18, 5, None, S_POSS1_XDIE8),
    # S_POSS1_XDIE8
    (SPR_POSS, 19, 5, A_OnDeathTrigger, S_POSS1_XDIE9),
    # S_POSS1_XDIE9
    (SPR_POSS, 20, -1, None, S_NULL),

    # S_POSS2_STND
    (SPR_POSS, 0, 10, A_Look, S_POSS2_STND2),
    # S_POSS2_STND2
    (SPR_POSS, 1, 10, A_Look, S_POSS2_STND),
    # S_POSS2_RUN1
    (SPR_POSS, 0, 3, A_Chase, S_POSS2_RUN2),
    # S_POSS2_RUN2
    (SPR_POSS, 0, 3, A_Chase, S_POSS2_RUN3),
    # S_POSS2_RUN3
    (SPR_POSS, 1, 3, A_Chase, S_POSS2_RUN4),
    # S_POSS2_RUN4
    (SPR_POSS, 1, 3, A_Chase, S_POSS2_RUN5),
    # S_POSS2_RUN5
    (SPR_POSS, 2, 3, A_Chase, S_POSS2_RUN6),
    # S_POSS2_RUN6
    (SPR_POSS, 2, 3, A_Chase, S_POSS2_RUN7),
    # S_POSS2_RUN7
    (SPR_POSS, 3, 3, A_Chase, S_POSS2_RUN8),
    # S_POSS2_RUN8
    (SPR_POSS, 3, 3, A_Chase, S_POSS2_RUN1),
    # S_POSS2_ATK1
    (SPR_POSS, 4, 10, A_FaceTarget, S_POSS2_ATK2),
    # S_POSS2_ATK2
    (SPR_POSS, 5, 10, A_SPosAttack, S_POSS2_ATK3),
    # S_POSS2_ATK3
    (SPR_POSS, 4, 10, None, S_POSS2_RUN1),
    # S_POSS2_PAIN
    (SPR_POSS, 6, 3, None, S_POSS2_PAIN2),
    # S_POSS2_PAIN2
    (SPR_POSS, 6, 3, A_Pain, S_POSS2_RUN1),
    # S_POSS2_DIE1
    (SPR_POSS, 7, 5, None, S_POSS2_DIE2),
    # S_POSS2_DIE2
    (SPR_POSS, 8, 5, A_Scream, S_POSS2_DIE3),
    # S_POSS2_DIE3
    (SPR_POSS, 9, 5, A_Fall, S_POSS2_DIE4),
    # S_POSS2_DIE4
    (SPR_POSS, 10, 5, A_OnDeathTrigger, S_POSS2_DIE5),
    # S_POSS2_DIE5
    (SPR_POSS, 11, -1, None, S_NULL),
    # S_POSS2_XDIE1
    (SPR_POSS, 12, 5, None, S_POSS2_XDIE2),
    # S_POSS2_XDIE2
    (SPR_POSS, 13, 5, A_XScream, S_POSS2_XDIE3),
    # S_POSS2_XDIE3
    (SPR_POSS, 14, 5, A_Fall, S_POSS2_XDIE4),
    # S_POSS2_XDIE4
    (SPR_POSS, 15, 5, None, S_POSS2_XDIE5),
    # S_POSS2_XDIE5
    (SPR_POSS, 16, 5, None, S_POSS2_XDIE6),
    # S_POSS2_XDIE6
    (SPR_POSS, 17, 5, None, S_POSS2_XDIE7),
    # S_POSS2_XDIE7
    (SPR_POSS, 18, 5, None, S_POSS2_XDIE8),
    # S_POSS2_XDIE8
    (SPR_POSS, 19, 5, A_OnDeathTrigger, S_POSS2_XDIE9),
    # S_POSS2_XDIE9
    (SPR_POSS, 20, -1, None, S_NULL),

    # S_TROO_STND
    (SPR_TROO, 0, 10, A_Look, S_TROO_STND2),
    # S_TROO_STND2
    (SPR_TROO, 1, 10, A_Look, S_TROO_STND),
    # S_TROO_RUN1
    (SPR_TROO, 0, 3, A_Chase, S_TROO_RUN2),
    # S_TROO_RUN2
    (SPR_TROO, 0, 3, A_Chase, S_TROO_RUN3),
    # S_TROO_RUN3
    (SPR_TROO, 1, 3, A_Chase, S_TROO_RUN4),
    # S_TROO_RUN4
    (SPR_TROO, 1, 3, A_Chase, S_TROO_RUN5),
    # S_TROO_RUN5
    (SPR_TROO, 2, 3, A_Chase, S_TROO_RUN6),
    # S_TROO_RUN6
    (SPR_TROO, 2, 3, A_Chase, S_TROO_RUN7),
    # S_TROO_RUN7
    (SPR_TROO, 3, 3, A_Chase, S_TROO_RUN8),
    # S_TROO_RUN8
    (SPR_TROO, 3, 3, A_Chase, S_TROO_RUN1),
    # S_TROO_MELEE1
    (SPR_TROO, 4, 8, A_FaceTarget, S_TROO_MELEE2),
    # S_TROO_MELEE2
    (SPR_TROO, 5, 8, A_FaceTarget, S_TROO_MELEE3),
    # S_TROO_MELEE3
    (SPR_TROO, 6, 6, A_TroopMelee, S_TROO_RUN1),
    # S_TROO_ATK1
    (SPR_TROO, 8, 8, A_FaceTarget, S_TROO_ATK2),
    # S_TROO_ATK2
    (SPR_TROO, 9, 8, A_FaceTarget, S_TROO_ATK3),
    # S_TROO_ATK3
    (SPR_TROO, 10, 6, A_TroopAttack, S_TROO_RUN1),
    # S_TROO_PAIN
    (SPR_TROO, 7, 2, None, S_TROO_PAIN2),
    # S_TROO_PAIN2
    (SPR_TROO, 7, 2, A_Pain, S_TROO_RUN1),
    # S_TROO_DIE1
    (SPR_TROO, 11, 8, None, S_TROO_DIE2),
    # S_TROO_DIE2
    (SPR_TROO, 12, 8, A_Scream, S_TROO_DIE3),
    # S_TROO_DIE3
    (SPR_TROO, 13, 6, A_Fall, S_TROO_DIE4),
    # S_TROO_DIE4
    (SPR_TROO, 14, 6, A_OnDeathTrigger, S_TROO_DIE5),
    # S_TROO_DIE5
    (SPR_TROO, 15, -1, None, S_NULL),
    # S_TROO_XDIE1
    (SPR_TROO, 16, 5, None, S_TROO_XDIE2),
    # S_TROO_XDIE2
    (SPR_TROO, 17, 5, A_XScream, S_TROO_XDIE3),
    # S_TROO_XDIE3
    (SPR_TROO, 18, 5, None, S_TROO_XDIE4),
    # S_TROO_XDIE4
    (SPR_TROO, 19, 5, A_Fall, S_TROO_XDIE5),
    # S_TROO_XDIE5
    (SPR_TROO, 20, 5, None, S_TROO_XDIE6),
    # S_TROO_XDIE6
    (SPR_TROO, 21, 5, None, S_TROO_XDIE7),
    # S_TROO_XDIE7
    (SPR_TROO, 22, 5, A_OnDeathTrigger, S_TROO_XDIE8),
    # S_TROO_XDIE8
    (SPR_TROO, 23, -1, None, S_NULL),

    # S_HEAD_STND
    (SPR_HEAD, 0, 15, A_Look, S_HEAD_STND2),
    # S_HEAD_STND2
    (SPR_HEAD, 1, 15, A_Look, S_HEAD_STND3),
    # S_HEAD_STND3
    (SPR_HEAD, 2, 15, A_Look, S_HEAD_STND4),
    # S_HEAD_STND4
    (SPR_HEAD, 3, 15, A_Look, S_HEAD_STND),
    # S_HEAD_RUN1
    (SPR_HEAD, 0, 3, A_Chase, S_HEAD_RUN2),
    # S_HEAD_RUN2
    (SPR_HEAD, 0, 3, A_Chase, S_HEAD_RUN3),
    # S_HEAD_RUN3
    (SPR_HEAD, 1, 3, A_Chase, S_HEAD_RUN4),
    # S_HEAD_RUN4
    (SPR_HEAD, 1, 3, A_Chase, S_HEAD_RUN5),
    # S_HEAD_RUN5
    (SPR_HEAD, 2, 3, A_Chase, S_HEAD_RUN6),
    # S_HEAD_RUN6
    (SPR_HEAD, 2, 3, A_Chase, S_HEAD_RUN7),
    # S_HEAD_RUN7
    (SPR_HEAD, 3, 3, A_Chase, S_HEAD_RUN8),
    # S_HEAD_RUN8
    (SPR_HEAD, 3, 3, A_Chase, S_HEAD_RUN1),
    # S_HEAD_ATK1
    (SPR_HEAD, 4, 5, A_FaceTarget, S_HEAD_ATK2),
    # S_HEAD_ATK2
    (SPR_HEAD, 5, 5, A_FaceTarget, S_HEAD_ATK3),
    # S_HEAD_ATK3
    (SPR_HEAD, 6, 5, A_FaceTarget, S_HEAD_ATK4),
    # S_HEAD_ATK4
    (SPR_HEAD, 6, 0, A_HeadAttack, S_HEAD_RUN1),
    # S_HEAD_PAIN
    (SPR_HEAD, 1, 3, None, S_HEAD_PAIN2),
    # S_HEAD_PAIN2
    (SPR_HEAD, 1, 3, A_Pain, S_HEAD_PAIN3),
    # S_HEAD_PAIN3
    (SPR_HEAD, 1, 6, None, S_HEAD_RUN1),
    # S_HEAD_DIE1
    (SPR_HEAD, 7, 8, None, S_HEAD_DIE2),
    # S_HEAD_DIE2
    (SPR_HEAD, 8, 8, A_Scream, S_HEAD_DIE3),
    # S_HEAD_DIE3
    (SPR_HEAD, 9, 8, None, S_HEAD_DIE4),
    # S_HEAD_DIE4
    (SPR_HEAD, 10, 8, A_Fall, S_HEAD_DIE5),
    # S_HEAD_DIE5
    (SPR_HEAD, 11, 8, A_OnDeathTrigger, S_HEAD_DIE6),
    # S_HEAD_DIE6
    (SPR_HEAD, 12, -1, None, S_NULL),

    # S_BOSS1_STND
    (SPR_BOSS, 0, 10, A_Look, S_BOSS1_STND2),
    # S_BOSS1_STND2
    (SPR_BOSS, 1, 10, A_Look, S_BOSS1_STND),
    # S_BOSS1_RUN1
    (SPR_BOSS, 0, 3, A_Chase, S_BOSS1_RUN2),
    # S_BOSS1_RUN2
    (SPR_BOSS, 0, 3, A_Chase, S_BOSS1_RUN3),
    # S_BOSS1_RUN3
    (SPR_BOSS, 1, 3, A_Chase, S_BOSS1_RUN4),
    # S_BOSS1_RUN4
    (SPR_BOSS, 1, 3, A_Chase, S_BOSS1_RUN5),
    # S_BOSS1_RUN5
    (SPR_BOSS, 2, 3, A_Chase, S_BOSS1_RUN6),
    # S_BOSS1_RUN6
    (SPR_BOSS, 2, 3, A_Chase, S_BOSS1_RUN7),
    # S_BOSS1_RUN7
    (SPR_BOSS, 3, 3, A_Chase, S_BOSS1_RUN8),
    # S_BOSS1_RUN8
    (SPR_BOSS, 3, 3, A_Chase, S_BOSS1_RUN1),
    # S_BOSS1_ATK1
    (SPR_BOSS, 4, 8, A_FaceTarget, S_BOSS1_ATK2),
    # S_BOSS1_ATK2
    (SPR_BOSS, 5, 8, A_FaceTarget, S_BOSS1_ATK3),
    # S_BOSS1_ATK3
    (SPR_BOSS, 6, 8, A_BruisAttack, S_BOSS1_RUN1),
    # S_BOSS1_PAIN
    (SPR_BOSS, 7, 2, None, S_BOSS1_PAIN2),
    # S_BOSS1_PAIN2
    (SPR_BOSS, 7, 2, A_Pain, S_BOSS1_RUN1),
    # S_BOSS1_DIE1
    (SPR_BOSS, 8, 8, None, S_BOSS1_DIE2),
    # S_BOSS1_DIE2
    (SPR_BOSS, 9, 8, A_Scream, S_BOSS1_DIE3),
    # S_BOSS1_DIE3
    (SPR_BOSS, 10, 8, None, S_BOSS1_DIE4),
    # S_BOSS1_DIE4
    (SPR_BOSS, 11, 8, A_Fall, S_BOSS1_DIE5),
    # S_BOSS1_DIE5
    (SPR_BOSS, 12, 8, A_OnDeathTrigger, S_BOSS1_DIE6),
    # S_BOSS1_DIE6
    (SPR_BOSS, 13, -1, None, S_NULL),

    # S_BOSS2_STND
    (SPR_BOSS, 0, 10, A_Look, S_BOSS2_STND2),
    # S_BOSS2_STND2
    (SPR_BOSS, 1, 10, A_Look, S_BOSS2_STND),
    # S_BOSS2_RUN1
    (SPR_BOSS, 0, 3, A_Chase, S_BOSS2_RUN2),
    # S_BOSS2_RUN2
    (SPR_BOSS, 0, 3, A_Chase, S_BOSS2_RUN3),
    # S_BOSS2_RUN3
    (SPR_BOSS, 1, 3, A_Chase, S_BOSS2_RUN4),
    # S_BOSS2_RUN4
    (SPR_BOSS, 1, 3, A_Chase, S_BOSS2_RUN5),
    # S_BOSS2_RUN5
    (SPR_BOSS, 2, 3, A_Chase, S_BOSS2_RUN6),
    # S_BOSS2_RUN6
    (SPR_BOSS, 2, 3, A_Chase, S_BOSS2_RUN7),
    # S_BOSS2_RUN7
    (SPR_BOSS, 3, 3, A_Chase, S_BOSS2_RUN8),
    # S_BOSS2_RUN8
    (SPR_BOSS, 3, 3, A_Chase, S_BOSS2_RUN1),
    # S_BOSS2_ATK1
    (SPR_BOSS, 4, 8, A_FaceTarget, S_BOSS2_ATK2),
    # S_BOSS2_ATK2
    (SPR_BOSS, 5, 8, A_FaceTarget, S_BOSS2_ATK3),
    # S_BOSS2_ATK3
    (SPR_BOSS, 6, 8, A_BruisAttack, S_BOSS2_RUN1),
    # S_BOSS2_PAIN
    (SPR_BOSS, 7, 2, None, S_BOSS2_PAIN2),
    # S_BOSS2_PAIN2
    (SPR_BOSS, 7, 2, A_Pain, S_BOSS2_RUN1),
    # S_BOSS2_DIE1
    (SPR_BOSS, 8, 8, None, S_BOSS2_DIE2),
    # S_BOSS2_DIE2
    (SPR_BOSS, 9, 8, A_Scream, S_BOSS2_DIE3),
    # S_BOSS2_DIE3
    (SPR_BOSS, 10, 8, None, S_BOSS2_DIE4),
    # S_BOSS2_DIE4
    (SPR_BOSS, 11, 8, A_Fall, S_BOSS2_DIE5),
    # S_BOSS2_DIE5
    (SPR_BOSS, 12, 8, A_OnDeathTrigger, S_BOSS2_DIE6),
    # S_BOSS2_DIE6
    (SPR_BOSS, 13, -1, None, S_NULL),

    # S_SKUL_STND
    (SPR_SKUL, 0, 5, A_Look, S_SKUL_STND2),
    # S_SKUL_STND2
    (SPR_SKUL, 1, 5, A_Look, S_SKUL_STND3),
    # S_SKUL_STND3
    (SPR_SKUL, 2, 5, A_Look, S_SKUL_STND),
    # S_SKUL_RUN1
    (SPR_SKUL, 0, 3, A_Chase, S_SKUL_RUN2),
    # S_SKUL_RUN2
    (SPR_SKUL, 1, 3, A_Chase, S_SKUL_RUN3),
    # S_SKUL_RUN3
    (SPR_SKUL, 2, 3, A_Chase, S_SKUL_RUN1),
    # S_SKUL_ATK1
    (SPR_SKUL, 3, 6, A_FaceTarget, S_SKUL_ATK2),
    # S_SKUL_ATK2
    (SPR_SKUL, 4, 4, A_SkullAttack, S_SKUL_ATK3),
    # S_SKUL_ATK3
    (SPR_SKUL, 3, 4, None, S_SKUL_ATK4),
    # S_SKUL_ATK4
    (SPR_SKUL, 4, 4, None, S_SKUL_ATK3),
    # S_SKUL_PAIN
    (SPR_SKUL, 5, 3, None, S_SKUL_PAIN2),
    # S_SKUL_PAIN2
    (SPR_SKUL, 5, 3, A_Pain, S_SKUL_RUN1),
    # S_SKUL_DIE1
    (SPR_SKUL, 32774, 5, None, S_SKUL_DIE2),
    # S_SKUL_DIE2
    (SPR_SKUL, 32775, 5, A_Scream, S_SKUL_DIE3),
    # S_SKUL_DIE3
    (SPR_SKUL, 32776, 5, A_Fall, S_SKUL_DIE4),
    # S_SKUL_DIE4
    (SPR_SKUL, 32777, 5, A_OnDeathTrigger, S_SKUL_DIE5),
    # S_SKUL_DIE5
    (SPR_SKUL, 32778, 4, A_SkullSetAlpha, S_SKUL_DIE6),
    # S_SKUL_DIE6
    (SPR_SKUL, 32779, 3, None, S_SKUL_DIE7),
    # S_SKUL_DIE7
    (SPR_SKUL, 32780, 2, None, S_SKUL_DIE8),
    # S_SKUL_DIE8
    (SPR_SKUL, 32781, 2, None, S_SKUL_DIE9),
    # S_SKUL_DIE9
    (SPR_SKUL, 32782, 1, None, S_SKUL_DIE10),
    # S_SKUL_DIE10
    (SPR_SKUL, 32783, 1, None, S_NULL),

    # S_BSPI_STND
    (SPR_BSPI, 0, 10, A_Look, S_BSPI_STND2),
    # S_BSPI_STND2
    (SPR_BSPI, 1, 10, A_Look, S_BSPI_STND),
    # S_BSPI_RUN1
    (SPR_BSPI, 0, 20, None, S_BSPI_RUN2),
    # S_BSPI_RUN2
    (SPR_BSPI, 0, 3, A_BabyMetal, S_BSPI_RUN3),
    # S_BSPI_RUN3
    (SPR_BSPI, 0, 3, A_Chase, S_BSPI_RUN4),
    # S_BSPI_RUN4
    (SPR_BSPI, 1, 3, A_Chase, S_BSPI_RUN5),
    # S_BSPI_RUN5
    (SPR_BSPI, 1, 3, A_Chase, S_BSPI_RUN6),
    # S_BSPI_RUN6
    (SPR_BSPI, 2, 3, A_Chase, S_BSPI_RUN7),
    # S_BSPI_RUN7
    (SPR_BSPI, 2, 3, A_Chase, S_BSPI_RUN8),
    # S_BSPI_RUN8
    (SPR_BSPI, 3, 3, A_Chase, S_BSPI_RUN9),
    # S_BSPI_RUN9
    (SPR_BSPI, 3, 3, A_Chase, S_BSPI_RUN2),
    # S_BSPI_ATK1
    (SPR_BSPI, 0, 15, A_BspiFaceTarget, S_BSPI_ATK2),
    # S_BSPI_ATK2
    (SPR_BSPI, 32772, 6, A_BspiAttack, S_BSPI_ATK3),
    # S_BSPI_ATK3
    (SPR_BSPI, 32772, 1, A_SpidRefire, S_BSPI_ATK2),
    # S_BSPI_PAIN
    (SPR_BSPI, 5, 3, None, S_BSPI_PAIN2),
    # S_BSPI_PAIN2
    (SPR_BSPI, 5, 3, A_Pain, S_BSPI_RUN2),
    # S_BSPI_DIE1
    (SPR_BSPI, 6, 20, A_Scream, S_BSPI_DIE2),
    # S_BSPI_DIE2
    (SPR_BSPI, 7, 7, A_Fall, S_BSPI_DIE3),
    # S_BSPI_DIE3
    (SPR_BSPI, 8, 7, None, S_BSPI_DIE4),
    # S_BSPI_DIE4
    (SPR_BSPI, 9, 7, None, S_BSPI_DIE5),
    # S_BSPI_DIE5
    (SPR_BSPI, 10, 7, A_OnDeathTrigger, S_BSPI_DIE6),
    # S_BSPI_DIE6
    (SPR_BSPI, 11, -1, None, S_NULL),

    # S_CYBR_STND
    (SPR_CYBR, 5, 10, A_Look, S_CYBR_STND),
    # S_CYBR_RUN1
    (SPR_CYBR, 0, 4, A_Hoof, S_CYBR_RUN2),
    # S_CYBR_RUN2
    (SPR_CYBR, 0, 4, A_Chase, S_CYBR_RUN3),
    # S_CYBR_RUN3
    (SPR_CYBR, 1, 4, A_Chase, S_CYBR_RUN4),
    # S_CYBR_RUN4
    (SPR_CYBR, 1, 4, A_Chase, S_CYBR_RUN5),
    # S_CYBR_RUN5
    (SPR_CYBR, 2, 4, A_Chase, S_CYBR_RUN6),
    # S_CYBR_RUN6
    (SPR_CYBR, 2, 4, A_Chase, S_CYBR_RUN7),
    # S_CYBR_RUN7
    (SPR_CYBR, 3, 4, A_Metal, S_CYBR_RUN8),
    # S_CYBR_RUN8
    (SPR_CYBR, 3, 4, A_Chase, S_CYBR_RUN1),
    # S_CYBR_ATK1
    (SPR_CYBR, 32772, 6, A_FaceTarget, S_CYBR_ATK2),
    # S_CYBR_ATK2
    (SPR_CYBR, 5, 12, A_CyberAttack, S_CYBR_ATK3),
    # S_CYBR_ATK3
    (SPR_CYBR, 32772, 12, A_FaceTarget, S_CYBR_ATK4),
    # S_CYBR_ATK4
    (SPR_CYBR, 5, 12, A_CyberAttack, S_CYBR_ATK5),
    # S_CYBR_ATK5
    (SPR_CYBR, 32772, 12, A_FaceTarget, S_CYBR_ATK6),
    # S_CYBR_ATK6
    (SPR_CYBR, 5, 12, A_CyberAttack, S_CYBR_RUN1),
    # S_CYBR_PAIN
    (SPR_CYBR, 5, 10, A_Pain, S_CYBR_RUN1),
    # S_CYBR_DIE1
    (SPR_CYBR, 6, 30, A_CyberDeathEvent, S_CYBR_DIE2),
    # S_CYBR_DIE2
    (SPR_CYBR, 7, 8, None, S_CYBR_DIE3),
    # S_CYBR_DIE3
    (SPR_CYBR, 8, 7, None, S_CYBR_DIE4),
    # S_CYBR_DIE4
    (SPR_CYBR, 9, 6, None, S_CYBR_DIE5),
    # S_CYBR_DIE5
    (SPR_CYBR, 10, 5, None, S_CYBR_DIE6),
    # S_CYBR_DIE6
    (SPR_CYBR, 11, 4, A_Fall, S_CYBR_DIE7),
    # S_CYBR_DIE7
    (SPR_CYBR, 12, 4, None, S_CYBR_DIE8),
    # S_CYBR_DIE8
    (SPR_CYBR, 13, 4, A_OnDeathTrigger, S_CYBR_DIE9),
    # S_CYBR_DIE9
    (SPR_CYBR, 14, -1, None, S_NULL),
    # S_CYBR_TITLE1
    (SPR_CYBR, 5, 1, A_TargetCamera, S_CYBR_TITLE1),
    # S_CYBR_TITLE2
    (SPR_CYBR, 32772, 18, A_CyberAttack, S_CYBR_TITLE3),
    # S_CYBR_TITLE3
    (SPR_CYBR, 5, 18, A_FaceTarget, S_CYBR_TITLE2),

    # S_PAIN_STND
    (SPR_PAIN, 0, 5, A_Look, S_PAIN_STND),
    # S_PAIN_RUN
    (SPR_PAIN, 0, 3, A_Chase, S_PAIN_RUN),
    # S_PAIN_ATK1
    (SPR_PAIN, 32769, 5, A_FaceTarget, S_PAIN_ATK2),
    # S_PAIN_ATK2
    (SPR_PAIN, 32769, 5, A_FaceTarget, S_PAIN_ATK3),
    # S_PAIN_ATK3
    (SPR_PAIN, 32770, 5, A_FaceTarget, S_PAIN_ATK4),
    # S_PAIN_ATK4
    (SPR_PAIN, 32770, 0, A_PainAttack, S_PAIN_RUN),
    # S_PAIN_PAIN
    (SPR_PAIN, 3, 6, None, S_PAIN_PAIN2),
    # S_PAIN_PAIN2
    (SPR_PAIN, 3, 6, A_Pain, S_PAIN_RUN),
    # S_PAIN_DIE1
    (SPR_PAIN, 32772, 8, None, S_PAIN_DIE2),
    # S_PAIN_DIE2
    (SPR_PAIN, 32773, 8, A_Scream, S_PAIN_DIE3),
    # S_PAIN_DIE3
    (SPR_PAIN, 32774, 8, A_PainDie, S_PAIN_DIE4),
    # S_PAIN_DIE4
    (SPR_PAIN, 32775, 8, A_PainDeathEvent, S_PAIN_DIE5),
    # S_PAIN_DIE5
    (SPR_PAIN, 32776, 5, A_PainDeathEvent, S_PAIN_DIE6),
    # S_PAIN_DIE6
    (SPR_PAIN, 32777, 5, A_PainDeathEvent, S_PAIN_DIE7),
    # S_PAIN_DIE7
    (SPR_PAIN, 32778, 5, None, S_PAIN_DIE8),
    # S_PAIN_DIE8
    (SPR_PAIN, 32779, 5, None, S_NULL),

    # S_RECT_STND
    (SPR_RECT, 0, 8, A_Look, S_RECT_STND2),
    # S_RECT_STND2
    (SPR_RECT, 1, 8, A_Look, S_RECT_STND3),
    # S_RECT_STND3
    (SPR_RECT, 2, 8, A_Look, S_RECT_STND4),
    # S_RECT_STND4
    (SPR_RECT, 3, 8, A_Look, S_RECT_STND),
    # S_RECT_RUN1
    (SPR_RECT, 0, 3, A_RectChase, S_RECT_RUN2),
    # S_RECT_RUN2
    (SPR_RECT, 0, 3, A_RectChase, S_RECT_RUN3),
    # S_RECT_RUN3
    (SPR_RECT, 0, 3, A_RectChase, S_RECT_RUN4),
    # S_RECT_RUN4
    (SPR_RECT, 1, 3, A_RectChase, S_RECT_RUN5),
    # S_RECT_RUN5
    (SPR_RECT, 1, 3, A_RectChase, S_RECT_RUN6),
    # S_RECT_RUN6
    (SPR_RECT, 1, 3, A_RectChase, S_RECT_RUN7),
    # S_RECT_RUN7
    (SPR_RECT, 2, 3, A_RectChase, S_RECT_RUN8),
    # S_RECT_RUN8
    (SPR_RECT, 2, 3, A_RectChase, S_RECT_RUN9),
    # S_RECT_RUN9
    (SPR_RECT, 2, 3, A_RectChase, S_RECT_RUN10),
    # S_RECT_RUN10
    (SPR_RECT, 3, 3, A_RectChase, S_RECT_RUN11),
    # S_RECT_RUN11
    (SPR_RECT, 3, 3, A_RectChase, S_RECT_RUN12),
    # S_RECT_RUN12
    (SPR_RECT, 3, 3, A_RectChase, S_RECT_RUN1),
    # S_RECT_ATK1
    (SPR_RECT, 32774, 12, A_RectGroundFire, S_RECT_ATK2),
    # S_RECT_ATK2
    (SPR_RECT, 4, 12, None, S_RECT_ATK3),
    # S_RECT_ATK3
    (SPR_RECT, 32773, 12, A_RectMissile, S_RECT_ATK4),
    # S_RECT_ATK4
    (SPR_RECT, 4, 8, None, S_RECT_RUN1),
    # S_RECT_PAIN
    (SPR_RECT, 7, 18, A_Pain, S_RECT_ATK1),
    # S_RECT_DIE1
    (SPR_RECT, 8, 60, A_RectDeathEvent, S_RECT_DIE2),
    # S_RECT_DIE2
    (SPR_RECT, 9, 8, None, S_RECT_DIE3),
    # S_RECT_DIE3
    (SPR_RECT, 10, 8, None, S_RECT_DIE4),
    # S_RECT_DIE4
    (SPR_RECT, 11, 5, None, S_RECT_DIE5),
    # S_RECT_DIE5
    (SPR_RECT, 12, 4, None, S_RECT_DIE6),
    # S_RECT_DIE6
    (SPR_RECT, 13, 3, A_OnDeathTrigger, S_RECT_DIE7),
    # S_RECT_DIE7
    (SPR_RECT, 14, 2, None, S_NULL),

    # S_FAKEITEM
    (SPR_SPOT, 32768, -1, None, S_NULL),

    # S_ROCKET
    (SPR_MISL, 32768, 2, A_SpawnSmoke, S_ROCKET),
    # S_ROCKET_DIE1
    (SPR_MISL, 32769, 3, A_Explode, S_ROCKET_DIE2),
    # S_ROCKET_DIE2
    (SPR_MISL, 32769, 3, A_FadeAlpha, S_ROCKET_DIE3),
    # S_ROCKET_DIE3
    (SPR_MISL, 32770, 3, A_FadeAlpha, S_ROCKET_DIE4),
    # S_ROCKET_DIE4
    (SPR_MISL, 32770, 3, A_FadeAlpha, S_ROCKET_DIE5),
    # S_ROCKET_DIE5
    (SPR_MISL, 32771, 2, A_FadeAlpha, S_ROCKET_DIE6),
    # S_ROCKET_DIE6
    (SPR_MISL, 32772, 2, None, S_ROCKET_DIE7),
    # S_ROCKET_DIE7
    (SPR_MISL, 32773, 2, None, S_NULL),

    # S_PLASMA1
    (SPR_PLSS, 32768, 3, None, S_PLASMA2),
    # S_PLASMA2
    (SPR_PLSS, 32769, 3, None, S_PLASMA1),
    # S_PLASMA_DIE1
    (SPR_PLSS, 32770, 2, A_FadeAlpha, S_PLASMA_DIE2),
    # S_PLASMA_DIE2
    (SPR_PLSS, 32771, 2, None, S_PLASMA_DIE3),
    # S_PLASMA_DIE3
    (SPR_PLSS, 32772, 2, None, S_PLASMA_DIE4),
    # S_PLASMA_DIE4
    (SPR_PLSS, 32773, 2, None, S_PLASMA_DIE5),
    # S_PLASMA_DIE5
    (SPR_PLSS, 32774, 2, None, S_PLASMA_DIE6),
    # S_PLASMA_DIE6
    (SPR_PLSS, 32775, 2, None, S_NULL),

    # S_BFGBALL1
    (SPR_BFS1, 32768, 2, None, S_BFGBALL2),
    # S_BFGBALL2
    (SPR_BFS1, 32769, 2, None, S_BFGBALL1),
    # S_BFGBALL_DIE1
    (SPR_BFS1, 32770, 8, A_BFGFlash, S_BFGBALL_DIE2),
    # S_BFGBALL_DIE2
    (SPR_BFS1, 32771, 6, A_FadeAlpha, S_BFGBALL_DIE3),
    # S_BFGBALL_DIE3
    (SPR_BFS1, 32772, 3, A_BFGSpray, S_BFGBALL_DIE4),
    # S_BFGBALL_DIE4
    (SPR_BFS1, 32773, 3, A_FadeAlpha, S_BFGBALL_DIE5),
    # S_BFGBALL_DIE5
    (SPR_BFS1, 32774, 2, None, S_BFGBALL_DIE6),
    # S_BFGBALL_DIE6
    (SPR_BFS1, 32775, 2, None, S_NULL),

    # S_LASER1
    (SPR_LASS, 32768, 3, None, S_LASER2),
    # S_LASER2
    (SPR_LASS, 32769, 3, None, S_LASER1),

    # S_TBALL1
    (SPR_BAL1, 32768, 4, None, S_TBALL2),
    # S_TBALL2
    (SPR_BAL1, 32769, 4, None, S_TBALL3),
    # S_TBALL3
    (SPR_BAL1, 32770, 4, None, S_TBALL1),
    # S_TBALL_DIE1
    (SPR_BAL1, 32771, 1, None, S_TBALL_DIE2),
    # S_TBALL_DIE2
    (SPR_BAL1, 32772, 1, None, S_TBALL_DIE3),
    # S_TBALL_DIE3
    (SPR_BAL1, 32773, 1, None, S_TBALL_DIE4),
    # S_TBALL_DIE4
    (SPR_BAL1, 32774, 1, None, S_TBALL_DIE5),
    # S_TBALL_DIE5
    (SPR_BAL1, 32775, 1, None, S_TBALL_DIE6),
    # S_TBALL_DIE6
    (SPR_BAL1, 32776, 1, None, S_NULL),

    # S_NBALL1
    (SPR_BAL3, 32768, 4, None, S_NBALL2),
    # S_NBALL2
    (SPR_BAL3, 32769, 4, None, S_NBALL3),
    # S_NBALL3
    (SPR_BAL3, 32770, 4, None, S_NBALL1),
    # S_NBALL_DIE1
    (SPR_BAL3, 32771, 2, None, S_NBALL_DIE2),
    # S_NBALL_DIE2
    (SPR_BAL3, 32772, 2, None, S_NBALL_DIE3),
    # S_NBALL_DIE3
    (SPR_BAL3, 32773, 2, None, S_NBALL_DIE4),
    # S_NBALL_DIE4
    (SPR_BAL3, 32774, 2, None, S_NBALL_DIE5),
    # S_NBALL_DIE5
    (SPR_BAL3, 32775, 2, None, S_NBALL_DIE6),
    # S_NBALL_DIE6
    (SPR_BAL3, 32776, 2, None, S_NULL),

    # S_CBALL1
    (SPR_BAL2, 32768, 4, None, S_CBALL2),
    # S_CBALL2
    (SPR_BAL2, 32769, 4, None, S_CBALL3),
    # S_CBALL3
    (SPR_BAL2, 32770, 4, None, S_CBALL1),
    # S_CBALL_DIE1
    (SPR_BAL2, 32771, 6, A_MissileSetAlpha, S_CBALL_DIE2),
    # S_CBALL_DIE2
    (SPR_BAL2, 32772, 5, None, S_CBALL_DIE3),
    # S_CBALL_DIE3
    (SPR_BAL2, 32773, 2, None, S_CBALL_DIE4),
    # S_CBALL_DIE4
    (SPR_BAL2, 32774, 2, None, S_CBALL_DIE5),
    # S_CBALL_DIE5
    (SPR_BAL2, 32775, 2, None, S_NULL),

    # S_BGBALL1
    (SPR_BAL7, 32768, 4, None, S_BGBALL2),
    # S_BGBALL2
    (SPR_BAL7, 32769, 4, None, S_BGBALL1),
    # S_BGBALL_DIE1
    (SPR_BAL7, 32770, 3, None, S_BGBALL_DIE2),
    # S_BGBALL_DIE2
    (SPR_BAL7, 32771, 3, A_FadeAlpha, S_BGBALL_DIE3),
    # S_BGBALL_DIE3
    (SPR_BAL7, 32772, 3, A_FadeAlpha, S_BGBALL_DIE4),
    # S_BGBALL_DIE4
    (SPR_BAL7, 32773, 2, None, S_BGBALL_DIE5),
    # S_BGBALL_DIE5
    (SPR_BAL7, 32774, 2, None, S_BGBALL_DIE6),
    # S_BGBALL_DIE6
    (SPR_BAL7, 32775, 2, None, S_NULL),

    # S_BRBALL1
    (SPR_BAL8, 32768, 4, None, S_BRBALL2),
    # S_BRBALL2
    (SPR_BAL8, 32769, 4, None, S_BRBALL1),
    # S_BRBALL_DIE1
    (SPR_BAL8, 32770, 3, None, S_BRBALL_DIE2),
    # S_BRBALL_DIE2
    (SPR_BAL8, 32771, 3, A_FadeAlpha, S_BRBALL_DIE3),
    # S_BRBALL_DIE3
    (SPR_BAL8, 32772, 3, A_FadeAlpha, S_BRBALL_DIE4),
    # S_BRBALL_DIE4
    (SPR_BAL8, 32773, 2, None, S_BRBALL_DIE5),
    # S_BRBALL_DIE5
    (SPR_BAL8, 32774, 2, None, S_BRBALL_DIE6),
    # S_BRBALL_DIE6
    (SPR_BAL8, 32775, 2, None, S_NULL),

    # S_APLS1
    (SPR_APLS, 32768, 2, None, S_APLS2),
    # S_APLS2
    (SPR_APLS, 32769, 2, None, S_APLS1),
    # S_APLS_DIE1
    (SPR_APLS, 32770, 3, None, S_APLS_DIE2),
    # S_APLS_DIE2
    (SPR_APLS, 32771, 3, None, S_APLS_DIE3),
    # S_APLS_DIE3
    (SPR_APLS, 32772, 3, None, S_APLS_DIE4),
    # S_APLS_DIE4
    (SPR_APLS, 32773, 3, None, S_APLS_DIE5),
    # S_APLS_DIE5
    (SPR_APLS, 32774, 3, None, S_APLS_DIE6),
    # S_APLS_DIE6
    (SPR_APLS, 32775, 3, None, S_NULL),

    # S_MANF1
    (SPR_MANF, 32768, 2, None, S_MANF2),
    # S_MANF2
    (SPR_MANF, 32769, 2, None, S_MANF3),
    # S_MANF3
    (SPR_MANF, 32770, 2, None, S_MANF1),
    # S_MANF_DIE1
    (SPR_MANF, 32771, 6, None, S_MANF_DIE2),
    # S_MANF_DIE2
    (SPR_MANF, 32772, 4, A_FadeAlpha, S_MANF_DIE3),
    # S_MANF_DIE3
    (SPR_MANF, 32773, 3, A_FadeAlpha, S_MANF_DIE4),
    # S_MANF_DIE4
    (SPR_MANF, 32774, 2, A_FadeAlpha, S_MANF_DIE5),
    # S_MANF_DIE5
    (SPR_MANF, 32775, 2, None, S_MANF_DIE6),
    # S_MANF_DIE6
    (SPR_MANF, 32776, 2, None, S_NULL),

    # S_TRCR1
    (SPR_TRCR, 32768, 3, A_Tracer, S_TRCR2),
    # S_TRCR2
    (SPR_TRCR, 32769, 3, A_Tracer, S_TRCR1),
    # S_TRCR_DIE1
    (SPR_TRCR, 32770, 4, A_FadeAlpha, S_TRCR_DIE2),
    # S_TRCR_DIE2
    (SPR_TRCR, 32771, 3, A_FadeAlpha, S_TRCR_DIE3),
    # S_TRCR_DIE3
    (SPR_TRCR, 32772, 2, A_FadeAlpha, S_TRCR_DIE4),
    # S_TRCR_DIE4
    (SPR_TRCR, 32773, 2, A_FadeAlpha, S_TRCR_DIE5),
    # S_TRCR_DIE5
    (SPR_TRCR, 32774, 2, None, S_TRCR_DIE6),
    # S_TRCR_DIE6
    (SPR_TRCR, 32775, 2, None, S_TRCR_DIE7),
    # S_TRCR_DIE7
    (SPR_TRCR, 32776, 2, None, S_NULL),

    # S_DART
    (SPR_DART, 32768, -1, None, S_NULL),

    # S_RFIRE1
    (SPR_FIRE, 32768, 3, A_MoveGroundFire, S_RFIRE2),
    # S_RFIRE2
    (SPR_FIRE, 32769, 3, A_MoveGroundFire, S_RFIRE3),
    # S_RFIRE3
    (SPR_FIRE, 32770, 3, A_MoveGroundFire, S_RFIRE4),
    # S_RFIRE4
    (SPR_FIRE, 32771, 3, A_MoveGroundFire, S_RFIRE1),

    # S_RBALL1
    (SPR_RBAL, 0, 2, A_RectTracer, S_RBALL2),
    # S_RBALL2
    (SPR_RBAL, 1, 2, A_RectTracer, S_RBALL1),
    # S_RBALL_DIE1
    (SPR_RBAL, 32770, 4, None, S_RBALL_DIE2),
    # S_RBALL_DIE2
    (SPR_RBAL, 32771, 3, A_MissileSetAlpha, S_RBALL_DIE3),
    # S_RBALL_DIE3
    (SPR_RBAL, 32772, 2, None, S_RBALL_DIE4),
    # S_RBALL_DIE4
    (SPR_RBAL, 32773, 2, None, S_RBALL_DIE5),
    # S_RBALL_DIE5
    (SPR_RBAL, 32774, 2, None, S_RBALL_DIE6),
    # S_RBALL_DIE6
    (SPR_RBAL, 32775, 2, None, S_NULL),

    # S_PUF21
    (SPR_PUF2, 32768, 2, None, S_PUF22),
    # S_PUF22
    (SPR_PUF2, 32769, 2, None, S_PUF23),
    # S_PUF23
    (SPR_PUF2, 32770, 2, None, S_PUF24),
    # S_PUF24
    (SPR_PUF2, 32771, 2, None, S_PUF25),
    # S_PUF25
    (SPR_PUF2, 32772, 2, None, S_NULL),

    # S_PUF31
    (SPR_PUF3, 32768, 2, None, S_PUF32),
    # S_PUF32
    (SPR_PUF3, 32769, 2, None, S_PUF33),
    # S_PUF33
    (SPR_PUF3, 32770, 2, None, S_PUF34),
    # S_PUF34
    (SPR_PUF3, 32771, 2, None, S_PUF35),
    # S_PUF35
    (SPR_PUF3, 32772, 2, None, S_NULL),

    # S_PUFF1
    (SPR_PUFF, 32768, 4, None, S_PUFF2),
    # S_PUFF2
    (SPR_PUFF, 32769, 3, None, S_PUFF3),
    # S_PUFF3
    (SPR_PUFF, 2, 3, None, S_PUFF4),
    # S_PUFF4
    (SPR_PUFF, 3, 3, None, S_PUFF5),
    # S_PUFF5
    (SPR_PUFF, 4, 3, None, S_PUFF6),
    # S_PUFF6
    (SPR_PUFF, 5, 3, None, S_NULL),

    # S_BLOOD1
    (SPR_BLUD, 0, 6, None, S_BLOOD2),
    # S_BLOOD2
    (SPR_BLUD, 1, 6, None, S_BLOOD3),
    # S_BLOOD3
    (SPR_BLUD, 2, 6, None, S_BLOOD4),
    # S_BLOOD4
    (SPR_BLUD, 3, 6, None, S_NULL),

    # S_CORPSE
    (SPR_A027, 0, -1, None, S_NULL),

    # S_TFOG1
    (SPR_TFOG, 32772, 3, None, S_TFOG2),
    # S_TFOG2
    (SPR_TFOG, 32771, 3, None, S_TFOG3),
    # S_TFOG3
    (SPR_TFOG, 32770, 3, None, S_TFOG4),
    # S_TFOG4
    (SPR_TFOG, 32769, 3, None, S_TFOG5),
    # S_TFOG5
    (SPR_TFOG, 32768, 3, None, S_TFOG6),
    # S_TFOG6
    (SPR_TFOG, 32769, 3, None, S_TFOG7),
    # S_TFOG7
    (SPR_TFOG, 32770, 3, None, S_TFOG8),
    # S_TFOG8
    (SPR_TFOG, 32771, 3, None, S_TFOG9),
    # S_TFOG9
    (SPR_TFOG, 32772, 3, None, S_TFOG10),
    # S_TFOG10
    (SPR_TFOG, 32773, 3, None, S_TFOG11),
    # S_TFOG11
    (SPR_TFOG, 32774, 3, None, S_TFOG12),
    # S_TFOG12
    (SPR_TFOG, 32775, 3, None, S_NULL),

    # S_BFGEXP1
    (SPR_BFE2, 32768, 4, None, S_BFGEXP2),
    # S_BFGEXP2
    (SPR_BFE2, 32769, 3, A_FadeAlpha, S_BFGEXP3),
    # S_BFGEXP3
    (SPR_BFE2, 32770, 2, None, S_BFGEXP4),
    # S_BFGEXP4
    (SPR_BFE2, 32771, 2, None, S_BFGEXP5),
    # S_BFGEXP5
    (SPR_BFE2, 32772, 2, None, S_BFGEXP6),
    # S_BFGEXP6
    (SPR_BFE2, 32773, 2, None, S_NULL),

    # S_ARMOR1A
    (SPR_ARM1, 32768, 6, None, S_ARMOR1B),
    # S_ARMOR1B
    (SPR_ARM1, 32769, 6, None, S_ARMOR1A),
    # S_ARMOR2A
    (SPR_ARM2, 32768, 6, None, S_ARMOR2B),
    # S_ARMOR2B
    (SPR_ARM2, 32769, 6, None, S_ARMOR2A),

    # S_BONUS1A
    (SPR_BON1, 0, 3, None, S_BONUS1B),
    # S_BONUS1B
    (SPR_BON1, 1, 3, None, S_BONUS1C),
    # S_BONUS1C
    (SPR_BON1, 2, 3, None, S_BONUS1D),
    # S_BONUS1D
    (SPR_BON1, 3, 3, None, S_BONUS1A),

    # S_BONUS2A
    (SPR_BON2, 0, 3, None, S_BONUS2B),
    # S_BONUS2B
    (SPR_BON2, 1, 3, None, S_BONUS2C),
    # S_BONUS2C
    (SPR_BON2, 2, 3, None, S_BONUS2D),
    # S_BONUS2D
    (SPR_BON2, 3, 3, None, S_BONUS2E),
    # S_BONUS2E
    (SPR_BON2, 2, 3, None, S_BONUS2F),
    # S_BONUS2F
    (SPR_BON2, 1, 3, None, S_BONUS2A),

    # S_BKEY1
    (SPR_BKEY, 0, 5, None, S_BKEY2),
    # S_BKEY2
    (SPR_BKEY, 32768, 5, None, S_BKEY1),
    # S_RKEY1
    (SPR_RKEY, 0, 5, None, S_RKEY2),
    # S_RKEY2
    (SPR_RKEY, 32768, 5, None, S_RKEY1),
    # S_YKEY1
    (SPR_YKEY, 0, 5, None, S_YKEY2),
    # S_YKEY2
    (SPR_YKEY, 32768, 5, None, S_YKEY1),
    # S_YSKULL1
    (SPR_YSKU, 0, 5, None, S_YSKULL2),
    # S_YSKULL2
    (SPR_YSKU, 32768, 5, None, S_YSKULL1),
    # S_RSKULL1
    (SPR_RSKU, 0, 5, None, S_RSKULL2),
    # S_RSKULL2
    (SPR_RSKU, 32768, 5, None, S_RSKULL1),
    # S_BSKULL1
    (SPR_BSKU, 0, 5, None, S_BSKULL2),
    # S_BSKULL2
    (SPR_BSKU, 32768, 5, None, S_BSKULL1),

    # S_ARTIFACT1A
    (SPR_ART1, 32768, 4, None, S_ARTIFACT1B),
    # S_ARTIFACT1B
    (SPR_ART1, 32769, 4, None, S_ARTIFACT1C),
    # S_ARTIFACT1C
    (SPR_ART1, 32770, 4, None, S_ARTIFACT1D),
    # S_ARTIFACT1D
    (SPR_ART1, 32771, 4, None, S_ARTIFACT1E),
    # S_ARTIFACT1E
    (SPR_ART1, 32772, 4, None, S_ARTIFACT1F),
    # S_ARTIFACT1F
    (SPR_ART1, 32771, 4, None, S_ARTIFACT1G),
    # S_ARTIFACT1G
    (SPR_ART1, 32770, 4, None, S_ARTIFACT1H),
    # S_ARTIFACT1H
    (SPR_ART1, 32769, 4, None, S_ARTIFACT1A),
    # S_ARTIFACT2A
    (SPR_ART2, 32768, 4, None, S_ARTIFACT2B),
    # S_ARTIFACT2B
    (SPR_ART2, 32769, 4, None, S_ARTIFACT2C),
    # S_ARTIFACT2C
    (SPR_ART2, 32770, 4, None, S_ARTIFACT2D),
    # S_ARTIFACT2D
    (SPR_ART2, 32771, 4, None, S_ARTIFACT2E),
    # S_ARTIFACT2E
    (SPR_ART2, 32772, 4, None, S_ARTIFACT2F),
    # S_ARTIFACT2F
    (SPR_ART2, 32771, 4, None, S_ARTIFACT2G),
    # S_ARTIFACT2G
    (SPR_ART2, 32770, 4, None, S_ARTIFACT2H),
    # S_ARTIFACT2H
    (SPR_ART2, 32769, 4, None, S_ARTIFACT2A),
    # S_ARTIFACT3A
    (SPR_ART3, 32768, 4, None, S_ARTIFACT3B),
    # S_ARTIFACT3B
    (SPR_ART3, 32769, 4, None, S_ARTIFACT3C),
    # S_ARTIFACT3C
    (SPR_ART3, 32770, 4, None, S_ARTIFACT3D),
    # S_ARTIFACT3D
    (SPR_ART3, 32771, 4, None, S_ARTIFACT3E),
    # S_ARTIFACT3E
    (SPR_ART3, 32772, 4, None, S_ARTIFACT3F),
    # S_ARTIFACT3F
    (SPR_ART3, 32771, 4, None, S_ARTIFACT3G),
    # S_ARTIFACT3G
    (SPR_ART3, 32770, 4, None, S_ARTIFACT3H),
    # S_ARTIFACT3H
    (SPR_ART3, 32769, 4, None, S_ARTIFACT3A),

    # S_STIM
    (SPR_STIM, 0, -1, None, S_NULL),
    # S_MEDI
    (SPR_MEDI, 0, -1, None, S_NULL),

    # S_SOUL1
    (SPR_SOUL, 32768, 6, None, S_SOUL2),
    # S_SOUL2
    (SPR_SOUL, 32769, 6, None, S_SOUL3),
    # S_SOUL3
    (SPR_SOUL, 32770, 6, None, S_SOUL4),
    # S_SOUL4
    (SPR_SOUL, 32771, 6, None, S_SOUL5),
    # S_SOUL5
    (SPR_SOUL, 32770, 6, None, S_SOUL6),
    # S_SOUL6
    (SPR_SOUL, 32769, 6, None, S_SOUL1),

    # S_PINV1
    (SPR_PINV, 32768, 6, None, S_PINV2),
    # S_PINV2
    (SPR_PINV, 32769, 6, None, S_PINV3),
    # S_PINV3
    (SPR_PINV, 32770, 6, None, S_PINV4),
    # S_PINV4
    (SPR_PINV, 32771, 6, None, S_PINV5),
    # S_PINV5
    (SPR_PINV, 32770, 6, None, S_PINV6),
    # S_PINV6
    (SPR_PINV, 32769, 6, None, S_PINV1),
    # S_PSTR
    (SPR_PSTR, 32768, -1, None, S_NULL),
    # S_PINS1
    (SPR_PINS, 32768, 2, None, S_PINS2),
    # S_PINS2
    (SPR_PINS, 32769, 3, None, S_PINS3),
    # S_PINS3
    (SPR_PINS, 32770, 2, None, S_PINS4),
    # S_PINS4
    (SPR_PINS, 32771, 1, None, S_PINS5),
    # S_PINS5
    (SPR_PINS, 32769, 2, None, S_PINS6),
    # S_PINS6
    (SPR_PINS, 32770, 1, None, S_PINS1),
    # S_SUIT1
    (SPR_SUIT, 32768, 4, None, S_SUIT2),
    # S_SUIT2
    (SPR_SUIT, 32769, 4, None, S_SUIT1),
    # S_PMAP1
    (SPR_PMAP, 32768, 5, None, S_PMAP2),
    # S_PMAP2
    (SPR_PMAP, 32769, 5, None, S_PMAP3),
    # S_PMAP3
    (SPR_PMAP, 32770, 5, None, S_PMAP4),
    # S_PMAP4
    (SPR_PMAP, 32771, 5, None, S_PMAP1),
    # S_PVIS1
    (SPR_PVIS, 32768, 3, None, S_PVIS2),
    # S_PVIS2
    (SPR_PVIS, 1, 3, None, S_PVIS1),

    # S_MEGA1
    (SPR_MEGA, 32768, 4, None, S_MEGA2),
    # S_MEGA2
    (SPR_MEGA, 32769, 4, None, S_MEGA3),
    # S_MEGA3
    (SPR_MEGA, 32770, 4, None, S_MEGA4),
    # S_MEGA4
    (SPR_MEGA, 32771, 4, None, S_MEGA5),
    # S_MEGA5
    (SPR_MEGA, 32770, 4, None, S_MEGA6),
    # S_MEGA6
    (SPR_MEGA, 32769, 4, None, S_MEGA1),

    # S_CLIP
    (SPR_CLIP, 0, -1, None, S_NULL),
    # S_AMMO
    (SPR_AMMO, 0, -1, None, S_NULL),
    # S_RCKT
    (SPR_RCKT, 0, -1, None, S_NULL),
    # S_BROK
    (SPR_BROK, 0, -1, None, S_NULL),
    # S_CELL
    (SPR_CELL, 0, -1, None, S_NULL),
    # S_CELP
    (SPR_CELP, 0, -1, None, S_NULL),
    # S_SHEL
    (SPR_SHEL, 0, -1, None, S_NULL),
    # S_SBOX
    (SPR_SBOX, 0, -1, None, S_NULL),
    # S_BPAK
    (SPR_BPAK, 0, -1, None, S_NULL),

    # S_BFUG
    (SPR_BFUG, 0, -1, None, S_NULL),
    # S_CSAW
    (SPR_CSAW, 0, -1, None, S_NULL),
    # S_MGUN
    (SPR_MGUN, 0, -1, None, S_NULL),
    # S_LAUN
    (SPR_LAUN, 0, -1, None, S_NULL),
    # S_PLSM
    (SPR_PLSM, 0, -1, None, S_NULL),
    # S_SHOT
    (SPR_SHOT, 0, -1, None, S_NULL),
    # S_SHOT2
    (SPR_SGN2, 0, -1, None, S_NULL),
    # S_LSRG
    (SPR_LSRG, 0, -1, None, S_NULL),

    # S_PROP_FIRE1
    (SPR_FIRE, 0, 3, None, S_PROP_FIRE2),
    # S_PROP_FIRE2
    (SPR_FIRE, 1, 3, None, S_PROP_FIRE3),
    # S_PROP_FIRE3
    (SPR_FIRE, 2, 3, None, S_PROP_FIRE4),
    # S_PROP_FIRE4
    (SPR_FIRE, 3, 3, None, S_PROP_FIRE5),
    # S_PROP_FIRE5
    (SPR_FIRE, 4, 3, None, S_PROP_FIRE1),

    # S_CANDLE1
    (SPR_CAND, 0, 2, None, S_CANDLE2),
    # S_CANDLE2
    (SPR_CAND, 1, 2, None, S_CANDLE1),

    # S_BARREL
    (SPR_BAR1, 0, -1, None, S_NULL),
    # S_BARREL_DIE1
    (SPR_BAR1, 1, 5, None, S_BARREL_DIE2),
    # S_BARREL_DIE2
    (SPR_BAR1, 2, 5, None, S_BARREL_DIE3),
    # S_BARREL_DIE3
    (SPR_BAR1, 3, 5, None, S_BARREL_DIE4),
    # S_BARREL_DIE4
    (SPR_BAR1, 32772, 5, A_BarrelExplode, S_NULL),

    # S_EXP1A
    (SPR_MISL, 32769, 6, None, S_EXP1B),
    # S_EXP1B
    (SPR_MISL, 32770, 5, None, S_EXP1C),
    # S_EXP1C
    (SPR_MISL, 32771, 2, None, S_EXP1D),
    # S_EXP1D
    (SPR_MISL, 32772, 2, None, S_EXP1E),
    # S_EXP1E
    (SPR_MISL, 32773, 2, None, S_NULL),
    # S_EXP2A
    (SPR_MISL, 32769, 2, None, S_EXP2B),
    # S_EXP2B
    (SPR_MISL, 32770, 2, None, S_EXP2C),
    # S_EXP2C
    (SPR_MISL, 32771, 2, None, S_EXP2D),
    # S_EXP2D
    (SPR_MISL, 32772, 2, None, S_EXP2E),
    # S_EXP2E
    (SPR_MISL, 32773, 2, None, S_NULL),

    # S_LAMP1
    (SPR_LMP1, 0, -1, None, S_NULL),
    # S_LAMP2
    (SPR_LMP2, 0, -1, None, S_NULL),

    # S_BTORCH1
    (SPR_A031, 0, 4, None, S_BTORCH2),
    # S_BTORCH2
    (SPR_A031, 1, 4, None, S_BTORCH3),
    # S_BTORCH3
    (SPR_A031, 2, 4, None, S_BTORCH4),
    # S_BTORCH4
    (SPR_A031, 3, 4, None, S_BTORCH5),
    # S_BTORCH5
    (SPR_A031, 4, 4, None, S_BTORCH1),
    # S_YTORCH1
    (SPR_A030, 0, 4, None, S_YTORCH2),
    # S_YTORCH2
    (SPR_A030, 1, 4, None, S_YTORCH3),
    # S_YTORCH3
    (SPR_A030, 2, 4, None, S_YTORCH4),
    # S_YTORCH4
    (SPR_A030, 3, 4, None, S_YTORCH5),
    # S_YTORCH5
    (SPR_A030, 4, 4, None, S_YTORCH1),
    # S_RTORCH1
    (SPR_A032, 0, 4, None, S_RTORCH2),
    # S_RTORCH2
    (SPR_A032, 1, 4, None, S_RTORCH3),
    # S_RTORCH3
    (SPR_A032, 2, 4, None, S_RTORCH4),
    # S_RTORCH4
    (SPR_A032, 3, 4, None, S_RTORCH5),
    # S_RTORCH5
    (SPR_A032, 4, 4, None, S_RTORCH1),
    # S_POLELONG
    (SPR_A033, 0, -1, None, S_NULL),
    # S_POLESHORT
    (SPR_A034, 0, -1, None, S_NULL),

    # S_BFLAME1
    (SPR_BFLM, 32768, 4, None, S_BFLAME2),
    # S_BFLAME2
    (SPR_BFLM, 32769, 4, None, S_BFLAME3),
    # S_BFLAME3
    (SPR_BFLM, 32770, 4, None, S_BFLAME4),
    # S_BFLAME4
    (SPR_BFLM, 32771, 4, None, S_BFLAME5),
    # S_BFLAME5
    (SPR_BFLM, 32772, 4, None, S_BFLAME1),
    # S_RFLAME1
    (SPR_RFLM, 32768, 4, None, S_RFLAME2),
    # S_RFLAME2
    (SPR_RFLM, 32769, 4, None, S_RFLAME3),
    # S_RFLAME3
    (SPR_RFLM, 32770, 4, None, S_RFLAME4),
    # S_RFLAME4
    (SPR_RFLM, 32771, 4, None, S_RFLAME5),
    # S_RFLAME5
    (SPR_RFLM, 32772, 4, None, S_RFLAME1),
    # S_YFLAME1
    (SPR_YFLM, 32768, 4, None, S_YFLAME2),
    # S_YFLAME2
    (SPR_YFLM, 32769, 4, None, S_YFLAME3),
    # S_YFLAME3
    (SPR_YFLM, 32770, 4, None, S_YFLAME4),
    # S_YFLAME4
    (SPR_YFLM, 32771, 4, None, S_YFLAME5),
    # S_YFLAME5
    (SPR_YFLM, 32772, 4, None, S_YFLAME1),

    # S_GORE1
    (SPR_A006, 0, -1, None, S_NULL),
    # S_GORE2
    (SPR_A021, 0, -1, None, S_NULL),
    # S_GORE3
    (SPR_A003, 0, -1, None, S_NULL),
    # S_GORE4
    (SPR_A020, 0, -1, None, S_NULL),
    # S_GORETWITCH1
    (SPR_A014, 0, 6, None, S_GORETWITCH2),
    # S_GORETWITCH2
    (SPR_A014, 1, 6, None, S_GORETWITCH1),
    # S_GORE5
    (SPR_A016, 0, -1, None, S_NULL),
    # S_GORE6
    (SPR_A027, 0, -1, None, S_NULL),
    # S_GORE7
    (SPR_A008, 0, -1, None, S_NULL),
    # S_GORE8
    (SPR_A007, 0, -1, None, S_NULL),
    # S_GOREHOOK1
    (SPR_A015, 0, -1, None, S_NULL),
    # S_GORECAGE
    (SPR_A001, 0, -1, None, S_NULL),
    # S_GOREHOOK2
    (SPR_A012, 0, -1, None, S_NULL),
    # S_GOREHOOK3
    (SPR_A010, 0, -1, None, S_NULL),
    # S_GOREMACE1
    (SPR_A018, 0, -1, None, S_NULL),
    # S_GOREHEAD1
    (SPR_A017, 0, -1, None, S_NULL),
    # S_GOREHEAD2
    (SPR_A026, 0, -1, None, S_NULL),
    # S_GORE9
    (SPR_A022, 0, -1, None, S_NULL),
    # S_GARGOYLE1
    (SPR_A028, 0, -1, None, S_NULL),
    # S_GARGOYLE2
    (SPR_A029, 0, -1, None, S_NULL),
    # S_TECHLAMP1
    (SPR_A035, 0, -1, None, S_NULL),
    # S_TECHLAMP2
    (SPR_A036, 0, -1, None, S_NULL),
    # S_TREE3
    (SPR_TRE3, 0, -1, None, S_NULL),
    # S_TREE2
    (SPR_TRE2, 0, -1, None, S_NULL),
    # S_TREE1
    (SPR_TRE1, 0, -1, None, S_NULL),
    # S_GORE10
    (SPR_A013, 0, -1, None, S_NULL),
    # S_GOREMACE
    (SPR_A019, 0, -1, None, S_NULL),
    # S_GORE11
    (SPR_A004, 0, -1, None, S_NULL),
    # S_GOREHEAD3
    (SPR_A005, 0, -1, None, S_NULL),
    # S_GORE12
    (SPR_A023, 0, -1, None, S_NULL),

    # S_SAWA
    (SPR_SAWG, 0, 4, A_ChainSawReady, S_SAWB),
    # S_SAWB
    (SPR_SAWG, 1, 4, A_WeaponReady, S_SAWA),
    # S_SAWDOWN
    (SPR_SAWG, 1, 1, A_Lower, S_SAWDOWN),
    # S_SAWUP
    (SPR_SAWG, 1, 1, A_Raise, S_SAWUP),
    # S_SAW1
    (SPR_SAWG, 2, 2, A_Saw, S_SAW2),
    # S_SAW2
    (SPR_SAWG, 3, 2, A_Saw, S_SAW3),
    # S_SAW3
    (SPR_SAWG, 3, 0, A_ReFire, S_SAWA),

    # S_PUNCH
    (SPR_PUNG, 0, 1, A_WeaponReady, S_PUNCH),
    # S_PUNCHDOWN
    (SPR_PUNG, 0, 1, A_Lower, S_PUNCHDOWN),
    # S_PUNCHUP
    (SPR_PUNG, 0, 1, A_Raise, S_PUNCHUP),
    # S_PUNCH1
    (SPR_PUNG, 1, 4, None, S_PUNCH2),
    # S_PUNCH2
    (SPR_PUNG, 2, 4, A_Punch, S_PUNCH3),
    # S_PUNCH3
    (SPR_PUNG, 3, 5, None, S_PUNCH4),
    # S_PUNCH4
    (SPR_PUNG, 2, 4, None, S_PUNCH5),
    # S_PUNCH5
    (SPR_PUNG, 1, 5, A_ReFire, S_PUNCH),

    # S_PISTOL
    (SPR_PISG, 0, 1, A_WeaponReady, S_PISTOL),
    # S_PISTOLDOWN
    (SPR_PISG, 0, 1, A_Lower, S_PISTOLDOWN),
    # S_PISTOLUP
    (SPR_PISG, 0, 1, A_Raise, S_PISTOLUP),
    # S_PISTOL1
    (SPR_PISG, 0, 2, None, S_PISTOL2),
    # S_PISTOL2
    (SPR_PISG, 1, 1, A_FirePistol, S_PISTOL3),
    # S_PISTOL3
    (SPR_PISG, 2, 5, None, S_PISTOL4),
    # S_PISTOL4
    (SPR_PISG, 1, 5, None, S_PISTOL5),
    # S_PISTOL5
    (SPR_PISG, 0, 1, A_ReFire, S_PISTOL),
    # S_PISTOLFLASH
    (SPR_PISG, 32771, 3, None, S_NULL),

    # S_SGUN
    (SPR_SHT1, 0, 1, A_WeaponReady, S_SGUN),
    # S_SGUNDOWN
    (SPR_SHT1, 0, 1, A_Lower, S_SGUNDOWN),
    # S_SGUNUP
    (SPR_SHT1, 0, 1, A_Raise, S_SGUNUP),
    # S_SGUN1
    (SPR_SHT1, 0, 2, None, S_SGUN2),
    # S_SGUN2
    (SPR_SHT1, 0, 4, A_FireShotgun, S_SGUN3),
    # S_SGUN3
    (SPR_SHT1, 1, 18, None, S_SGUN4),
    # S_SGUN4
    (SPR_SHT1, 2, 5, None, S_SGUN5),
    # S_SGUN5
    (SPR_SHT1, 0, 3, None, S_SGUN6),
    # S_SGUN6
    (SPR_SHT1, 0, 7, A_ReFire, S_SGUN),
    # S_SGUNFLASH
    (SPR_SHT1, 32771, 4, None, S_NULL),

    # S_SSG
    (SPR_SHT2, 0, 1, A_WeaponReady, S_SSG),
    # S_SSGDOWN
    (SPR_SHT2, 0, 1, A_Lower, S_SSGDOWN),
    # S_SSGUP
    (SPR_SHT2, 0, 1, A_Raise, S_SSGUP),
    # S_SSG1
    (SPR_SHT2, 0, 1, None, S_SSG2),
    # S_SSG2
    (SPR_SHT2, 0, 4, A_FireShotgun2, S_SSG3),
    # S_SSG3
    (SPR_SHT2, 1, 7, None, S_SSG4),
    # S_SSG4
    (SPR_SHT2, 1, 5, A_CheckReload, S_SSG5),
    # S_SSG5
    (SPR_SHT2, 1, 5, None, S_SSG6),
    # S_SSG6
    (SPR_SHT2, 1, 5, None, S_SSG7),
    # S_SSG7
    (SPR_SHT2, 1, 5, None, S_SSG8),
    # S_SSG8
    (SPR_SHT2, 1, 5, A_LoadShotgun2, S_SSG9),
    # S_SSG9
    (SPR_SHT2, 2, 4, A_CloseShotgun2, S_SSG10),
    # S_SSG10
    (SPR_SHT2, 0, 5, A_ReFire, S_SSG),
    # S_SSGFLASH
    (SPR_SHT2, 32771, 4, None, S_NULL),

    # S_CHAING
    (SPR_CHGG, 0, 1, A_WeaponReady, S_CHAING),
    # S_CHAINGDOWN
    (SPR_CHGG, 0, 1, A_Lower, S_CHAINGDOWN),
    # S_CHAINGUP
    (SPR_CHGG, 0, 1, A_Raise, S_CHAINGUP),
    # S_CHAING1
    (SPR_CHGG, 0, 3, A_FireCGun, S_CHAING2),
    # S_CHAING2
    (SPR_CHGG, 1, 3, A_FireCGun, S_CHAING3),
    # S_CHAING3
    (SPR_CHGG, 1, 0, A_ReFire, S_CHAING),
    # S_CHAINGLIGHT1
    (SPR_CHGG, 32771, 3, None, S_NULL),
    # S_CHAINGLIGHT2
    (SPR_CHGG, 32770, 3, None, S_NULL),

    # S_ROCKETL
    (SPR_ROCK, 0, 1, A_WeaponReady, S_ROCKETL),
    # S_ROCKETLDOWN
    (SPR_ROCK, 0, 1, A_Lower, S_ROCKETLDOWN),
    # S_ROCKETLUP
    (SPR_ROCK, 0, 1, A_Raise, S_ROCKETLUP),
    # S_ROCKETL1
    (SPR_ROCK, 1, 8, A_GunFlash, S_ROCKETL2),
    # S_ROCKETL2
    (SPR_ROCK, 1, 10, A_FireMissile, S_ROCKETL3),
    # S_ROCKETL3
    (SPR_ROCK, 1, 0, A_ReFire, S_ROCKETL),
    # S_ROCKETLLIGHT1
    (SPR_ROCK, 32770, 3, None, S_ROCKETLLIGHT2),
    # S_ROCKETLLIGHT2
    (SPR_ROCK, 32771, 4, None, S_ROCKETLLIGHT3),
    # S_ROCKETLLIGHT3
    (SPR_ROCK, 32772, 4, None, S_ROCKETLLIGHT4),
    # S_ROCKETLLIGHT4
    (SPR_ROCK, 32773, 4, None, S_NULL),

    # S_PLASMAG
    (SPR_PLAS, 0, 1, A_WeaponReady, S_PLASMAG),
    # S_PLASMAGDOWN
    (SPR_PLAS, 0, 1, A_Lower, S_PLASMAGDOWN),
    # S_PLASMAGUP1
    (SPR_PLAS, 0, 0, A_PlasmaAnimate, S_PLASMAGUP2),
    # S_PLASMAGUP2
    (SPR_PLAS, 0, 1, A_Raise, S_PLASMAGUP2),
    # S_PLASMAG1
    (SPR_PLAS, 32772, 2, A_FirePlasma, S_PLASMAG2),
    # S_PLASMAG2
    (SPR_PLAS, 0, 2, A_PlasmaAnimate, S_PLASMAG3),
    # S_PLASMAG3
    (SPR_PLAS, 0, 1, A_ReFire, S_PLASMAG),
    # S_PLASMAGANIM1
    (SPR_PLAS, 1, 2, None, S_PLASMAGANIM2),
    # S_PLASMAGANIM2
    (SPR_PLAS, 2, 2, None, S_PLASMAGANIM3),
    # S_PLASMAGANIM3
    (SPR_PLAS, 3, 2, None, S_PLASMAGANIM1),

    # S_BFG
    (SPR_BFGG, 0, 1, A_WeaponReady, S_BFG),
    # S_BFGDOWN
    (SPR_BFGG, 0, 1, A_Lower, S_BFGDOWN),
    # S_BFGUP
    (SPR_BFGG, 0, 1, A_Raise, S_BFGUP),
    # S_BFG1
    (SPR_BFGG, 0, 20, A_BFGsound, S_BFG2),
    # S_BFG2
    (SPR_BFGG, 1, 10, A_GunFlash, S_BFG3),
    # S_BFG3
    (SPR_BFGG, 1, 10, A_FireBFG, S_BFG4),
    # S_BFG4
    (SPR_BFGG, 1, 20, A_ReFire, S_BFG),
    # S_BFGLIGHT1
    (SPR_BFGG, 32770, 8, None, S_BFGLIGHT2),
    # S_BFGLIGHT2
    (SPR_BFGG, 32771, 5, None, S_BFGLIGHT3),
    # S_BFGLIGHT3
    (SPR_BFGG, 32772, 3, None, S_NULL),

    # S_LASERG
    (SPR_LASR, 0, 2, A_WeaponReady, S_LASERG),
    # S_LASERGDOWN
    (SPR_LASR, 0, 1, A_Lower, S_LASERGDOWN),
    # S_LASERGUP
    (SPR_LASR, 0, 1, A_Raise, S_LASERGUP),
    # S_LASERG1
    (SPR_LASR, 0, 8, A_FireLaser, S_LASERG2),
    # S_LASERG2
    (SPR_LASR, 0, 3, A_ReFire, S_LASERG),
    # S_LASERGLIGHT
    (SPR_LASR, 32769, 3, None, S_NULL),

    (SPR_S003, 0, 4, None, S_BWTORCH2),  # S_BWTORCH1
    (SPR_S003, 1, 4, None, S_BWTORCH3),  # S_BWTORCH2
    (SPR_S003, 2, 4, None, S_BWTORCH4),  # S_BWTORCH3
    (SPR_S003, 3, 4, None, S_BWTORCH1),  # S_BWTORCH4
    (SPR_S039, 0, 4, None, S_YWTORCH2),  # S_YWTORCH1
    (SPR_S039, 1, 4, None, S_YWTORCH3),  # S_YWTORCH2
    (SPR_S039, 2, 4, None, S_YWTORCH4),  # S_YWTORCH3
    (SPR_S039, 3, 4, None, S_YWTORCH1),  # S_YWTORCH4
    (SPR_S025, 0, 4, None, S_RWTORCH2),  # S_RWTORCH1
    (SPR_S025, 1, 4, None, S_RWTORCH3),  # S_RWTORCH2
    (SPR_S025, 2, 4, None, S_RWTORCH4),  # S_RWTORCH3
    (SPR_S025, 3, 4, None, S_RWTORCH1),  # S_RWTORCH4
    (SPR_S033, 32768, 4, None, S_BFLM2),  # S_BFLM1
    (SPR_S033, 32769, 4, None, S_BFLM3),  # S_BFLM2
    (SPR_S033, 32770, 4, None, S_BFLM4),  # S_BFLM3
    (SPR_S033, 32771, 4, None, S_BFLM1),  # S_BFLM4
    (SPR_S034, 32768, 4, None, S_RFLM2),  # S_RFLM1
    (SPR_S034, 32769, 4, None, S_RFLM3),  # S_RFLM2
    (SPR_S034, 32770, 4, None, S_RFLM4),  # S_RFLM3
    (SPR_S034, 32771, 4, None, S_RFLM1),  # S_RFLM4
    (SPR_S035, 32768, 4, None, S_YFLM2),  # S_YFLM1
    (SPR_S035, 32769, 4, None, S_YFLM3),  # S_YFLM2
    (SPR_S035, 32770, 4, None, S_YFLM4),  # S_YFLM3
    (SPR_S035, 32771, 4, None, S_YFLM1),  # S_YFLM4
    (SPR_S005, 0, -1, None, S_NULL),  # S_MISC5
    (SPR_S006, 0, -1, None, S_NULL),  # S_MISC6
    (SPR_S007, 0, -1, None, S_NULL),  # S_MISC7
    (SPR_S008, 0, -1, None, S_NULL),  # S_MISC8_1
    (SPR_S009, 0, -1, None, S_NULL),  # S_MISC9_1
    (SPR_S010, 0, -1, None, S_NULL),  # S_MISC10
    (SPR_S011, 0, 6, None, S_MISC11_2),  # S_MISC11_1
    (SPR_S011, 1, 6, None, S_MISC11_1),  # S_MISC11_2
    (SPR_S012, 0, 6, None, S_MISC12_2),  # S_MISC12_1
    (SPR_S012, 1, 6, None, S_MISC12_1),  # S_MISC12_2
    (SPR_S013, 0, 6, None, S_MISC13_2),  # S_MISC13_1
    (SPR_S013, 1, 6, None, S_MISC13_1),  # S_MISC13_2
    (SPR_S014, 0, -1, None, S_NULL),  # S_MISC14
    (SPR_S017, 0, -1, None, S_NULL),  # S_MISC17
    (SPR_S018, 0, -1, None, S_NULL),  # S_MISC18
    (SPR_S019, 0, -1, None, S_NULL),  # S_MISC19
    (SPR_S020, 0, -1, None, S_NULL),  # S_MISC20
    (SPR_S021, 0, 4, None, S_MISC21_2),  # S_MISC21_1
    (SPR_S021, 1, 4, None, S_MISC21_1),  # S_MISC21_2
    (SPR_S022, 0, -1, None, S_NULL),  # S_MISC22
    (SPR_S023, 0, -1, None, S_NULL),  # S_MISC23
    (SPR_S024, 0, -1, None, S_NULL),  # S_MISC24
    (SPR_S028, 0, -1, None, S_NULL),  # S_MISC28
    (SPR_S029, 0, -1, None, S_NULL),  # S_MISC29
    (SPR_S031, 0, -1, None, S_NULL),  # S_MISC31
    (SPR_S032, 0, -1, None, S_NULL),  # S_MISC32
    (SPR_S027, 0, -1, None, S_NULL),  # S_MISC27
    (SPR_S036, 0, -1, None, S_NULL),  # S_MISC36
    (SPR_S037, 0, -1, None, S_NULL),  # S_MISC37
    (SPR_S038, 0, -1, None, S_NULL),  # S_MISC38
    (SPR_S040, 0, -1, None, S_NULL),  # S_MISC45
    (SPR_S041, 0, -1, None, S_NULL),  # S_MISC41
    (SPR_S026, 0, -1, None, S_NULL),  # S_MISC26
    (SPR_S027, 0, -1, None, S_NULL),  # S_MISC46
    (SPR_S002, 32768, 4, None, S_MISC47_2),  # S_MISC47_1
    (SPR_S002, 32769, 4, None, S_MISC47_3),  # S_MISC47_2
    (SPR_S002, 32770, 4, None, S_MISC47_4),  # S_MISC47_3
    (SPR_S002, 32771, 4, None, S_MISC47_1),  # S_MISC47_4
    (SPR_S030, 32768, 4, None, S_MISC30_2),  # S_MISC30_1
    (SPR_S030, 32769, 4, None, S_MISC30_3),  # S_MISC30_2
    (SPR_S030, 32770, 4, None, S_MISC30_4),  # S_MISC30_3
    (SPR_S030, 32771, 4, None, S_MISC30_1),  # S_MISC30_4

    # S_CPOS_STND
    (SPR_CPOS, 0, 10, A_Look, S_CPOS_STND2),
    # S_CPOS_STND2
    (SPR_CPOS, 1, 10, A_Look, S_CPOS_STND),
    # S_CPOS_RUN1
    (SPR_CPOS, 0, 3, A_Chase, S_CPOS_RUN2),
    # S_CPOS_RUN2
    (SPR_CPOS, 0, 3, A_Chase, S_CPOS_RUN3),
    # S_CPOS_RUN3
    (SPR_CPOS, 1, 3, A_Chase, S_CPOS_RUN4),
    # S_CPOS_RUN4
    (SPR_CPOS, 1, 3, A_Chase, S_CPOS_RUN5),
    # S_CPOS_RUN5
    (SPR_CPOS, 2, 3, A_Chase, S_CPOS_RUN6),
    # S_CPOS_RUN6
    (SPR_CPOS, 2, 3, A_Chase, S_CPOS_RUN7),
    # S_CPOS_RUN7
    (SPR_CPOS, 3, 3, A_Chase, S_CPOS_RUN8),
    # S_CPOS_RUN8
    (SPR_CPOS, 3, 3, A_Chase, S_CPOS_RUN1),
    # S_CPOS_ATK1
    (SPR_CPOS, 4, 10, A_FaceTarget, S_CPOS_ATK2),
    # S_CPOS_ATK2
    (SPR_CPOS, 32773, 4, A_CPosAttack, S_CPOS_ATK3),
    # S_CPOS_ATK3
    (SPR_CPOS, 32772, 4, A_CPosAttack, S_CPOS_ATK4),
    # S_CPOS_ATK4
    (SPR_CPOS, 5, 1, A_CPosRefire, S_CPOS_ATK2),
    # S_CPOS_PAIN
    (SPR_CPOS, 6, 3, None, S_CPOS_PAIN2),
    # S_CPOS_PAIN2
    (SPR_CPOS, 6, 3, A_Pain, S_CPOS_RUN1),
    # S_CPOS_DIE1
    (SPR_CPOS, 7, 5, None, S_CPOS_DIE2),
    # S_CPOS_DIE2
    (SPR_CPOS, 8, 5, A_Scream, S_CPOS_DIE3),
    # S_CPOS_DIE3
    (SPR_CPOS, 9, 5, A_Fall, S_CPOS_DIE4),
    # S_CPOS_DIE4
    (SPR_CPOS, 10, 5, None, S_CPOS_DIE5),
    # S_CPOS_DIE5
    (SPR_CPOS, 11, 5, None, S_CPOS_DIE6),
    # S_CPOS_DIE6
    (SPR_CPOS, 12, 5, A_OnDeathTrigger, S_CPOS_DIE7),
    # S_CPOS_DIE7
    (SPR_CPOS, 13, -1, None, S_NULL),
    # S_CPOS_XDIE1
    (SPR_CPOS, 14, 5, None, S_CPOS_XDIE2),
    # S_CPOS_XDIE2
    (SPR_CPOS, 15, 5, A_XScream, S_CPOS_XDIE3),
    # S_CPOS_XDIE3
    (SPR_CPOS, 16, 5, A_Fall, S_CPOS_XDIE4),
    # S_CPOS_XDIE4
    (SPR_CPOS, 17, 5, None, S_CPOS_XDIE5),
    # S_CPOS_XDIE5
    (SPR_CPOS, 18, 5, A_OnDeathTrigger, S_CPOS_XDIE6),
    # S_CPOS_XDIE6
    (SPR_CPOS, 19, -1, None, S_NULL),

    # S_SKEL_STND
    (SPR_SKEL, 0, 10, A_Look, S_SKEL_STND2),
    # S_SKEL_STND2
    (SPR_SKEL, 1, 10, A_Look, S_SKEL_STND),
    # S_SKEL_RUN1
    (SPR_SKEL, 0, 2, A_Chase, S_SKEL_RUN2),
    # S_SKEL_RUN2
    (SPR_SKEL, 0, 2, A_Chase, S_SKEL_RUN3),
    # S_SKEL_RUN3
    (SPR_SKEL, 1, 2, A_Chase, S_SKEL_RUN4),
    # S_SKEL_RUN4
    (SPR_SKEL, 1, 2, A_Chase, S_SKEL_RUN5),
    # S_SKEL_RUN5
    (SPR_SKEL, 2, 2, A_Chase, S_SKEL_RUN6),
    # S_SKEL_RUN6
    (SPR_SKEL, 2, 2, A_Chase, S_SKEL_RUN7),
    # S_SKEL_RUN7
    (SPR_SKEL, 3, 2, A_Chase, S_SKEL_RUN8),
    # S_SKEL_RUN8
    (SPR_SKEL, 3, 2, A_Chase, S_SKEL_RUN9),
    # S_SKEL_RUN9
    (SPR_SKEL, 4, 2, A_Chase, S_SKEL_RUN10),
    # S_SKEL_RUN10
    (SPR_SKEL, 4, 2, A_Chase, S_SKEL_RUN11),
    # S_SKEL_RUN11
    (SPR_SKEL, 5, 2, A_Chase, S_SKEL_RUN12),
    # S_SKEL_RUN12
    (SPR_SKEL, 5, 2, A_Chase, S_SKEL_RUN1),
    # S_SKEL_FIST1
    (SPR_SKEL, 6, 0, A_FaceTarget, S_SKEL_FIST2),
    # S_SKEL_FIST2
    (SPR_SKEL, 6, 6, A_SkelWhoosh, S_SKEL_FIST3),
    # S_SKEL_FIST3
    (SPR_SKEL, 7, 6, A_FaceTarget, S_SKEL_FIST4),
    # S_SKEL_FIST4
    (SPR_SKEL, 8, 6, A_SkelFist, S_SKEL_RUN1),
    # S_SKEL_MISS1
    (SPR_SKEL, 32777, 0, A_FaceTarget, S_SKEL_MISS2),
    # S_SKEL_MISS2
    (SPR_SKEL, 32777, 10, A_FaceTarget, S_SKEL_MISS3),
    # S_SKEL_MISS3
    (SPR_SKEL, 10, 10, A_SkelAttack, S_SKEL_MISS4),
    # S_SKEL_MISS4
    (SPR_SKEL, 10, 10, A_FaceTarget, S_SKEL_RUN1),
    # S_SKEL_PAIN
    (SPR_SKEL, 11, 4, None, S_SKEL_PAIN2),
    # S_SKEL_PAIN2
    (SPR_SKEL, 11, 4, A_Pain, S_SKEL_RUN1),
    # S_SKEL_DIE1
    (SPR_SKEL, 11, 6, None, S_SKEL_DIE2),
    # S_SKEL_DIE2
    (SPR_SKEL, 12, 6, None, S_SKEL_DIE3),
    # S_SKEL_DIE3
    (SPR_SKEL, 13, 6, A_Scream, S_SKEL_DIE4),
    # S_SKEL_DIE4
    (SPR_SKEL, 14, 6, A_Fall, S_SKEL_DIE5),
    # S_SKEL_DIE5
    (SPR_SKEL, 15, 6, A_OnDeathTrigger, S_SKEL_DIE6),
    # S_SKEL_DIE6
    (SPR_SKEL, 16, -1, None, S_NULL),

    # S_ARCR1
    (SPR_ARCR, 32768, 3, A_Tracer, S_ARCR2),
    # S_ARCR2
    (SPR_ARCR, 32769, 3, A_Tracer, S_ARCR1),

    # S_POW1_DIE1
    (SPR_POW1, 32768, 4, A_FadeAlpha, S_POW1_DIE2),
    # S_POW1_DIE2
    (SPR_POW1, 32769, 3, A_FadeAlpha, S_POW1_DIE3),
    # S_POW1_DIE3
    (SPR_POW1, 32770, 2, A_FadeAlpha, S_POW1_DIE4),
    # S_POW1_DIE4
    (SPR_POW1, 32771, 2, None, S_POW1_DIE5),
    # S_POW1_DIE5
    (SPR_POW1, 32772, 2, None, S_POW1_DIE6),
    # S_POW1_DIE6
    (SPR_POW1, 32773, 2, None, S_POW1_DIE7),
    # S_POW1_DIE7
    (SPR_POW1, 32774, 2, None, S_POW1_DIE8),
    # S_POW1_DIE8
    (SPR_POW1, 32775, 2, None, S_NULL),

    # S_SPID_STND
    (SPR_SPID, 0, 10, A_Look, S_SPID_STND2),
    # S_SPID_STND2
    (SPR_SPID, 1, 10, A_Look, S_SPID_STND),
    # S_SPID_RUN1
    (SPR_SPID, 0, 4, A_Metal, S_SPID_RUN2),
    # S_SPID_RUN2
    (SPR_SPID, 0, 4, A_Chase, S_SPID_RUN3),
    # S_SPID_RUN3
    (SPR_SPID, 1, 4, A_Chase, S_SPID_RUN4),
    # S_SPID_RUN4
    (SPR_SPID, 1, 4, A_Chase, S_SPID_RUN5),
    # S_SPID_RUN5
    (SPR_SPID, 2, 4, A_Metal, S_SPID_RUN6),
    # S_SPID_RUN6
    (SPR_SPID, 2, 4, A_Chase, S_SPID_RUN7),
    # S_SPID_RUN7
    (SPR_SPID, 3, 4, A_Chase, S_SPID_RUN8),
    # S_SPID_RUN8
    (SPR_SPID, 3, 4, A_Chase, S_SPID_RUN1),
    # S_SPID_ATK1
    (SPR_SPID, 32768, 20, A_BspiFaceTarget, S_SPID_ATK2),
    # S_SPID_ATK2
    (SPR_SPID, 32772, 2, A_SpidAttack, S_SPID_ATK3),
    # S_SPID_ATK3
    (SPR_SPID, 32773, 2, None, S_SPID_ATK4),
    # S_SPID_ATK4
    (SPR_SPID, 32774, 2, A_SpidAttack, S_SPID_ATK5),
    # S_SPID_ATK5
    (SPR_SPID, 32775, 2, None, S_SPID_ATK6),
    # S_SPID_ATK6
    (SPR_SPID, 32776, 2, A_SpidRefire, S_SPID_ATK2),
    # S_SPID_PAIN
    (SPR_SPID, 9, 4, None, S_SPID_PAIN2),
    # S_SPID_PAIN2
    (SPR_SPID, 10, 4, A_Pain, S_SPID_RUN1),
    # S_SPID_DIE1
    (SPR_SPID, 11, 16, A_Scream, S_SPID_DIE2),
    # S_SPID_DIE2
    (SPR_SPID, 12, 6, A_Fall, S_SPID_DIE3),
    # S_SPID_DIE3
    (SPR_SPID, 13, 6, None, S_SPID_DIE4),
    # S_SPID_DIE4
    (SPR_SPID, 14, 6, None, S_SPID_DIE5),
    # S_SPID_DIE5
    (SPR_SPID, 14, 6, A_OnDeathTrigger, S_SPID_DIE6),
    # S_SPID_DIE6
    (SPR_SPID, 15, -1, None, S_NULL),

    # S_HEAD_STND
    (SPR_TEST, 0, 15, A_Look, S_TEST_STND2),
    # S_HEAD_STND2
    (SPR_TEST, 1, 15, A_Look, S_TEST_STND3),
    # S_HEAD_STND3
    (SPR_TEST, 2, 15, A_Look, S_TEST_STND4),
    # S_HEAD_STND4
    (SPR_TEST, 3, 15, A_Look, S_TEST_STND),
    # S_HEAD_RUN1
    (SPR_TEST, 0, 3, A_Chase, S_TEST_RUN2),
    # S_HEAD_RUN2
    (SPR_TEST, 0, 3, A_Chase, S_TEST_RUN3),
    # S_HEAD_RUN3
    (SPR_TEST, 1, 3, A_Chase, S_TEST_RUN4),
    # S_HEAD_RUN4
    (SPR_TEST, 1, 3, A_Chase, S_TEST_RUN5),
    # S_HEAD_RUN5
    (SPR_TEST, 2, 3, A_Chase, S_TEST_RUN6),
    # S_HEAD_RUN6
    (SPR_TEST, 2, 3, A_Chase, S_TEST_RUN7),
    # S_HEAD_RUN7
    (SPR_TEST, 3, 3, A_Chase, S_TEST_RUN8),
    # S_HEAD_RUN8
    (SPR_TEST, 3, 3, A_Chase, S_TEST_RUN1),
    # S_HEAD_ATK1
    (SPR_TEST, 4, 5, A_FaceTarget, S_TEST_ATK2),
    # S_HEAD_ATK2
    (SPR_TEST, 5, 5, A_RectMissile, S_TEST_ATK3),
    # S_HEAD_ATK3
    (SPR_TEST, 6, 5, A_FaceTarget, S_TEST_ATK4),
    # S_HEAD_ATK4
    (SPR_TEST, 6, 0, A_RectMissile, S_TEST_RUN1),
    # S_HEAD_PAIN
    (SPR_TEST, 1, 3, None, S_TEST_PAIN2),
    # S_HEAD_PAIN2
    (SPR_TEST, 1, 3, A_Pain, S_TEST_PAIN3),
    # S_HEAD_PAIN3
    (SPR_TEST, 1, 6, None, S_TEST_RUN1),
    # S_HEAD_DIE1
    (SPR_TEST, 7, 8, None, S_TEST_DIE2),
    # S_HEAD_DIE2
    (SPR_TEST, 8, 8, A_Scream, S_TEST_DIE3),
    # S_HEAD_DIE3
    (SPR_TEST, 9, 8, None, S_TEST_DIE4),
    # S_HEAD_DIE4
    (SPR_TEST, 10, 8, A_Fall, S_TEST_DIE5),
    # S_HEAD_DIE5
    (SPR_TEST, 11, 8, A_OnDeathTrigger, S_TEST_DIE6),
    # S_HEAD_DIE6
    (SPR_TEST, 12, -1, None, S_NULL)
])

mobjinfo = c.StructArray(mobjinfo_t, [
    (
        ##MT_PLAYER
        -1,  # #doomednum
        S_PLAY,  # #spawnstate
        100,  # #spawnhealth
        S_PLAY_RUN1,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        0,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_PLAY_PAIN,  # #painstate
        255,  # #painchance
        sfx_plrpain,  # #painsound
        S_NULL,  # #meleestate
        S_PLAY_ATK1,  # #missilestate
        S_PLAY_DIE1,  # #deathstate
        S_PLAY_XDIE1,  # #xdeathstate
        sfx_plrdie,  # #deathsound
        0,  # #speed
        19 * FRACUNIT,  # #radius
        64 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_DROPOFF | MF_PICKUP | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PLAYERBOT1
        3008,  # #doomednum
        S_PBOT_STND,  # #spawnstate
        100,  # #spawnhealth
        S_PBOT_RUN1,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        0,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_PBOT_PAIN,  # #painstate
        255,  # #painchance
        sfx_plrpain,  # #painsound
        S_NULL,  # #meleestate
        S_PBOT_ATK1,  # #missilestate
        S_PLAY_XDIE1,  # #deathstate
        S_PLAY_XDIE1,  # #xdeathstate
        sfx_plrdie,  # #deathsound
        16,  # #speed
        32 * FRACUNIT,  # #radius
        87 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_DROPOFF | MF_COUNTKILL | MF_NOTDMATCH,  # #flags
        1,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PLAYERBOT2
        3009,  # #doomednum
        S_PBOT_STND,  # #spawnstate
        100,  # #spawnhealth
        S_PBOT_RUN1,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        0,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_PBOT_PAIN,  # #painstate
        255,  # #painchance
        sfx_plrpain,  # #painsound
        S_NULL,  # #meleestate
        S_PBOT_PATK1,  # #missilestate
        S_PLAY_DIE1,  # #deathstate
        S_PLAY_XDIE1,  # #xdeathstate
        sfx_plrdie,  # #deathsound
        16,  # #speed
        32 * FRACUNIT,  # #radius
        87 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_DROPOFF | MF_COUNTKILL | MF_NOTDMATCH,  # #flags
        2,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PLAYERBOT3
        3010,  # #doomednum
        S_PBOT_STND,  # #spawnstate
        100,  # #spawnhealth
        S_PBOT_RUN1,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        0,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_PBOT_PAIN,  # #painstate
        255,  # #painchance
        sfx_plrpain,  # #painsound
        S_NULL,  # #meleestate
        S_PBOT_ATK1,  # #missilestate
        S_PLAY_XDIE1,  # #deathstate
        S_PLAY_XDIE1,  # #xdeathstate
        sfx_plrdie,  # #deathsound
        0,  # #speed
        32 * FRACUNIT,  # #radius
        87 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_DROPOFF | MF_COUNTKILL | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_DEMON1
        3002,  # #doomednum
        S_SARG_STND,  # #spawnstate
        150,  # #spawnhealth
        S_SARG_RUN1,  # #seestate
        sfx_sargsit,  # #seesound
        8,  # #reactiontime
        sfx_sargatk,  # #attacksound
        S_SARG_PAIN1,  # #painstate
        180,  # #painchance
        sfx_dbpain2,  # #painsound
        S_SARG_ATK1,  # #meleestate
        S_NULL,  # #missilestate
        S_SARG_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_sargdie,  # #deathsound
        12,  # #speed
        44 * FRACUNIT,  # #radius
        100 * FRACUNIT,  # #height
        400,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_DEMON2
        58,  # #doomednum
        S_SARG_STND,  # #spawnstate
        150,  # #spawnhealth
        S_SARG_RUN0,  # #seestate
        sfx_sargsit,  # #seesound
        8,  # #reactiontime
        sfx_sargatk,  # #attacksound
        S_SARG_PAIN0,  # #painstate
        180,  # #painchance
        sfx_dbpain2,  # #painsound
        S_SARG_ATK0,  # #meleestate
        S_NULL,  # #missilestate
        S_SARG_DIE0,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_sargdie,  # #deathsound
        12,  # #speed
        50 * FRACUNIT,  # #radius
        100 * FRACUNIT,  # #height
        400,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        1,  # #palette
        255  # #alpha
    ),

    (
        ##MT_MANCUBUS
        67,  # #doomednum
        S_FATT_STND,  # #spawnstate
        600,  # #spawnhealth
        S_FATT_RUN1,  # #seestate
        sfx_fattsit,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_FATT_PAIN,  # #painstate
        80,  # #painchance
        sfx_fatthit,  # #painsound
        S_NULL,  # #meleestate
        S_FATT_ATK1,  # #missilestate
        S_FATT_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_fattdie,  # #deathsound
        8,  # #speed
        60 * FRACUNIT,  # #radius
        108 * FRACUNIT,  # #height
        1000,  # #mass
        0,  # #damage
        sfx_posact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_POSSESSED1
        3004,  # #doomednum
        S_POSS1_STND,  # #spawnstate
        20,  # #spawnhealth
        S_POSS1_RUN1,  # #seestate
        sfx_possit1,  # #seesound
        8,  # #reactiontime
        sfx_pistol,  # #attacksound
        S_POSS1_PAIN,  # #painstate
        200,  # #painchance
        sfx_dbpain1,  # #painsound
        S_NULL,  # #meleestate
        S_POSS1_ATK1,  # #missilestate
        S_POSS1_DIE1,  # #deathstate
        S_POSS1_XDIE1,  # #xdeathstate
        sfx_posdie1,  # #deathsound
        8,  # #speed
        32 * FRACUNIT,  # #radius
        87 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_posact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_POSSESSED2
        9,  # #doomednum
        S_POSS2_STND,  # #spawnstate
        30,  # #spawnhealth
        S_POSS2_RUN1,  # #seestate
        sfx_possit2,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_POSS2_PAIN,  # #painstate
        170,  # #painchance
        sfx_dbpain1,  # #painsound
        S_NULL,  # #meleestate
        S_POSS2_ATK1,  # #missilestate
        S_POSS2_DIE1,  # #deathstate
        S_POSS2_XDIE1,  # #xdeathstate
        sfx_posdie2,  # #deathsound
        8,  # #speed
        32 * FRACUNIT,  # #radius
        87 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_posact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        1,  # #palette
        255  # #alpha
    ),

    (
        ##MT_IMP1
        3001,  # #doomednum
        S_TROO_STND,  # #spawnstate
        60,  # #spawnhealth
        S_TROO_RUN1,  # #seestate
        sfx_impsit1,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_TROO_PAIN,  # #painstate
        200,  # #painchance
        sfx_dbpain1,  # #painsound
        S_TROO_MELEE1,  # #meleestate
        S_TROO_ATK1,  # #missilestate
        S_TROO_DIE1,  # #deathstate
        S_TROO_XDIE1,  # #xdeathstate
        sfx_impdth1,  # #deathsound
        8,  # #speed
        42 * FRACUNIT,  # #radius
        94 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_impact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_IMP2
        3007,  # #doomednum
        S_TROO_STND,  # #spawnstate
        60,  # #spawnhealth
        S_TROO_RUN1,  # #seestate
        sfx_impsit1,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_TROO_PAIN,  # #painstate
        128,  # #painchance
        sfx_dbpain1,  # #painsound
        S_TROO_MELEE1,  # #meleestate
        S_TROO_ATK1,  # #missilestate
        S_TROO_DIE1,  # #deathstate
        S_TROO_XDIE1,  # #xdeathstate
        sfx_impdth1,  # #deathsound
        16,  # #speed
        42 * FRACUNIT,  # #radius
        94 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_impact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL | MF_SHADOW,  # #flags
        1,  # #palette
        180  # #alpha
    ),

    (
        ##MT_CACODEMON
        3005,  # #doomednum
        S_HEAD_STND,  # #spawnstate
        400,  # #spawnhealth
        S_HEAD_RUN1,  # #seestate
        sfx_headsit,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_HEAD_PAIN,  # #painstate
        128,  # #painchance
        sfx_dbpain2,  # #painsound
        S_NULL,  # #meleestate
        S_HEAD_ATK1,  # #missilestate
        S_HEAD_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_headdie,  # #deathsound
        8,  # #speed
        55 * FRACUNIT,  # #radius
        90 * FRACUNIT,  # #height
        400,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_FLOAT | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_BRUISER1
        3003,  # #doomednum
        S_BOSS1_STND,  # #spawnstate
        1000,  # #spawnhealth
        S_BOSS1_RUN1,  # #seestate
        sfx_bos1sit,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_BOSS1_PAIN,  # #painstate
        50,  # #painchance
        sfx_dbpain2,  # #painsound
        S_BOSS1_ATK1,  # #meleestate
        S_BOSS1_ATK1,  # #missilestate
        S_BOSS1_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_bos1die,  # #deathsound
        8,  # #speed
        24 * FRACUNIT,  # #radius
        100 * FRACUNIT,  # #height
        1000,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        1,  # #palette
        255  # #alpha
    ),

    (
        ##MT_BRUISER2
        69,  # #doomednum
        S_BOSS2_STND,  # #spawnstate
        500,  # #spawnhealth
        S_BOSS2_RUN1,  # #seestate
        sfx_bos2sit,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_BOSS2_PAIN,  # #painstate
        50,  # #painchance
        sfx_dbpain2,  # #painsound
        S_BOSS2_ATK1,  # #meleestate
        S_BOSS2_ATK1,  # #missilestate
        S_BOSS2_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_bos2die,  # #deathsound
        8,  # #speed
        24 * FRACUNIT,  # #radius
        100 * FRACUNIT,  # #height
        1000,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_SKULL
        3006,  # #doomednum
        S_SKUL_STND,  # #spawnstate
        60,  # #spawnhealth
        S_SKUL_RUN1,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_skullatk,  # #attacksound
        S_SKUL_PAIN,  # #painstate
        256,  # #painchance
        sfx_dbpain2,  # #painsound
        S_NULL,  # #meleestate
        S_SKUL_ATK1,  # #missilestate
        S_SKUL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        8,  # #speed
        28 * FRACUNIT,  # #radius
        64 * FRACUNIT,  # #height
        50,  # #mass
        3,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_FLOAT | MF_COUNTKILL,  # #flags
        0,  # #palette
        192  # #alpha
    ),

    (
        ##MT_BABY
        68,  # #doomednum
        S_BSPI_STND,  # #spawnstate
        500,  # #spawnhealth
        S_BSPI_RUN1,  # #seestate
        sfx_bspisit,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_BSPI_PAIN,  # #painstate
        128,  # #painchance
        sfx_dbpain2,  # #painsound
        S_NULL,  # #meleestate
        S_BSPI_ATK1,  # #missilestate
        S_BSPI_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_bspidie,  # #deathsound
        12,  # #speed
        64 * FRACUNIT,  # #radius
        80 * FRACUNIT,  # #height
        600,  # #mass
        0,  # #damage
        sfx_bspilift,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_CYBORG
        16,  # #doomednum
        S_CYBR_STND,  # #spawnstate
        4000,  # #spawnhealth
        S_CYBR_RUN1,  # #seestate
        sfx_cybsit,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_CYBR_PAIN,  # #painstate
        20,  # #painchance
        sfx_dbpain2,  # #painsound
        S_NULL,  # #meleestate
        S_CYBR_ATK1,  # #missilestate
        S_CYBR_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_cybdth,  # #deathsound
        16,  # #speed
        70 * FRACUNIT,  # #radius
        170 * FRACUNIT,  # #height
        1000,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_CYBORG_TITLE
        3014,  # #doomednum
        S_CYBR_TITLE1,  # #spawnstate
        4000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_CYBR_TITLE2,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        40 * FRACUNIT,  # #radius
        110 * FRACUNIT,  # #height
        1000,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PAIN
        71,  # #doomednum
        S_PAIN_STND,  # #spawnstate
        400,  # #spawnhealth
        S_PAIN_RUN,  # #seestate
        sfx_pesit,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_PAIN_PAIN,  # #painstate
        128,  # #painchance
        sfx_pepain,  # #painsound
        S_NULL,  # #meleestate
        S_PAIN_ATK1,  # #missilestate
        S_PAIN_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_pedie,  # #deathsound
        8,  # #speed
        60 * FRACUNIT,  # #radius
        112 * FRACUNIT,  # #height
        400,  # #mass
        0,  # #damage
        sfx_dbact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_FLOAT | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_RESURRECTOR
        3013,  # #doomednum
        S_RECT_STND,  # #spawnstate
        5000,  # #spawnhealth
        S_RECT_RUN1,  # #seestate
        sfx_rectsit,  # #seesound
        8,  # #reactiontime
        sfx_rectatk,  # #attacksound
        S_RECT_PAIN,  # #painstate
        50,  # #painchance
        sfx_rectpain,  # #painsound
        S_RECT_ATK1,  # #meleestate
        S_NULL,  # #missilestate
        S_RECT_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_rectdie,  # #deathsound
        30,  # #speed
        80 * FRACUNIT,  # #radius
        150 * FRACUNIT,  # #height
        1000,  # #mass
        0,  # #damage
        sfx_rectact,  # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_DROPOFF | MF_COUNTKILL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_CAMERA
        0,  # #doomednum
        S_NULL,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOSECTOR | MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_DEST_TELEPORT
        14,  # #doomednum
        S_NULL,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOSECTOR | MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_DEST_PROJECTILE
        2050,  # #doomednum
        S_NULL,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOSECTOR | MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_FAKEITEM
        89,  # #doomednum
        S_FAKEITEM,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        32 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_NOSECTOR,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_LASERMARKER
        90,  # #doomednum
        S_NULL,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_RENDERLASER,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_ROCKET
        -1,  # #doomednum
        S_ROCKET,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_missile,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_ROCKET_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_explode,  # #deathsound
        30 * FRACUNIT,  # #speed
        11 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        20,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_PLASMA
        -1,  # #doomednum
        S_PLASMA1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_plasma,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_PLASMA_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        40 * FRACUNIT,  # #speed
        13 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        5,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_BFG
        -1,  # #doomednum
        S_BFGBALL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_BFGBALL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_bfgexp,  # #deathsound
        40 * FRACUNIT,  # #speed
        13 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        100,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_LASER
        -1,  # #doomednum
        S_LASER1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_IMP1
        -1,  # #doomednum
        S_TBALL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_bdmissile,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_TBALL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        10 * FRACUNIT,  # #speed
        6 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        3,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_IMP2
        -1,  # #doomednum
        S_NBALL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_bdmissile,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NBALL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        20 * FRACUNIT,  # #speed
        6 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        3,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        100  # #alpha
    ),

    (
        ##MT_PROJ_HEAD
        -1,  # #doomednum
        S_CBALL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_bdmissile,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_CBALL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        20 * FRACUNIT,  # #speed
        6 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        5,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_BRUISER1
        -1,  # #doomednum
        S_BGBALL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_bdmissile,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_BGBALL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        15 * FRACUNIT,  # #speed
        6 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        8,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_BRUISER2
        -1,  # #doomednum
        S_BRBALL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_bdmissile,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_BRBALL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        15 * FRACUNIT,  # #speed
        6 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        8,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_BABY
        -1,  # #doomednum
        S_APLS1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_plasma,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_APLS_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        25 * FRACUNIT,  # #speed
        13 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        3,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_FATSO
        -1,  # #doomednum
        S_MANF1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_bdmissile,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_MANF_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_implod,  # #deathsound
        20 * FRACUNIT,  # #speed
        6 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        8,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_TRACER
        -1,  # #doomednum
        S_TRCR1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_tracer,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_TRCR_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_explode,  # #deathsound
        10 * FRACUNIT,  # #speed
        11 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        10,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_DART
        -1,  # #doomednum
        S_DART,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_dart,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        16 * FRACUNIT,  # #speed
        13 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        4,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROJ_RECTFIRE
        -1,  # #doomednum
        S_RFIRE1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_tracer,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        20 * FRACUNIT,  # #speed
        16 * FRACUNIT,  # #radius
        64 * FRACUNIT,  # #height
        100,  # #mass
        5,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_GRAVITY | MF_DROPOFF | MF_MISSILE | MF_SHADOW,  # #flags
        0,  # #palette
        180  # #alpha
    ),

    (
        ##MT_PROJ_RECT
        -1,  # #doomednum
        S_RBALL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_tracer,  # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_RBALL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_explode,  # #deathsound
        18 * FRACUNIT,  # #speed
        11 * FRACUNIT,  # #radius
        8 * FRACUNIT,  # #height
        100,  # #mass
        10,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_SMOKE_GRAY
        -1,  # #doomednum
        S_PUF21,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        120  # #alpha
    ),

    (
        ##MT_SMOKE_RED
        -1,  # #doomednum
        S_PUF31,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        120  # #alpha
    ),

    (
        ##MT_SMOKE_SMALL
        -1,  # #doomednum
        S_PUFF1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SHADOW,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_BLOOD
        -1,  # #doomednum
        S_BLOOD1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_GRAVITY,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_CRUSHED
        24,  # #doomednum
        S_CORPSE,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_TELEPORTFOG
        -1,  # #doomednum
        S_TFOG1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SHADOW,  # #flags
        0,  # #palette
        140  # #alpha
    ),

    (
        ##MT_BFGSPREAD
        -1,  # #doomednum
        S_BFGEXP1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_ARMOR1
        2018,  # #doomednum
        S_ARMOR1A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_ARMOR2
        2019,  # #doomednum
        S_ARMOR2A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_BONUSHEALTH
        2014,  # #doomednum
        S_BONUS1A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_BONUSARMOR
        2015,  # #doomednum
        S_BONUS2A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_BLUECARDKEY
        5,  # #doomednum
        S_BKEY1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_REDCARDKEY
        13,  # #doomednum
        S_RKEY1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_YELLOWCARDKEY
        6,  # #doomednum
        S_YKEY1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_YELLOWSKULLKEY
        39,  # #doomednum
        S_YSKULL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_REDSKULLKEY
        38,  # #doomednum
        S_RSKULL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_BLUESKULLKEY
        40,  # #doomednum
        S_BSKULL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_NOTDMATCH,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_ARTIFACT1
        1042,  # #doomednum
        S_ARTIFACT1A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_ARTIFACT2
        1043,  # #doomednum
        S_ARTIFACT2A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_ARTIFACT3
        1044,  # #doomednum
        S_ARTIFACT3A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_STIMPACK
        2011,  # #doomednum
        S_STIM,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_MEDKIT
        2012,  # #doomednum
        S_MEDI,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_SOULSPHERE
        2013,  # #doomednum
        S_SOUL1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_INVULSPHERE
        2022,  # #doomednum
        S_PINV1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_BERSERK
        2023,  # #doomednum
        S_PSTR,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_INVISSPHERE
        2024,  # #doomednum
        S_PINS1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM | MF_SHADOW,  # #flags
        0,  # #palette
        176  # #alpha
    ),

    (
        ##MT_ITEM_RADSPHERE
        2025,  # #doomednum
        S_SUIT1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_AUTOMAP
        2026,  # #doomednum
        S_PMAP1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_PVIS
        2045,  # #doomednum
        S_PVIS1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_ITEM_MEGASPHERE
        83,  # #doomednum
        S_MEGA1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL | MF_COUNTITEM,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_CLIP
        2007,  # #doomednum
        S_CLIP,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_CLIPBOX
        2048,  # #doomednum
        S_AMMO,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_ROCKET
        2010,  # #doomednum
        S_RCKT,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_ROCKETBOX
        2046,  # #doomednum
        S_BROK,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_CELL
        2047,  # #doomednum
        S_CELL,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_CELLPACK
        17,  # #doomednum
        S_CELP,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_SHELL
        2008,  # #doomednum
        S_SHEL,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_SHELLBOX
        2049,  # #doomednum
        S_SBOX,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_AMMO_BACKPACK
        8,  # #doomednum
        S_BPAK,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_BFG
        2006,  # #doomednum
        S_BFUG,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_CHAINSAW
        2005,  # #doomednum
        S_CSAW,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_CHAINGUN
        2002,  # #doomednum
        S_MGUN,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_LAUNCHER
        2003,  # #doomednum
        S_LAUN,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_PLASMA
        2004,  # #doomednum
        S_PLSM,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_SHOTGUN
        2001,  # #doomednum
        S_SHOT,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_SSHOTGUN
        82,  # #doomednum
        S_SHOT2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_WEAP_LCARBINE
        84,  # #doomednum
        S_LSRG,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SPECIAL,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_FIRE
        2051,  # #doomednum
        S_PROP_FIRE1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        16 * FRACUNIT,  # #radius
        64 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SHADOW,  # #flags
        0,  # #palette
        140  # #alpha
    ),

    (
        ##MT_PROP_CANDLE
        34,  # #doomednum
        S_CANDLE1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_BARREL
        1001,  # #doomednum
        S_BARREL,  # #spawnstate
        20,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_BARREL_DIE1,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_explode,  # #deathsound
        0,  # #speed
        16 * FRACUNIT,  # #radius
        50 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID | MF_SHOOTABLE | MF_NOBLOOD,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_EXPLOSION1
        -1,  # #doomednum
        S_EXP1A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        80  # #alpha
    ),

    (
        ##MT_EXPLOSION2
        -1,  # #doomednum
        S_EXP2A,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP,  # #flags
        0,  # #palette
        80  # #alpha
    ),

    (
        ##MT_PROP_TECHLAMP1
        1015,  # #doomednum
        S_LAMP1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        54 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TECHLAMP2
        1016,  # #doomednum
        S_LAMP2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        12 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TORCHBLUE
        1003,  # #doomednum
        S_BTORCH1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TORCHYELLOW
        1039,  # #doomednum
        S_YTORCH1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TORCHRED
        1025,  # #doomednum
        S_RTORCH1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_POLEBASELONG
        1050,  # #doomednum
        S_POLELONG,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        12 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_POLEBASESHORT
        1051,  # #doomednum
        S_POLESHORT,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_FIREBLUE
        1033,  # #doomednum
        S_BFLAME1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        192  # #alpha
    ),

    (
        ##MT_PROP_FIRERED
        1034,  # #doomednum
        S_RFLAME1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        192  # #alpha
    ),

    (
        ##MT_PROP_FIREYELLOW
        1035,  # #doomednum
        S_YFLAME1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        192  # #alpha
    ),

    (
        ##MT_GIB_MEATSTICK
        1005,  # #doomednum
        S_GORE1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_MEATHANG
        1006,  # #doomednum
        S_GORE2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        95 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_TORSOHANG
        1007,  # #doomednum
        S_GORE3,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        83 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_RIBFLOOR
        1008,  # #doomednum
        S_GORE4,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_TWITCHFLOOR
        1009,  # #doomednum
        S_GORETWITCH1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_BLOODPOOL
        1010,  # #doomednum
        S_GORE5,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_BONEFLOOR
        1011,  # #doomednum
        S_GORE6,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_MEATRIBFLOOR
        1012,  # #doomednum
        S_GORE7,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_MEATRIBCAGE
        1013,  # #doomednum
        S_GORE8,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        0,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_CHAINHOOK
        1014,  # #doomednum
        S_GOREHOOK1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        95 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HANGCAGE
        1017,  # #doomednum
        S_GORECAGE,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        91 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_CHAINPINSER
        1018,  # #doomednum
        S_GOREHOOK2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        101 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_CHAINARM
        1019,  # #doomednum
        S_GOREHOOK3,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        58 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HANGMACE1
        1020,  # #doomednum
        S_GOREMACE1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        80 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HEADSTICK1
        1022,  # #doomednum
        S_GOREHEAD1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HEADSTICK2
        1023,  # #doomednum
        S_GOREHEAD2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_DOUBLEMEATSTICK
        1024,  # #doomednum
        S_GORE9,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_STATUE1
        1028,  # #doomednum
        S_GARGOYLE1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_STATUE2
        1029,  # #doomednum
        S_GARGOYLE2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TECHPOLELONG
        1031,  # #doomednum
        S_TECHLAMP1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        80 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TECHPOLESHORT
        1032,  # #doomednum
        S_TECHLAMP2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        62 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TREESTUMPSMALL
        1036,  # #doomednum
        S_TREE3,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        16 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TREESTUMPLARGE
        1037,  # #doomednum
        S_TREE2,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        16 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_TREE
        1038,  # #doomednum
        S_TREE1,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        16 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_PROP_BLOODYPOLE
        1045,  # #doomednum
        S_GORE10,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        8 * FRACUNIT,  # #radius
        16 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_SOLID,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HANGMACE2
        1046,  # #doomednum
        S_GOREMACE,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        56 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HANGWHITEMEAT
        1047,  # #doomednum
        S_GORE11,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        64 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HANGHEAD
        1048,  # #doomednum
        S_GOREHEAD3,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        60 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),

    (
        ##MT_GIB_HANGRIB
        1049,  # #doomednum
        S_GORE12,  # #spawnstate
        1000,  # #spawnhealth
        S_NULL,  # #seestate
        sfx_None,  # sfx_000,        # #seesound
        8,  # #reactiontime
        sfx_None,  # sfx_000,        # #attacksound
        S_NULL,  # #painstate
        0,  # #painchance
        sfx_None,  # sfx_000,        # #painsound
        S_NULL,  # #meleestate
        S_NULL,  # #missilestate
        S_NULL,  # #deathstate
        S_NULL,  # #xdeathstate
        sfx_None,  # sfx_000,        # #deathsound
        0,  # #speed
        20 * FRACUNIT,  # #radius
        98 * FRACUNIT,  # #height
        100,  # #mass
        0,  # #damage
        sfx_None,  # sfx_000,        # #activesound
        MF_NOBLOCKMAP | MF_SPAWNCEILING,  # #flags
        0,  # #palette
        255  # #alpha
    ),
    (  # MT_MISC2
        1015,  # doomednum
        S_LAMP1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        47 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC3
        1016,  # doomednum
        S_LAMP2,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        12 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC4
        1003,  # doomednum
        S_BWTORCH1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC5
        1039,  # doomednum
        S_YWTORCH1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC6
        1025,  # doomednum
        S_RWTORCH1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC7
        1033,  # doomednum
        S_BFLM1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        192  # alpha
    ),

    (  # MT_MISC8
        1034,  # doomednum
        S_RFLM1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        192  # alpha
    ),

    (  # MT_MISC9
        1035,  # doomednum
        S_YFLM1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        192  # alpha
    ),

    (  # MT_MISC10
        1005,  # doomednum
        S_MISC5,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC11
        1006,  # doomednum
        S_MISC6,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        65 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC12
        1007,  # doomednum
        S_MISC7,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        132 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC13
        1008,  # doomednum
        S_MISC8_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC14
        1009,  # doomednum
        S_MISC9_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC15
        1010,  # doomednum
        S_MISC10,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC16
        1011,  # doomednum
        S_MISC11_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),
    (  # MT_MISC17
        1012,  # doomednum
        S_MISC12_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC18
        1013,  # doomednum
        S_MISC13_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC19
        1014,  # doomednum
        S_MISC14,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        85 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC20
        1017,  # doomednum
        S_MISC17,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        132 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC21
        1018,  # doomednum
        S_MISC18,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        62 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC22
        1019,  # doomednum
        S_MISC19,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        72 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC23
        1020,  # doomednum
        S_MISC20,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        62 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC24
        1021,  # doomednum
        S_MISC21_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        97 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SPAWNCEILING | MF_NOBLOCKMAP,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC25
        1022,  # doomednum
        S_MISC22,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        8 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC26
        1023,  # doomednum
        S_MISC23,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        8 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC27
        1024,  # doomednum
        S_MISC24,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        8 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC28
        1028,  # doomednum
        S_MISC28,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC29
        1029,  # doomednum
        S_MISC29,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC30
        1031,  # doomednum
        S_MISC31,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        8 * FRACUNIT,  # radius
        80 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC31
        1032,  # doomednum
        S_MISC32,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        8 * FRACUNIT,  # radius
        62 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC32
        1027,  # doomednum
        S_MISC27,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        14 * FRACUNIT,  # radius
        80 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC33
        1036,  # doomednum
        S_MISC36,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        16 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC34
        1037,  # doomednum
        S_MISC37,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        16 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC35
        1038,  # doomednum
        S_MISC38,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        16 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC36
        1040,  # doomednum
        S_MISC45,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        32 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC37
        1041,  # doomednum
        S_MISC41,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC38
        1026,  # doomednum
        S_MISC26,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        20 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        0,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC39
        45,  # doomednum
        S_MISC46,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        32 * FRACUNIT,  # radius
        81 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC40
        70,  # doomednum
        S_MISC47_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        16 * FRACUNIT,  # radius
        16 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (  # MT_MISC41
        1030,  # doomednum
        S_MISC30_1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_None,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_NULL,  # deathstate
        S_NULL,  # xdeathstate
        sfx_None,  # deathsound
        0,  # speed
        8 * FRACUNIT,  # radius
        62 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_None,  # activesound
        MF_SOLID,  # flags
        0,  # palette
        255  # alpha
    ),

    (
        # MT_CHAINGUY
        65,  # doomednum
        S_CPOS_STND,  # spawnstate
        70,  # spawnhealth
        S_CPOS_RUN1,  # seestate
        sfx_possit2,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_CPOS_PAIN,  # painstate
        170,  # painchance
        sfx_dbpain1,  # painsound
        S_NULL,  # meleestate
        S_CPOS_ATK1,  # missilestate
        S_CPOS_DIE1,  # deathstate
        S_CPOS_XDIE1,  # xdeathstate
        sfx_posdie2,  # deathsound
        8,  # speed
        32 * FRACUNIT,  # radius
        87 * FRACUNIT,  # height
        100,  # mass
        0,  # damage
        sfx_posact,  # activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # flags
        0,  # palette
        255  # alpha
    ),

    (
        # MT_UNDEAD
        66,  # doomednum
        S_SKEL_STND,  # spawnstate
        300,  # spawnhealth
        S_SKEL_RUN1,  # seestate
        sfx_skelsit,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_SKEL_PAIN,  # painstate
        100,  # painchance
        sfx_dbpain1,  # painsound
        S_SKEL_FIST1,  # meleestate
        S_SKEL_MISS1,  # missilestate
        S_SKEL_DIE1,  # deathstate
        S_NULL,  # xdeathstate
        sfx_skeldth,  # deathsound
        10,  # speed
        32 * FRACUNIT,  # radius
        120 * FRACUNIT,  # height
        500,  # mass
        0,  # damage
        sfx_skelact,  # activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # flags
        0,  # palette
        255  # alpha
    ),

    (
        # MT_PROJ_UNDEAD
        -1,  # doomednum
        S_ARCR1,  # spawnstate
        1000,  # spawnhealth
        S_NULL,  # seestate
        sfx_tracer,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_NULL,  # painstate
        0,  # painchance
        sfx_None,  # painsound
        S_NULL,  # meleestate
        S_NULL,  # missilestate
        S_POW1_DIE1,  # deathstate
        S_NULL,  # xdeathstate
        sfx_explode,  # deathsound
        7 * FRACUNIT,  # speed
        11 * FRACUNIT,  # radius
        8 * FRACUNIT,  # height
        100,  # mass
        5,  # damage
        sfx_None,  # activesound
        MF_NOBLOCKMAP | MF_DROPOFF | MF_MISSILE,  # flags
        0,  # palette
        255  # alpha
    ),

    (
        # MT_SPIDER
        7,  # doomednum
        S_SPID_STND,  # spawnstate
        3000,  # spawnhealth
        S_SPID_RUN1,  # seestate
        sfx_spisit,  # seesound
        8,  # reactiontime
        sfx_pistol,  # attacksound
        S_SPID_PAIN,  # painstate
        40,  # painchance
        sfx_dbpain2,  # painsound
        S_NULL,  # meleestate
        S_SPID_ATK1,  # missilestate
        S_SPID_DIE1,  # deathstate
        S_NULL,  # xdeathstate
        sfx_spidth,  # deathsound
        12,  # speed
        128 * FRACUNIT,  # radius
        140 * FRACUNIT,  # height
        1000,  # mass
        0,  # damage
        sfx_dbact,  # activesound
        MF_SOLID | MF_SHOOTABLE | MF_GRAVITY | MF_COUNTKILL,  # flags,
        0,  # palette
        255  # alpha
    ),
    (
        # MT_TESTA0
        9005,  # doomednum
        S_TEST_STND,  # spawnstate
        800,  # spawnhealth
        S_TEST_RUN1,  # seestate
        sfx_headsit,  # seesound
        8,  # reactiontime
        sfx_None,  # attacksound
        S_TEST_PAIN,  # painstate
        128,  # painchance
        sfx_dbpain2,  # painsound
        S_NULL,  # meleestate
        S_TEST_ATK1,  # missilestate
        S_TEST_DIE1,  # deathstate
        S_NULL,  # xdeathstate
        sfx_headdie,  # deathsound
        12,  # speed
        55 * FRACUNIT,  # radius
        90 * FRACUNIT,  # height
        500,  # mass
        0,  # damage
        sfx_dbact,  # activesound
        MF_SOLID | MF_SHOOTABLE | MF_FLOAT | MF_COUNTKILL,  # flags
        0,  # palette
        255  # alpha
    )
], one_indexed=True)

mobjinfo.set_object_names([
    "Player",
    "Player Bot 1",
    "Player Bot 2",
    "Player Bot 3",
    "Demon",
    "Spectre",
    "Mancubus",
    "Zombieman",
    "Sargeant",
    "Imp",
    "Nightmare Imp",
    "Cacodemon",
    "Baron of Hell",
    "Hell Knight",
    "Lost Soul",
    "Arachnotron",
    "Cyberdemon",
    "Cyberdemon Title",
    "Pain Elemental",
    "Resurrector / Mother Demon",
    "Camera",
    "Destination Teleporter",
    "Destination Projectile",
    "Fake Item",
    "Laser Marker",
    "Rocket Projectile",
    "Plasma Projectile",
    "BFG Projectile",
    "Laser Projectile",
    "Imp Projectile",
    "Nightmare Imp Projectile",
    "Cacodemon Projectile",
    "Baron of Hell Projectile",
    "Hell Knight Projectile",
    "Arachnotron Projectile",
    "Mancubi Projectile",
    "Tracer Projectile",
    "Dart Projectile",
    "Mother Demon Projectile Ball",
    "Mother Demon Projectile",
    "Gray Smoke",
    "Red Smoke",
    "Small Smoke",
    "Blood",
    "Crushed Gibs",
    "Teleporter Fog",
    "BFG Spread",
    "Armor 1",
    "Armor 2",
    "Bonus Health",
    "Bonus Armor",
    "Blue Card Key",
    "Red Card Key",
    "Yellow Card Key",
    "Yellow Skull Key",
    "Red Skull Key",
    "Blue Skull Key",
    "Artifact 1",
    "Artifact 2",
    "Artifact 3",
    "Stimpack",
    "Medkit",
    "Soul Sphere",
    "Invulnerability Sphere",
    "Berserk",
    "Invisibility Sphere",
    "Radiation Sphere",
    "Automap",
    "Visibility Visor",
    "Mega Sphere",
    "Ammo Clip",
    "Ammo Clip Box",
    "Ammo Rocket",
    "Ammo Rocket Box",
    "Ammo Cell",
    "Ammo Cell Pack",
    "Ammo Shell",
    "Ammo Shell Box",
    "Ammo Back Pack",
    "Weapon BFG",
    "Weapon Chainsaw",
    "Weapon Chaingun",
    "Weapon Rocket Launcher",
    "Weapon Plasma Gun",
    "Weapon Shotgun",
    "Weapon Super Shotgun",
    "Weapon Umaker",
    "Prop Fire",
    "Prop Candle",
    "Prop Barrel",
    "Explosion 1",
    "Explosion 2",
    "Prop Tech Lamp 1",
    "Prop Tech Lamp 2",
    "Prop Blue Torch",
    "Prop Yellow Torch",
    "Prop Red Torch",
    "Prop Pole Long",
    "Prop Pole Short",
    "Prop Fire Blue",
    "Prop Fire Red",
    "Prop Fire Yellow",
    "Gib Meat Stick",
    "Gib Meat Hang",
    "Gib Torso Hang",
    "Gib Ribs Floor",
    "Gib Twitching Floor",
    "Gib Blood Pool",
    "Gib Bones Floor",
    "Gib Meat Ribs Floor",
    "Gib Meat Ribs Cage",
    "Gib Chain Hook",
    "Gib Hang Cage",
    "Gib Chain Pinser",
    "Gib Chain Arm",
    "Gib Hang Mace 1",
    "Gib Head Stick 1",
    "Gib Head Stick 2",
    "Gib Double Meat Stick",
    "Prop Statue 1",
    "Prop Statue 2",
    "Prop Tech Pole Long",
    "Prop Tech Pole Short",
    "Prop Tree Stump Small",
    "Prop Tree Stump Large",
    "Prop Tree",
    "Prop Bloody Pole",
    "Gib Hang Mace 2",
    "Gib Hang White Meat",
    "Gib Hang Head",
    "Gib Hang Ribs",
])

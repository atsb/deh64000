import deh9000
from deh9000 import *

a = deh9000.DehackedFile()
b = deh9000.DehackedFile()
c = deh9000.DehackedFile()
d = deh9000.DehackedFile()
e = deh9000.DehackedFile()
f = deh9000.DehackedFile()
g = deh9000.DehackedFile()
h = deh9000.DehackedFile()

# Give all weapons infinite ammo.
for weapon in weaponinfo:
	weapon.ammo = am_noammo

dehfile.save("infinite_ammo.deh")

z = deh9000.DehackedFile()

for mob in mobjinfo:
	z.mobjinfo[deh9000.MT_PLAYER].mass = 1
	z.mobjinfo[deh9000.MT_PLAYERBOT1].mass = 1
	z.mobjinfo[deh9000.MT_PLAYERBOT2].mass = 1
	z.mobjinfo[deh9000.MT_PLAYERBOT3].mass = 1
	z.mobjinfo[deh9000.MT_DEMON1].mass = 1
	z.mobjinfo[deh9000.MT_DEMON2].mass = 1
	z.mobjinfo[deh9000.MT_MANCUBUS].mass = 1
	z.mobjinfo[deh9000.MT_POSSESSED1].mass = 1
	z.mobjinfo[deh9000.MT_POSSESSED2].mass = 1
	z.mobjinfo[deh9000.MT_IMP1].mass = 1
	z.mobjinfo[deh9000.MT_IMP2].mass = 1
	z.mobjinfo[deh9000.MT_CACODEMON].mass = 1
	z.mobjinfo[deh9000.MT_BRUISER1].mass = 1
	z.mobjinfo[deh9000.MT_BRUISER2].mass = 1
	z.mobjinfo[deh9000.MT_SKULL].mass = 1
	z.mobjinfo[deh9000.MT_BABY].mass = 1
	z.mobjinfo[deh9000.MT_CYBORG].mass = 1
	z.mobjinfo[deh9000.MT_CYBORG_TITLE].mass = 1
	z.mobjinfo[deh9000.MT_PAIN].mass = 1
	z.mobjinfo[deh9000.MT_RESURRECTOR].mass = 1
	z.mobjinfo[deh9000.MT_CAMERA].mass = 1
	z.mobjinfo[deh9000.MT_DEST_TELEPORT].mass = 1
	z.mobjinfo[deh9000.MT_DEST_PROJECTILE].mass = 1
	z.mobjinfo[deh9000.MT_FAKEITEM].mass = 1
	z.mobjinfo[deh9000.MT_LASERMARKER].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_ROCKET].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_PLASMA].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_BFG].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_LASER].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_IMP1].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_IMP2].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_HEAD].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_BRUISER1].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_BRUISER2].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_BABY].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_FATSO].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_TRACER].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_DART].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_RECTFIRE].mass = 1
	z.mobjinfo[deh9000.MT_PROJ_RECT].mass = 1
	z.mobjinfo[deh9000.MT_SMOKE_GRAY].mass = 1
	z.mobjinfo[deh9000.MT_SMOKE_RED].mass = 1
	z.mobjinfo[deh9000.MT_SMOKE_SMALL].mass = 1
	z.mobjinfo[deh9000.MT_BLOOD].mass = 1
	z.mobjinfo[deh9000.MT_GIB_CRUSHED].mass = 1
	z.mobjinfo[deh9000.MT_TELEPORTFOG].mass = 1
	z.mobjinfo[deh9000.MT_BFGSPREAD].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_ARMOR1].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_ARMOR2].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_BONUSHEALTH].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_BONUSARMOR].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_BLUECARDKEY].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_REDCARDKEY].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_YELLOWCARDKEY].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_YELLOWSKULLKEY].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_REDSKULLKEY].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_BLUESKULLKEY].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_ARTIFACT1].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_ARTIFACT2].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_ARTIFACT3].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_STIMPACK].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_MEDKIT].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_SOULSPHERE].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_INVULSPHERE].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_BERSERK].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_INVISSPHERE].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_RADSPHERE].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_AUTOMAP].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_PVIS].mass = 1
	z.mobjinfo[deh9000.MT_ITEM_MEGASPHERE].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_CLIP].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_CLIPBOX].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_ROCKET].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_ROCKETBOX].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_CELL].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_CELLPACK].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_SHELL].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_SHELLBOX].mass = 1
	z.mobjinfo[deh9000.MT_AMMO_BACKPACK].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_BFG].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_CHAINSAW].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_CHAINGUN].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_LAUNCHER].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_PLASMA].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_SHOTGUN].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_SSHOTGUN].mass = 1
	z.mobjinfo[deh9000.MT_WEAP_LCARBINE].mass = 1
	z.mobjinfo[deh9000.MT_PROP_FIRE].mass = 1
	z.mobjinfo[deh9000.MT_PROP_CANDLE].mass = 1
	z.mobjinfo[deh9000.MT_PROP_BARREL].mass = 1
	z.mobjinfo[deh9000.MT_EXPLOSION1].mass = 1
	z.mobjinfo[deh9000.MT_EXPLOSION2].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TECHLAMP1].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TECHLAMP2].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TORCHBLUE].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TORCHYELLOW].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TORCHRED].mass = 1
	z.mobjinfo[deh9000.MT_PROP_POLEBASELONG].mass = 1
	z.mobjinfo[deh9000.MT_PROP_POLEBASESHORT].mass = 1
	z.mobjinfo[deh9000.MT_PROP_FIREBLUE].mass = 1
	z.mobjinfo[deh9000.MT_PROP_FIRERED].mass = 1
	z.mobjinfo[deh9000.MT_PROP_FIREYELLOW].mass = 1
	z.mobjinfo[deh9000.MT_GIB_MEATSTICK].mass = 1
	z.mobjinfo[deh9000.MT_GIB_MEATHANG].mass = 1
	z.mobjinfo[deh9000.MT_GIB_TORSOHANG].mass = 1
	z.mobjinfo[deh9000.MT_GIB_RIBFLOOR].mass = 1
	z.mobjinfo[deh9000.MT_GIB_TWITCHFLOOR].mass = 1
	z.mobjinfo[deh9000.MT_GIB_BLOODPOOL].mass = 1
	z.mobjinfo[deh9000.MT_GIB_BONEFLOOR].mass = 1
	z.mobjinfo[deh9000.MT_GIB_MEATRIBFLOOR].mass = 1
	z.mobjinfo[deh9000.MT_GIB_MEATRIBCAGE].mass = 1
	z.mobjinfo[deh9000.MT_GIB_CHAINHOOK].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HANGCAGE].mass = 1
	z.mobjinfo[deh9000.MT_GIB_CHAINPINSER].mass = 1
	z.mobjinfo[deh9000.MT_GIB_CHAINARM].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HANGMACE1].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HEADSTICK1].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HEADSTICK2].mass = 1
	z.mobjinfo[deh9000.MT_GIB_DOUBLEMEATSTICK].mass = 1
	z.mobjinfo[deh9000.MT_PROP_STATUE1].mass = 1
	z.mobjinfo[deh9000.MT_PROP_STATUE2].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TECHPOLELONG].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TECHPOLESHORT].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TREESTUMPSMALL].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TREESTUMPLARGE].mass = 1
	z.mobjinfo[deh9000.MT_PROP_TREE].mass = 1
	z.mobjinfo[deh9000.MT_PROP_BLOODYPOLE].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HANGMACE2].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HANGWHITEMEAT].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HANGHEAD].mass = 1
	z.mobjinfo[deh9000.MT_GIB_HANGRIB].mass = 1

z.save("things.deh")

pistol_states = (
	deh9000.S_PISTOL1, deh9000.S_PISTOL2, deh9000.S_PISTOL3,
	deh9000.S_PISTOL4, deh9000.S_PISTOL5,
)

sgun_states = (
	deh9000.S_SGUN1, deh9000.S_SGUN2, deh9000.S_SGUN3,
	deh9000.S_SGUN4, deh9000.S_SGUN5, deh9000.S_SGUN6,
)

ssg_states = (
	deh9000.S_SSG1, deh9000.S_SSG2, deh9000.S_SSG3,
	deh9000.S_SSG4, deh9000.S_SSG5,deh9000.S_SSG6,
	deh9000.S_SSG7, deh9000.S_SSG8,
	deh9000.S_SSG9, deh9000.S_SSG10,
)

chain_states = (
	deh9000.S_CHAING1, deh9000.S_CHAING2, deh9000.S_CHAING3,
)

rocket_states = (
	deh9000.S_ROCKETL1, deh9000.S_ROCKETL2, deh9000.S_ROCKETL3,
)

plasma_states = (
	deh9000.S_PLASMAG1, deh9000.S_PLASMAG2, deh9000.S_PLASMAG3,
)

bfg_states = (
	deh9000.S_BFG1, deh9000.S_BFG2, deh9000.S_BFG3,
	deh9000.S_BFG4,
)

laser_states = (
	deh9000.S_LASERG1, deh9000.S_LASERG2,
)

macubus_attack = (
	deh9000.S_FATT_ATK1, deh9000.S_FATT_ATK2,
	deh9000.S_FATT_ATK3, deh9000.S_FATT_ATK4,
	deh9000.S_FATT_ATK5, deh9000.S_FATT_ATK6,
	deh9000.S_FATT_ATK7,
)

zombieman_attack = (
	deh9000.S_POSS1_ATK1, deh9000.S_POSS1_ATK2,
	deh9000.S_POSS1_ATK3,
)

sargeant_attack = (
	deh9000.S_POSS2_ATK1, deh9000.S_POSS2_ATK2,
	deh9000.S_POSS2_ATK3,
)

imp_attack = (
	deh9000.S_TROO_ATK1, deh9000.S_TROO_ATK2,
	deh9000.S_TROO_ATK3,
)

cacodemon_attack = (
	deh9000.S_HEAD_ATK1, deh9000.S_HEAD_ATK2,
	deh9000.S_HEAD_ATK3,
)

baronofhell_attack = (
	deh9000.S_BOSS1_ATK1, deh9000.S_BOSS1_ATK2,
	deh9000.S_BOSS1_ATK3,
)

hellknight_attack = (
	deh9000.S_BOSS2_ATK1, deh9000.S_BOSS2_ATK2,
	deh9000.S_BOSS2_ATK3,
)

lostsoul_attack = (
	deh9000.S_SKUL_ATK1, deh9000.S_SKUL_ATK2,
	deh9000.S_SKUL_ATK3, deh9000.S_SKUL_ATK4,
)

arachnotron_attack = (
	deh9000.S_BSPI_ATK1, deh9000.S_BSPI_ATK2,
	deh9000.S_BSPI_ATK3,
)

cyberdemon_attack = (
	deh9000.S_CYBR_ATK1, deh9000.S_CYBR_ATK2,
	deh9000.S_CYBR_ATK3, deh9000.S_CYBR_ATK4,
	deh9000.S_CYBR_ATK5, deh9000.S_CYBR_ATK6,
)

resurrector_attack = (
	deh9000.S_RECT_ATK1, deh9000.S_RECT_ATK2,
	deh9000.S_RECT_ATK3, deh9000.S_RECT_ATK4,
)

punch_states = (
	deh9000.S_PUNCH1, deh9000.S_PUNCH2,
	deh9000.S_PUNCH3, deh9000.S_PUNCH4,
	deh9000.S_PUNCH5,
)

saw_states = (
	deh9000.S_SAW1, deh9000.S_SAW2, deh9000.S_SAW3,
)

# Make the pistol fire really quickly.
for state_id in pistol_states:
	a.states[state_id].tics = 1

a.save("fastpistol.deh")

# Make the pistol fire really quickly.
for state_id in sgun_states:
	b.states[state_id].tics = 1

b.save("fastsgun.deh")

# Make the pistol fire really quickly.
for state_id in ssg_states:
	c.states[state_id].tics = 1

c.save("fastssg.deh")

# Make the pistol fire really quickly.
for state_id in chain_states:
	d.states[state_id].tics = 1

d.save("fastchain.deh")

# Make the pistol fire really quickly.
for state_id in rocket_states:
	e.states[state_id].tics = 1

e.save("fastrocket.deh")

# Make the pistol fire really quickly.
for state_id in plasma_states:
	f.states[state_id].tics = 1

f.save("fastplasma.deh")

# Make the pistol fire really quickly.
for state_id in bfg_states:
	g.states[state_id].tics = 1

g.save("fastbfg.deh")

# Make the pistol fire really quickly.
for state_id in laser_states:
	h.states[state_id].tics = 1

h.save("fastlaser.deh")

# Make the pistol fire really quickly.
for state_id in punch_states:
	h.states[state_id].tics = 1

h.save("fastpunch.deh")

# Make the pistol fire really quickly.
for state_id in saw_states:
	h.states[state_id].tics = 1

h.save("fastsaw.deh")

# Make the pistol fire really quickly.
for state_id in macubus_attack:
	h.states[state_id].tics = 1

h.save("fastmancattack.deh")

# Make the pistol fire really quickly.
for state_id in zombieman_attack:
	h.states[state_id].tics = 1

h.save("fastzombieattack.deh")

# Make the pistol fire really quickly.
for state_id in sargeant_attack:
	h.states[state_id].tics = 1

h.save("fastsargeantattack.deh")

# Make the pistol fire really quickly.
for state_id in imp_attack:
	h.states[state_id].tics = 1

h.save("fastimpattack.deh")

# Make the pistol fire really quickly.
for state_id in cacodemon_attack:
	h.states[state_id].tics = 1

h.save("fastcacoattack.deh")

# Make the pistol fire really quickly.
for state_id in baronofhell_attack:
	h.states[state_id].tics = 1

h.save("fastbaronattack.deh")

# Make the pistol fire really quickly.
for state_id in hellknight_attack:
	h.states[state_id].tics = 1

h.save("fastknightattack.deh")

# Make the pistol fire really quickly.
for state_id in lostsoul_attack:
	h.states[state_id].tics = 1

h.save("fastsoulattack.deh")

# Make the pistol fire really quickly.
for state_id in arachnotron_attack:
	h.states[state_id].tics = 1

h.save("fastarachnotronattack.deh")

# Make the pistol fire really quickly.
for state_id in cyberdemon_attack:
	h.states[state_id].tics = 1

h.save("fastcyberdemonattack.deh")

# Make the pistol fire really quickly.
for state_id in resurrector_attack:
	h.states[state_id].tics = 1

h.save("fastmothersisterattack.deh")
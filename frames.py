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

zombieman_frames = (
    deh9000.S_POSS1_STND, deh9000.S_POSS1_STND2,
    deh9000.S_POSS1_RUN1, deh9000.S_POSS1_RUN2,
    deh9000.S_POSS1_RUN3, deh9000.S_POSS1_RUN4,
    deh9000.S_POSS1_RUN5, deh9000.S_POSS1_RUN6,
    deh9000.S_POSS1_RUN7, deh9000.S_POSS1_RUN8,
    deh9000.S_POSS1_ATK1, deh9000.S_POSS1_ATK2,
    deh9000.S_POSS1_ATK3, deh9000.S_POSS1_PAIN,
    deh9000.S_POSS1_PAIN2, deh9000.S_POSS1_DIE1,
    deh9000.S_POSS1_DIE2, deh9000.S_POSS1_DIE3,
    deh9000.S_POSS1_DIE4, deh9000.S_POSS1_DIE5,
    deh9000.S_POSS1_XDIE1, deh9000.S_POSS1_XDIE2,
    deh9000.S_POSS1_XDIE3, deh9000.S_POSS1_XDIE4,
    deh9000.S_POSS1_XDIE5, deh9000.S_POSS1_XDIE6,
    deh9000.S_POSS1_XDIE7, deh9000.S_POSS1_XDIE8,
    deh9000.S_POSS1_XDIE9,
)

for state_id in zombieman_frames:
    a.states[state_id].sprite = 1
a.save("zombieman_frames.deh")

sargeant_frames = (
    deh9000.S_POSS2_STND, deh9000.S_POSS2_STND2,
    deh9000.S_POSS2_RUN1, deh9000.S_POSS2_RUN2,
    deh9000.S_POSS2_RUN3, deh9000.S_POSS2_RUN4,
    deh9000.S_POSS2_RUN5, deh9000.S_POSS2_RUN6,
    deh9000.S_POSS2_RUN7, deh9000.S_POSS2_RUN8,
    deh9000.S_POSS2_ATK1, deh9000.S_POSS2_ATK2,
    deh9000.S_POSS2_ATK3, deh9000.S_POSS2_PAIN,
    deh9000.S_POSS2_PAIN2, deh9000.S_POSS2_DIE1,
    deh9000.S_POSS2_DIE2, deh9000.S_POSS2_DIE3,
    deh9000.S_POSS2_DIE4, deh9000.S_POSS2_DIE5,
    deh9000.S_POSS2_XDIE1, deh9000.S_POSS2_XDIE2,
    deh9000.S_POSS2_XDIE3, deh9000.S_POSS2_XDIE4,
    deh9000.S_POSS2_XDIE5, deh9000.S_POSS2_XDIE6,
    deh9000.S_POSS2_XDIE7, deh9000.S_POSS2_XDIE8,
    deh9000.S_POSS2_XDIE9,
)

for state_id in sargeant_frames:
    b.states[state_id].sprite = 1
b.save("sargeant_frames.deh")

imp_frames = (
    deh9000.S_TROO_STND, deh9000.S_TROO_STND2,
    deh9000.S_TROO_RUN1, deh9000.S_TROO_RUN2,
    deh9000.S_TROO_RUN3, deh9000.S_TROO_RUN4,
    deh9000.S_TROO_RUN5, deh9000.S_TROO_RUN6,
    deh9000.S_TROO_RUN7, deh9000.S_TROO_RUN8,
    deh9000.S_TROO_MELEE1, deh9000.S_TROO_MELEE2,
    deh9000.S_TROO_MELEE3, deh9000.S_TROO_ATK1,
    deh9000.S_TROO_ATK2, deh9000.S_TROO_ATK3,
    deh9000.S_TROO_PAIN, deh9000.S_TROO_PAIN2,
    deh9000.S_TROO_DIE1, deh9000.S_TROO_DIE2,
    deh9000.S_TROO_DIE3, deh9000.S_TROO_DIE4,
    deh9000.S_TROO_DIE5, deh9000.S_TROO_XDIE1,
    deh9000.S_TROO_XDIE2, deh9000.S_TROO_XDIE3,
    deh9000.S_TROO_XDIE4, deh9000.S_TROO_XDIE5,
    deh9000.S_TROO_XDIE6, deh9000.S_TROO_XDIE7,
    deh9000.S_TROO_XDIE8,
)

for state_id in imp_frames:
    c.states[state_id].sprite = 1
c.save("imp_frames.deh")

sarg_frames = (
    deh9000.S_SARG_STND, deh9000.S_SARG_STND2,
    deh9000.S_SARG_RUN1, deh9000.S_SARG_RUN2,
    deh9000.S_SARG_RUN3, deh9000.S_SARG_RUN4,
    deh9000.S_SARG_RUN5, deh9000.S_SARG_RUN6,
    deh9000.S_SARG_RUN7, deh9000.S_SARG_RUN8,
    deh9000.S_SARG_ATK1, deh9000.S_SARG_ATK2,
    deh9000.S_SARG_ATK3, deh9000.S_SARG_PAIN1,
    deh9000.S_SARG_PAIN2, deh9000.S_SARG_DIE1,
    deh9000.S_SARG_DIE2, deh9000.S_SARG_DIE3,
    deh9000.S_SARG_DIE4, deh9000.S_SARG_DIE5,
    deh9000.S_SARG_DIE6, deh9000.S_SARG_RUN0,
    deh9000.S_SARG_ATK0, deh9000.S_SARG_PAIN0,
    deh9000.S_SARG_DIE0,
)

for state_id in sarg_frames:
    d.states[state_id].sprite = 1
d.save("sarg_frames.deh")

fat_frames = (
    deh9000.S_FATT_STND, deh9000.S_FATT_STND2,
    deh9000.S_FATT_RUN1, deh9000.S_FATT_RUN2,
    deh9000.S_FATT_RUN3, deh9000.S_FATT_RUN4,
    deh9000.S_FATT_RUN5, deh9000.S_FATT_RUN6,
    deh9000.S_SARG_RUN7, deh9000.S_SARG_RUN8,
    deh9000.S_FATT_RUN7, deh9000.S_FATT_RUN8,
    deh9000.S_FATT_RUN9, deh9000.S_FATT_RUN10,
    deh9000.S_FATT_RUN11, deh9000.S_FATT_RUN12,
    deh9000.S_FATT_ATK1, deh9000.S_FATT_ATK2,
    deh9000.S_FATT_ATK3, deh9000.S_FATT_ATK4,
    deh9000.S_FATT_ATK5, deh9000.S_FATT_ATK6,
    deh9000.S_FATT_ATK7, deh9000.S_FATT_PAIN,
    deh9000.S_FATT_PAIN2, deh9000.S_FATT_DIE1,
    deh9000.S_FATT_DIE2, deh9000.S_FATT_DIE3,
    deh9000.S_FATT_DIE4, deh9000.S_FATT_DIE5,
    deh9000.S_FATT_DIE6,
)

for state_id in fat_frames:
    e.states[state_id].sprite = 1
e.save("fat_frames.deh")

head_frames = (
    deh9000.S_HEAD_STND, deh9000.S_HEAD_STND2,
    deh9000.S_HEAD_STND3, deh9000.S_HEAD_STND4,
    deh9000.S_HEAD_RUN1, deh9000.S_HEAD_RUN2,
    deh9000.S_HEAD_RUN3, deh9000.S_HEAD_RUN4,
    deh9000.S_HEAD_RUN5, deh9000.S_HEAD_RUN6,
    deh9000.S_HEAD_RUN7, deh9000.S_HEAD_RUN8,
    deh9000.S_HEAD_ATK1, deh9000.S_HEAD_ATK2,
    deh9000.S_HEAD_ATK3, deh9000.S_HEAD_ATK4,
    deh9000.S_HEAD_PAIN, deh9000.S_HEAD_PAIN2,
    deh9000.S_HEAD_PAIN3, deh9000.S_HEAD_DIE1,
    deh9000.S_HEAD_DIE2, deh9000.S_HEAD_DIE3,
    deh9000.S_HEAD_DIE4, deh9000.S_HEAD_DIE5,
    deh9000.S_HEAD_DIE6,
)

for state_id in head_frames:
    f.states[state_id].sprite = 1
f.save("head_frames.deh")

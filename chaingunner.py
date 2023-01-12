import deh9000
from deh9000 import *

a = deh9000.DehackedFile()

chaingunner_attack = (
	deh9000.S_CPOS_ATK1, deh9000.S_CPOS_ATK2,
	deh9000.S_CPOS_ATK3, deh9000.S_CPOS_ATK4,
)

# Make the pistol fire really quickly.
for state_id in chaingunner_attack:
	a.states[state_id].tics = 1
	a.states[state_id].sprite = deh9000.S_BSPI_ATK1

a.save("fastchaingunnerattack.deh")

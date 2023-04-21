"""Doom's internal action functions.

Action functions, also known as "code pointers", are callback functions that
are associated with particular frames and invoked when a thing reaches that
particular frame.

  <https://doomwiki.org/wiki/DeHackEd#Code_pointers>
"""

class Action():
	"""Represents a callback function used to perform a particular action.

	In dehacked these are called "code pointers".
	"""
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name


A_WeaponReady = Action("A_WeaponReady")
A_ChainSawReady = Action("A_ChainSawReady")
A_Lower = Action("A_Lower")
A_Raise = Action("A_Raise")
A_Punch = Action("A_Punch")
A_ReFire = Action("A_ReFire")
A_FirePistol = Action("A_FirePistol")
A_FireShotgun = Action("A_FireShotgun")
A_FireShotgun2 = Action("A_FireShotgun2")
A_CheckReload = Action("A_CheckReload")
A_LoadShotgun2 = Action("A_LoadShotgun2")
A_CloseShotgun2 = Action("A_CloseShotgun2")
A_FireCGun = Action("A_FireCGun")
A_GunFlash = Action("A_GunFlash")
A_FireMissile = Action("A_FireMissile")
A_Saw = Action("A_Saw")
A_FirePlasma = Action("A_FirePlasma")
A_PlasmaAnimate = Action("A_PlasmaAnimate")
A_BFGsound = Action("A_BFGsound")
A_FireBFG = Action("A_FireBFG")
A_BFGSpray = Action("A_BFGSpray")
A_BFGFlash = Action("A_BFGFlash")
A_Explode = Action("A_Explode")
A_Pain = Action("A_Pain")
A_PlayerScream = Action("A_PlayerScream")
A_Fall = Action("A_Fall")
A_XScream = Action("A_XScream")
A_Look = Action("A_Look")
A_Chase = Action("A_Chase")
A_FaceTarget = Action("A_FaceTarget")
A_PosAttack = Action("A_PosAttack")
A_Scream = Action("A_Scream")
A_SPosAttack = Action("A_SPosAttack")
A_Tracer = Action("A_Tracer")
A_FatRaise = Action("A_FatRaise")
A_FatAttack1 = Action("A_FatAttack1")
A_FatAttack2 = Action("A_FatAttack2")
A_FatAttack3 = Action("A_FatAttack3")
A_TroopAttack = Action("A_TroopAttack")
A_TroopMelee = Action("A_TroopMelee")
A_SargAttack = Action("A_SargAttack")
A_HeadAttack = Action("A_HeadAttack")
A_BruisAttack = Action("A_BruisAttack")
A_SkullAttack = Action("A_SkullAttack")
A_Metal = Action("A_Metal")
A_SpidRefire = Action("A_SpidRefire")
A_BabyMetal = Action("A_BabyMetal")
A_BspiAttack = Action("A_BspiAttack")
A_Hoof = Action("A_Hoof")
A_CyberAttack = Action("A_CyberAttack")
A_PainAttack = Action("A_PainAttack")
A_PainDie = Action("A_PainDie")
A_SpawnSmoke = Action("A_SpawnSmoke")
A_FadeAlpha = Action("A_FadeAlpha")
A_FireLaser = Action("A_FireLaser")
A_OnDeathTrigger = Action("A_OnDeathTrigger")
A_BarrelExplode = Action("A_BarrelExplode")
A_TargetCamera = Action("A_TargetCamera")
A_BspiFaceTarget = Action("A_BspiFaceTarget")
A_PlayAttack = Action("A_PlayAttack")
A_RectChase = Action("A_RectChase")
A_RectMissile = Action("A_RectMissile")
A_RectGroundFire = Action("A_RectGroundFire")
A_MoveGroundFire = Action("A_MoveGroundFire")
A_RectTracer = Action("A_RectTracer")
A_PainDeathEvent = Action("A_PainDeathEvent")
A_CyberDeathEvent = Action("A_CyberDeathEvent")
A_RectDeathEvent = Action("A_RectDeathEvent")
A_FadeOut = Action("A_FadeOut")
A_FadeIn = Action("A_FadeIn")
A_SkullSetAlpha = Action("A_SkullSetAlpha")
A_MissileSetAlpha = Action("A_MissileSetAlpha")
A_CPosAttack = Action("A_CPosAttack")
A_CPosRefire = Action("A_CPosRefire")
A_SkelWhoosh = Action("A_SkelWhoosh")
A_SkelFist = Action("A_SkelFist")
A_SkelAttack = Action("A_SkelAttack")
A_SpidAttack = Action("A_SpidAttack")
A_SpidDeathEvent = Action("A_SpidDeathEvent")
A_Fire = Action("A_Fire")
A_StartFire = Action("A_StartFire")
A_FireCrackle = Action("A_FireCrackle")
A_VileChase = Action("A_VileChase")
A_VileStart = Action("A_VileStart")
A_VileTarget = Action("A_VileTarget")
A_VileAttack = Action("A_VileAttack")

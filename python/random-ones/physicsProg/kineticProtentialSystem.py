'''
Handles the kinetic, and potential systems class, base problems only
'''


class kinPotSys(object):
    def __init__(self):
        self.kEnergy = None  # 1/2 Mass * Velocity**2
        self.kMass = None
        self.kVelocity = None  #

        self.pEnergy = None
        self.pMass = None
        self.pAcceleration = None
        self.pDisplacement = None

        self.kSpringConstant = None
        self.potKSpringEnergy = None
        self.potKSpringDisplacement = None
        self.potKSpringMass = None
        self.kinKSpringEnergy = None
        self.kinKSpringDisplacement = None
        self.kinKSpringVelocity = None
        self.kinKSpringMass = None

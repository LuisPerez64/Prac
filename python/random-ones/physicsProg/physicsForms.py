'''
A bunch of physics formulas, and their counterparts.
Prints out the formula for the needed problem, and goes from there.
'''

'''
Attains the initial velocities, and things of the sort, and finds the final
'''


def sqrt(inpt):
    return inpt ** .5


def elasticMom(massOne=None, velOne=None, massTwo=None, velTwo=None):
    first = (2 * massTwo * velTwo) / (massOne + massTwo)
    second = ((massOne - massTwo) / (massOne + massTwo)) * velOne
    return first + second


def inelasticMom(massOne=None, velOne=None, massTwo=None, velTwo=None):
    return ((massOne * velOne) + (massTwo * velTwo)) / (massOne + massTwo)


'''
make each subfunctionality its own class, this will cut down on the need
to have things pop up in their own functional focus point.
'''


def basePotentialEnergy(mass=None, height=None, accel=None, potEnergy=None):
    if (accel == 'g'):
        accel = 9.8

    return mass * accel * height


def baseKineticEnergy(mass=None, velocity=None, kineticEnergy=None):
    return .5 * mass * velocity ** 2


def findHeightInKineticPotentialSystem(velocity=None, accel=None):
    if accel == None:
        accel = 9.8
    return velocity ** 2 / (accel * 2)

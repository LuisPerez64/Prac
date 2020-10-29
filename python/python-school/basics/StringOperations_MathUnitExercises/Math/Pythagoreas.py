'''
Given at least two measurements. Analyze the lengths of the given triangle.
Works for a right triangle, with at least two measurements.
Formula(Read through the code base.)
Formula(SOHCAHTOA):Sin(Opp/Hyp) | Cos(Adj/Hyp) | Tan(Opp/Adj)
Did not want to over complicate things more than needed.. Already more than I wanted.
'''
from math import *


def main():
    print("We're given at least 2 points. Please input them when they arise. Else enter")
    inpVals = ['Theta', 'Opposite', 'Hypotenuse', 'Adjacent']
    print('Please input the values that you know. Else press enter')
    inps = [_float(input('Input {0}: '.format(x))) for x in inpVals]
    if not inps[0]:
        PYT(inps)
    elif inps[1]:
        TOA(inps)
    elif inps[2]:
        SOH(inps)
    elif inps[3]:
        CAH(inps)

    printOut(inpVals, inps)


# Tries to place afloating value in the given area, else places 0
def _float(inpVal):
    try:
        outVal = float(inpVal)
    except ValueError:
        outVal = 0
    return outVal


# Simple Print Function, should use a map but not yet.
def printOut(vals, inp):
    print("\nPrinting out metrics\n")
    for i in range(len(vals)):
        print('{0} came out to be {1}'.format(vals[i], inp[i]))


# Given Hypotenuse, attain Sin(theta) -> attain Opposite -> attain Adjacent
def SOH(inps):
    theta = sin(radians(inps[0]))
    inps[1] = theta * inps[2]
    inps[3] = sqrt(inps[2] ** 2 + inps[1] ** 2)


# Given Adjacent, attain Cos(theta) -> attain Hypotenuse -> attain Opposite
def CAH(theta, inps):
    theta = cos(radians(inps[0]))
    inps[2] = theta * inps[3]
    inps[1] = sqrt(inps[2] ** 2 + inps[3] ** 2)


# Given Opposite, attain Tan(theta) -> attain Adjacent -> attain Hypotenuse
def TOA(theta, inps):
    theta = tan(radians(inps[0]))
    inps[3] = theta * inps[1]
    inps[2] = sqrt(inps[3] ** 2 + inps[1] ** 2)


# Given two sides, use good old Pythagoreans Theorem (a^2=b^2+c^2)
def PYT(inps):
    sides = inps[1:]
    pass


if __name__ == '__main__':
    main()

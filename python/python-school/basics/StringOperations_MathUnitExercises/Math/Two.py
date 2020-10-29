'''
Volume of a Cylinder calculations.
Given Diameter ~ r*2
Formula(Diameter of Circle): radius * 2
Formula(Volume of a Cylinder): pi*r^2*h (Area of a Base * Height)
'''
from math import pi

diam = float(input("What's the diameter of the cylinder: "))
height = float(input("How high is it from it's base to the top: "))

print("""
With a diamater of {0} giving a radius of {1}
The volume of the given cylinder would be {2}
""".format(diam, round(diam / 2, 2), round(pi * (diam / 2) ** 2 * height, 2)))

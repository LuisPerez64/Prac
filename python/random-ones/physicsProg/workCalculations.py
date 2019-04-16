import math as m
def basicWork(force, displacement, angle):
    radians = angle * m.pi / 180
    angle = m.cos(radians)
    return force * displacement * angle


    

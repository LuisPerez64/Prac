'''
Calculation for the cirumference of a circle, and area of a circle.
Formula(Circumference of a Circle): 2*pi*r 
Formula(Area of a Circle): pi*r^2
'''
import math
rads=(float(input('Whats the radius of the circle we\'re dealing with: ')))
      
print('''
Solving for the area and circumference with {0} radians.
Applying formula for Circumference at (2*pi*r) gives {1}
Applying formula for Area with pi*r^2 gives {2}
'''.format(rads,round(rads*math.pi*2,2),round(rads*math.pi**2,2))) 

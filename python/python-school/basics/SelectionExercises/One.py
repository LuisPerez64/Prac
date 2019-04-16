'''
Basic mathematic implementation of Area of a cuboid.
'''
dimMeasures=('width','height','depth')
print('Please input the dimensions of the Lift. In feet.')
inpLift=[int(input('{0}: '.format(x))) for x in dimMeasures]

print('Please input the dimensions of the Fridge. In feet.')
inpFridge=[int(input('{0}: '.format(x))) for x in dimMeasures]

toggle=False
dimLift,dimFridge=(1,1)
for x in range(3):
    if inpFridge[x] > inpLift[x]:
        print('The fridge will not fit due to {0} '.format(dimMeasures[x]))
        toggle=True
    dimLift*=inpLift[x]
    dimFridge*=inpFridge[x]
    
if not toggle:
    print('The space that will be left based on the dimensions given would be {0} feet'.format(dimLift-dimFridge))

inpList=[]
while True:
    inpList.append(float(input('Please input a number (0) to exit: ')))
    if inpList[-1] == 0:
        break

print('Total value of the numbers input: {0}'.format(sum(inpList)))

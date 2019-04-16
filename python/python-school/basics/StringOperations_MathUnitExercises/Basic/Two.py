print('Please input 3 integers.')
inpList=[ int(input('Input number {0}: '.format(x+1))) for x in range(3) ]
print('If you multiply {0} and {1} and divide them by {2} you get {3}'.format(str(inpList[0]),str(inpList[1]),str(inpList[2]),str(inpList[0]*inpList[1]/inpList[2])))

'''
Another iteration of the isPrime function,
Finding the 10001'st prime number
Added functionality to the isPrime function as well.
'''
###
def isPrime(inputNum, primesList):
    retVal = False
    for indexNum in primesList:
        if inputNum % indexNum == 0:
            break
        if indexNum * indexNum > inputNum:
            retVal = True
            break

    return retVal
##

primesList = [2,3,5] #Initial prime points to test against
primeIndex = len(primesList)
upperLimit = input('Which prime are you seeking: ')
testVal = 7

while(True):
    if isPrime(testVal, primesList):
        primeIndex += 1
        primesList.extend([testVal])
        if primeIndex == upperLimit:
            break
    testVal += 2

#print primesList
print testVal

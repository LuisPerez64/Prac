"""
Finds the largest prime factor of a given number.
An excercise in building the is prime function, without memoization again.
Going to need to employ this principle sooner than later.
"""
def isPrime(inputNum, x): # Takes in a list, and checks primeness against that
    returnValue = True
    for listIndex in x:
        if listIndex*listIndex <= inputNum:
            if inputNum % listIndex == 0:
                returnValue = False
        else: 
            break
    return returnValue

'''
    for i in range(int(math.sqrt(inputNum)) + 1):
        print i
        for j in range(3, int(math.sqrt(inputNum)) + 1):
             if i % j == 0:
                 return False
  
    return True
'''
x = [2,3,5] # holds the primes that have been found so far, my stage of memoize

#Split this off into it's own thread with multithreading, getting it 
#updated as the main program runs in the background?

#Usage of a list, and a for loop
'''
for i in range(7, 10**6):#Fill the list with the needed primes
    if isPrime(i, x) == True:
        x.extend([i])

'''
#Using a while loop, no list initialization
count = 7
while True:
    if count > 10**6:
        break
    if isPrime(count, x):
        x.extend([count])
    count += 2

inputNum = input('Input Value to be tested against: ')

#Test the values in the list from the last value to the first, cuts down time.
for i in reversed(x):
    if inputNum % i == 0:
        print i #largest value that divides inputNum is here
        break


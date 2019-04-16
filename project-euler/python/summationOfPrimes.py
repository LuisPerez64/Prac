#!/usr/bin/env python
'''
Finding the sum of all the primes below a given index point.

Another time writing the isprime function through.
Rewriting it every time to see if I find some new manner of doing it.
'''
###
def isPrime(testVal, setOfPrimes):
    retVal = False
    for index in setOfPrimes:
        if index * index > testVal:
            retVal =True
            break
        if testVal % index == 0:
            break
    return retVal
##

primesList = [2] #List with most base prime, primes added to it when found
primesCounter = 3 #Intial value of the prime funct
sumOfPrimes = 2
while primesCounter <= 2 * 10**6:
    if isPrime(primesCounter, primesList):
        primesList.extend([primesCounter]) #Is prime, add it to the list
        sumOfPrimes += primesCounter
    primesCounter += 2 #Only one even prime so no need to check them all

'''
#If the sum is wanted to be done in an external function, from the genral function above.
for i in primesList:    
    sumOfPrimes += i
'''
print sumOfPrimes

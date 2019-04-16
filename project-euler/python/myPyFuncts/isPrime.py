'''
Finds the prime number that is being asked of it, uses a list to keep track of 
the primes that it has found so far to help it find the needed prime number.
'''
###
'''
This is the function that will actively check if a given valued number is prime
or not. 
@Params:
  TestVal: The value to be evaluated by the isPrimeTest
  setOfPrimes: A list containing all the prime values that have been found so
   far.

'''
def isPrimeTest(testVal, setOfPrimes):
    retVal = False #Try ot prove me wrong
    for index in setOfPrimes: #Iterates through the list of primes 
        if index * index > testVal: #If the square of the prime is > testVal
            retVal =True #This means that the testValue has to be prime
            break
        if testVal % index == 0: #The number was divisible by a prime. !prime
            break
    return retVal
##

### Populate the list as soon as the isPrime Module is imported
'''
isPrimeHelp: The populate primesList function
The only function that is able to mutate the Primes list

@Params:
  lowBound: The last value in the primes list if called after the initial call
    3, on the first run around, to populate the list
  highBound: The value that is being validated for primeness after initial call
    2**19 on the first run around, to populate the list
@Returns:
  If number is not prime, False
  Else True
'''
Primes = [2] #This is the list of all the primes that have been found so far.
def isPrimeHelp(lowBound, highBound):
#Don't test any even numbers, not worth it, populate the list when needed.    
    if highBound % 2 == 0: return False
    primesIndex = lowBound #Assign the first value to test
    while primesIndex <= highBound: #Test until the testValue is met
        if isPrimeTest(primesIndex, Primes): #Is prime add it to the list
            Primes.extend([primesIndex]) 
        primesIndex +=2
    if highBound in Primes: #If the value is in the list is prime
        return True
    return False

isPrimeHelp(3, 2**19-1) #Populate the list with primes under 512K

def isPrime(inputValue):
    retVal = False
    if inputValue in Primes:
        retVal = True
    elif inputValue < Primes[len(Primes) -1]:
        retVal = False
    else: 
        retVal = isPrimeHelp(Primes[len(Primes) - 1], inputValue)
    return retVal

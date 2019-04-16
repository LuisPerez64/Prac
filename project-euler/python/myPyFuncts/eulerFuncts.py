###############################################################################
########################### Discrete Functions ################################
###############################################################################
'''
The factorial Function: n! = n*(n-1)*(n-2)*...*n*(n-1)*1
Self explanatory to a point.
'''
def factorial(inputNum):
    retVal = 1
    while inputNum > 1: 
        retVal *= inputNum 
        inputNum -= 1
    return retVal

'''
Basic Combinatorics function
N Choose K
N elements in a set, the different manners of choosing K elts from the set
Formula N!/(K!*(N-K)!)
'''
def nChooseK(n,k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n-k)
    return numerator / denominator

'''
The fibonacci sequence. 
f(n) = f(n-1) + f(n-2). Returns the N'th fibonacci number in the sequence
Break cases are f(1) and f(0) at which point the fib sequence == 1
'''
def fibonacci(inputValue):
    #Linear algebra approximation of the fibonacci function.
    fib = (( ((1 + 5**.5) ** inputValue - (1 - 5**.5) ** inputValue)) / 
           (2 ** inputValue * 5**.5))
    return int(fib);

'''
#Compounding f(1) and f(2) == 1, comp sci indices.
    if inputValue == 0 or inputValue == 1:
        return 1
#Recursively call itself with the needed indices until the above cond is met.
    return fibonacci(inputValue -1) + fibonacci(inputValue -2)
'''


###############################################################################
################################ IsPrimeFunct #################################
###############################################################################
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

###############################################################################
###################### Manners of reading in a file ###########################
###############################################################################
'''
Manners of reading in a given file, and placing it into a given object
New Keyword: with | Syntax:
   with open('filename') as varName:
    Opens a file, gives it the var name, allows operations to be done on it
    closes the file right after. Can open as many files are as needed in that 
    scope. with ..., ..., ...: (... = open('...') as var)
New Keyword: open | Syntax:
   open("FileName", Arguments("r"=read,"w"=write,"a"=append, addable(+,b,b+))
     Self explanatory syntax, opens the file for whatever operation is wanted
     +  = read/ write||append
     b  = binary file operations
     b+ = binary read/write||append

First implementation: Write the files contents to a list, including newLine
'''

###
'''
First implementation of the readIn function
@Params:
  fileName: The given file to be opened, and read in

@Returns:
  returnedList: This is the list with all the read in values, inclusive of the
   newLine for this implementation.
'''
def readInFileToList(fileName):
    returnedList = []
    with open(fileName) as inFile:
        returnedList = inFile.readlines()
    return returnedList

'''
Builds on the function above.
Added functionality:
  Removes new lines from the given list objects.
'''
def readInFileToListNoNewLines(fileName):
    noNewLineList = readInFileToList(fileName)
#Strip the newlines from the list in itself. Basic point since they're strings
    noNewLineList = [x.strip('\n') for x in noNewLineList]
    return noNewLineList

'''
Builds again on the function above.
Added functionality:
  Converts every elt in the file into an integer instead of a string.
'''
def readInFileOfNumbers(fileName):
    arrayOfNums = readInFileToListNoNewLines(fileName)
#Convert the strings to intgers, one variable at a time. 
    arrayOfNums = [int(x) for x in arrayOfNums]
    return arrayOfNums

###############################################################################
########################### Array Manipulation ################################
###############################################################################
'''
Functions that when used, remove duplicates from a given list, making the list
hold only one of any given elt. If it can be optimized, will do so in the
future. So far only works on 1 dimensional lists.
'''
def remDup(inputList):
    newList = [] #List to be returned to the caller function.
    for inputListIndex in inputList:
        if inputListIndex not in newList:
            newList.extend([inputListIndex])
    return newList

'''
Added functionality sorts the list that holds no duplicates.
'''
def remDupSort(inputList):
    sortedList = remDup(inputList)
    sortedList.sort() #Sort the list
    return sortedList

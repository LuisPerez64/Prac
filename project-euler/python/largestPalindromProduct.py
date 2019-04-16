'''
Is fed a sequene of numbers, checks to see if the number that it is given is a 
palindrome. 
String manipulation more or less for this is the main point that is being 
pushed forward.
'''

def isPalindrome(inputString):
    test = len(inputString) # Establish this as the baseline
    retVal = False 
    if test <= 1: # If this is met then the string is a palindrome
        retVal = True
    elif inputString[test-1] == inputString[0]: # Checks if the ends match
        retVal = isPalindrome(inputString[1:(test-1)]) #test substr of non-edge
    
    return retVal

#Established the difference between input and raw_input. 
#Raw input does no conversions, input takes in what is given and treats it as 
#a line being added to the script directly, not a string.
#ints = input('Type it in: ')

lastPalProd = 0
#Find all palindromes within the given range of multiples.
for i in range(100, 1000):
    for j in range(100, 1000):
        testVal = i *j 
        if isPalindrome(str(testVal)):
            if testVal > lastPalProd:
                lastPalProd = testVal

print lastPalProd

'''
Find the longest Collatz Sequence Chain that could be made with a value that is
not above a given range.
ie. If User inputs 10, only checks collatz sequences below ten.
'''
###
'''
Collatz Sequence terms:

@Params:
  testVal:The value to be checked against the collatz Conjecture
  dictOfVars: The dictionary with the entries so far in the list.
 
@Returns:
  The steps taken to reach 1 in the given collatz sequence
  The dictionary with a new key/value for the length of the sequence at test.
'''
'''
Bug 1: The dictionary would double count a lot of the values since it was 
 pushing in the initial size of 1 everytime a value pair was found, and doing 
 so twice, and every value after that incrementing as well. Simple concept
 simple fix, remove the incremented point from the dictionary. 1 and two will
 not invalidate since they are not found as of yet.
'''
def collatzSequence(testVal, dictOfVars):
   size = 1
   tempTest = testVal
   while testVal != 1:
      if testVal in dictOfVars: #Found the key in the keyvalue pair
#Add the found size of the collatz at test. The minus one to account for the
         size += dictOfVars[testVal] -1 #Original input, no double count.
         break #Break out of the loop.
      if testVal % 2 == 0:
         testVal /= 2
      else:
         testVal = testVal * 3 + 1
      size += 1

   dictOfVars[tempTest] = size #Add the value pair to the dictionary itself.
   return size

inpt = 1
terms = 0
#Keys the given testValu number. Values: Steps to one from that number.
dictOfVars = dict() #Initialize the empty dictionary.
while inpt <= 10**6:
    newVal = collatzSequence(inpt, dictOfVars)
    if newVal > terms:
        largestVal = inpt
        terms = newVal
    inpt += 1

print(largestVal, terms)

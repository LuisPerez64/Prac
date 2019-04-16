"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000, or a given number.
"""
## Marks delineating functions, will not be needed too much later on.
def multiplesOf(inputRange):
    sumTotal = 0 # The total sum of all the valid integers matching the reqs.
    count = 0
    while count <= inputRange: # basic for loop for(i = 0; i < j; ++i)
        if count % 5 == 0 or count % 3 == 0:
            sumTotal += i 

    return sumTotal
##
inputRange =10**3 #input('Please input the number for high limit of range: ')

print('Total value for max ' + str(inputRange) +' is '+
      str(multiplesOf(inputRange)))

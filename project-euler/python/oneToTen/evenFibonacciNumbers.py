"""
Denotes and finds the even valued fibonacci sequence numbers.
An excercise in list manipulation mainly. 
Also first time writing the beautiful fibonacci sequence in python
Could do the fibonacci within my own while loop construct, adding the values
up instead of calling the function everytime, but not yet sure of how to.
"""

###
"""
A rather ineffecient manner of doing the fibonacci calculations.
Not too keen on list operations at this point, and memoization is in itself 
pretty new to me. So doing it the good old, old way.
"""
def fibIneffective(inputValue):
    if(inputValue == 1 or inputValue == 0):
        return 1
    return(fibIneffective(inputValue -2) + fibIneffective(inputValue - 1))
##

###
"""
Is given the max value that could be added, should it be an even valued number.
Proceeds to run the fibonacci finder, written above, and checking if the values
that are returned are even. Breaks if the sumTotal is ever greater than max
"""
def evenFibsSum(inputMax):
    sumTotal = 0
    counter = 0
    while True: # Implementing with a while loop, practice.
        testValue = fibIneffective(counter)
        if(testValue > inputMax): # The break condition
            return sumTotal # The next value coming in is too larger, break
        if testValue % 2 == 0:
            sumTotal += testValue
        counter += 1
##


# I can't believe it allows you to input calculations as input.
inputMax = input('Max boundary for function even fibs: ')

print 'For the given range of ' + str(inputMax) + ' sum of even fibs is:'
print evenFibsSum(inputMax)



###
"""
Attained this solution from theProject Euler site after the fact.
Holy mother of everything it's so much more efficient, but using mathematical
principles that I do not yet fully understand. Also not recursively calling
the given function pointsto a much more efficient solution than the one that 
I have written. 
"""
def calcE():
    x = y = 1
    sum = 0
    while (sum < 1000000):
        sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum
##

'''
Problem 21:
Let d(n) be defined as the sum of proper divisiors of n(numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, and a != b, then a and b
are an amicable pair and each of a and b are called amicable numbers.
For example the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,110; 
therefore d(220) = 284. The proper divisors of 284 are 1,2,4,71,142; so
d(284) = 220.
Spec:
 Evaluate the sum of all the amicable numbers under 10000.
'''

def factors(inputNum):
    testAgainst = inputNum // 2 # Get the floor of the division point.
    sum = 0
    while testAgainst > 0:
        if inputNum % testAgainst == 0:
            sum += testAgainst
        testAgainst -= 1
    return sum

testNums = range(1,10001) 
dontTest = [] #So as not to test multiple values
amicableNums = [] #The amicable values


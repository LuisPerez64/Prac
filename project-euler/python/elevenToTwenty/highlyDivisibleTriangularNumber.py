'''
Triangular number: The sequenceattained by adding given natural numbers. ie
1+2+3+4+5 == 5thTriNum == 15, and so forth.
Divisors of 15: 15, 5, 3, 1
Purpose: find the first Tri number to be able to be evenly divided by 500 other
integers total.
'''

'''
The formula for the triangular number at any given index is N * (N + 1) / 2

@Param: 
  indexedTri: The triangular number to be found at a given index
@Returns:
  The triangular number at the given index
Implanted this function directly to see if it could increase speed, leaving for
description
'''
def triangularAtIndex(indexedTri):
    return indexedTri * (indexedTri + 1) / 2

'''
Attains the divisors of a given number, including itself as one of the possible
values that divide it out.

@Params: 
  inputNum: The triangular number to find the divisors for
@Returns:
  The amount of numbers that evenly divide the given triangular number

Added a mathematical principle to this to make it, exponentially, faster.
Attained from the overview:
  For every exact divisor, x % y == 0, up to the square root, there is a 
  corresponding divisor above the square root.
  ie: divisors of 12: sqrt(12) == 3.464
    Below 3.46, 1,2,3 || Above 3.46, 4,6,12
  Always yielding an even number of divisors.
  This principle applies to every integer iff it's not an evenly square number
  ie: divisors of 64: sqrt(64) == 8
    Below 8, 1,2,4,8 || Above 8, 8,16,32,64
  Because of this double count of the value 8, one must be taken off so
  This would always yield an uneven number of divisors.

There exist a much more efficient solution than the one that I have provided,
 but to use it, and call it my own at this time wouldbe a far stretch.The
 overview points that I employed werejust a minor tweak. Don't have too strong
 of a mathematical background, so the other concept I can only narrowly explain
'''
def howManyDivisors(inputNum):
    totalDivisors = 0
    divideBy = 1 

    while divideBy * divideBy <= inputNum: 
        if inputNum % divideBy == 0:
# For every divisor up to sqrt(x) there exists a complimentary one past sqrt(x)
            totalDivisors += 2
            
        divideBy += 1
    if inputNum == (divideBy-1)**2: # Takes into account the last added divisor
        totalDivisors -=1 # inputNum is a square number decrement totalDivs
    return totalDivisors


findFirstOccurenceOf = input('How many divisors are you seeking: ')
index = 1
divisors = 0
while divisors < findFirstOccurenceOf:
    triangularNum = index * (index+1) / 2 # Replacing the function call 
    divisors = howManyDivisors(triangularNum)
    index +=1

# It kind of irks me that the variable does not just exist in the given scope.
print triangularNum

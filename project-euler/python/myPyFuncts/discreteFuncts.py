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

'''
def nChooseK(n,k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n-k)
    return numerator / denominator

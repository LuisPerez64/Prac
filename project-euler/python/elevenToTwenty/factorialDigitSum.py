'''
Problem 20:
n! means n*(n-1)*...*3*2
For example, 10! = 10 * 9 * ... * 3 * 2 = 3628800
and the sum of the digits in the number 10! is 3+6+2+8+8 = 27
Find the sum of the digits in the number 100!
'''
def factorial(inputVal):
    product = 1
    while(inputVal > 1):
        product *= inputVal
        inputVal -= 1
    return product

inputVal = factorial(100)

sumOfVals = 0
for i in str(inputVal):
    sumOfVals += int(i)

print(sumOfVals)

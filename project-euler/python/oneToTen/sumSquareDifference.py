'''
Attains the difference between the sum of squaresof a sequence, and the square
of the sum of the same rangeof numbers.
'''
inputNum = input('Max range point: ')
listInp = range(inputNum + 1)
sumOfSquares = 0
squareOfSum = 0

for i in listInp:
    sumOfSquares += i*i

for j in listInp:
    squareOfSum += j

squareOfSum **=2
sumSquareDiff = squareOfSum - sumOfSquares 

print sumSquareDiff

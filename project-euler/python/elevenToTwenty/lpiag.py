#Need these dependencies
from eulerFuncts import readInFileToListNoNewLines
'''
Is fed a group of numbers, most likely in the form of a grid, and finds the 
largest product of a given length of arguments that is passed to the given 
list. Attains the index of the values as well, and logs them, Added funct.
Python 3 points from now on.
'''

'''
Setting up three different functions:
 One for the values that are maxed at the straight read, left to right.
 One for the values going down in the matrix at a given point.
 One for the values going diagonally to the left of a given point.
 One for the values going diagonally to the right of a given point.

This will be gotten and the max value, should it be met, will be updated at 
 each of the function call intervals.

Do all the operations as long as they will not reach to an external point in 
 the given array. Do the operations at each point, (0,0) check all the values
 (0,1)...(0,n) Then go down a rown (1,0)...(m,n), Basically (0,0)...(m,n)
 n = biggest y index
 m = biggest x index
'''
'''
Function: Convert To Grid of Ints

@Params:
  inputMatrix: The 'matrix' of strings to be converted to a matrix of ints
  lengthOfNumers: Assumes that the list is well ordered with a set range of 
    numbers. ie, 0-9, 00-99, 000-999 ... n-m. For this implementation anything
    else would break this.
Somewhat well documented, messy since I don't fully grasp pythons indentation 
  points as of yet, and how they can affect the flow of the program itself.
'''
def convertToGridOfInts(inputMatrix, lengthOfNums):
    returnMatrix = []
    for i in range(len(inputMatrix)):
#Appends a new list to the old list. Extend does not work in this instance
          returnMatrix.append([])
#Initialize the needed variables, to the points that are needed to be inited.
          startIndex = 0
          endIndex = lengthOfNums
          while True:
#Add in all the elements in the given list, from the list of strings.
#Attains the string at the [i:j] substr and convert them to ints.
              returnMatrix[i].extend(
                  [int(inputMatrix[i][startIndex:endIndex])])
              if endIndex >= len(inputMatrix[0]):
                  break
#Keep things within the length of each string construct[startRead:endRead]
              startIndex = endIndex
              endIndex += lengthOfNums
    return returnMatrix
'''
The four functions for reading, and adjusting the matrix.
@Params:
  readLen: The amount to be traversed by the counter
  index: A vector(list[x,y]) containing the index to do the check from
  inputMatrix: The matrix to be acted upon.

@Returns:
  The calculated product of that traversal path, from the given index point.
  May revamp and just make it do the traversal total for each type.

All of these functions do bound checking within themselves, and run forward 
  accordingly.
'''
def findMaxDown(inputMatrix, index, readLen):
    if index[0] + readLen > (len(inputMatrix)-1): #Index of the X-Axis 
        return 0
   
    retTotal = 1
    while readLen > 0:
        retTotal *= inputMatrix[index[0]][index[1]+readLen]
        readLen -= 1
    return retTotal
        
def findMaxRight(inputMatrix, index, readLen):
    if index[0] + readLen > len(inputMatrix[0])-1:
        return 0
    
    retTotal = 1

    return retTotal
def findMaxDiagRight(inputMatrix, index, readLen):
    if(index[0] + readLen > len(inputMatrix[0])-1 or
       index[1] + readLen > len(inputMatrix))-1:
        return 0
    
    retTotal = 1


def findMaxDiagLeft(inputMatrix, index, readLen):
    if(index[0] - readLen < 0 or
       index[1] - readLen < 0):
        return 0
    
    retTotal = 1


##Read in the file, not doing any grid operations on it as of yet.
gridOfNums = readInFileToListNoNewLines("largestProductInAGrid.txt")
gridOfNums = convertToGridOfInts(gridOfNums, 3)
traverseThisMuch = 4
index = [0,0]
maxValues = [0 for i in range(4)] #Holds the valvulated max values in the lists
for i in range(len(gridOfNums)): #X Index
    for j in range(len(gridOfNums[i])): #Y Index
        index[0], index[1] = i, j #Assign the read index point
        print(index)
        newDown = findMaxDown(gridOfNums, index, traverseThisMuch)
        if newDown > maxValues[0]:
            maxValues[0] = newDown
        newRight = findMaxRight(gridOfNums,index,traverseThisMuch)
        if newRight > maxValues[1]:
            maxValues[1] = newRight
        newLeftDiag = findMaxDiagLeft(gridOfNums, index, traverseThisMuch)
        if newLeftDiag > maxValues[2]:
            maxValues[2] = newLeftDiag
        newRightDiag = findMaxDiagRight(gridOfNums, index, traverseThisMuch)
        if newRightDiag > maxValues[3]:
            maxValues[3] = newRightDiag


print(maxValues)

#Matrix multiplication. [0,0] ~ [m,n]
class matrix(object):
    def __init__(self): #Populate the matrix, first point
        self.rows = int(input('How many rows in this: '))
        self.cols = int(input('How many colums in this: '))
        self._matrix =[[0 for i in range(self.cols)] for j in range(self.rows)]
        self.populateEmptyMatrix()
#Populate the matrix, can be called standalone, is called on init.
    def populateEmptyMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print('Entry['+str(i)+','+str(j)+']: ',end="")
                self._matrix[i][j] = int(input(''))
#Change a value in the given matrix, mutator function
    def changeValue(self, iIndex, jIndex):
        if jIndex < self.cols and iIndex < self.rows:
            self._matrix[iIndex][jIndex] = int(input('New Value: '))
        else:
            if iIndex >= self.rows:
                print(iIndex,' is out of range for rows.')
            if jIndex >= self.cols:
                print(jIndex,' is out of range for cols.')
        return
#Self explanatory print out the given matrix.        
    def printMatrix(self):
        for i in range(self.rows):
            print(self._matrix[i])

#Helper functions for the matrix algebra points.     
#Validation of input functions.
def validMult(inputMatrix, inputMatrixTwo):
#Given two matrices size m*n and node_q*node_p if n != node_q then they cannot be multiplied.
    return inputMatrix.cols == inputMatrixTwo.rows
def validAdd(inputMatrix, inputMatrixTwo):
#Addition and subtraction fail if this is not met. The rows and columns must be
#the same size for the objects in place.
    return (inputMatrix.cols == inputMatrixTwo.cols and
            inputMatrix.rows == inputMatrixTwo.rows)
def validDeter(inputMatrix):
#Determinant of a matrix can only be found if the matrix is a square matrix.
    return inputMatrix.cols == inputMatrix.rows

#Matrix addition, doesn't work if the matrices don't follow the property
#Outlines in validAdd function
def matrixAddition(inputMatrix, inputMatrixTwo):
    if(not validAdd(inputMatrix, inputMatrixTwo)):
        print("The matrices are not able to be added.")
        print("M(1) != M(2) or N(1) != N(2)")
        return
    retMatrix = [[0 for i in range(inputMatrix.cols)] 
                 for j in range(inputMatrix.rows)]    
    for i in range(inputMatrix.rows):
        for j in range(inputMatrix.cols):
            retMatrix[i][j] = (inputMatrix._matrix[i][j] + 
                               inputMatrixTwo._matrix[i][j])
    return retMatrix

def matrixSubtraction(inputMatrix, inputMatrixTwo):
    if(not validAdd(inputMatrix, inputMatrixTwo)):
        print("The matrices are not able to be subtracted.")
        print("M(1) != M(2) or N(1) != N(2)") 
        return
    retMatrix = [[0 for i in range(inputMatrix.cols)] 
                 for j in range(inputMatrix.rows)]    
    for i in range(inputMatrix.rows):
        for j in range(inputMatrix.cols):
            retMatrix[i][j] = (inputMatrix._matrix[i][j] - 
                               inputMatrixTwo._matrix[i][j])
    return retMatrix

#Scalar Multiplication. Takes scale applies multi to each elt.
def scalarMultiplication(scale, inputMatrix):
    retMatrix = inputMatrix._matrix
    for i in range(inputMatrix.rows):
        for j in range(inputMatrix.cols):
            retMatrix[i][j] *= scale
    return retMatrix
'''
Is given two matrices, takes them in and makes them get multiplied through 
the basis of matrix multiplication, rows * cols and such forward. This is a
test sentence, will apply to actual code in the manner when it is needed, not 
too sure why I am still writi8ng this point forwards.
'''
def matrixMultiplication(inputMatrix, inputMatrixTwo):
    if not validMult(inputMatrix, inputMatrixTwo):
        print("These two matrices cannot be multiplied together.")
        return
    retMatrix =[[0 for i in range(inputMatrix.rows)] 
                for i in range(inputMatrixTwo.cols)] 
    if (inputMatrix.cols == inputMatrixTwo.cols and 
        inputMatrix.rows == inputMatrixTwo.rows): #mxn * nxm ~~ m==n
        equalMatrices(inputMatrix, inputMatrixTwo,retMatrix)
    elif inputMatrix.rows == inputMatrixTwo.cols: #mxn * nxp ~~ m==node_p ^ n!=m||node_p
        mirroredMatrices(inputMatrix, inputMatrixTwo, retMatrix)
    
    return retMatrix

def equalMatrices(inputMatrix, inputMatrixTwo, retMatrix):
    for i in range(inputMatrix.rows):
        for j in range(inputMatrixTwo.cols):
            k = 0
            while k < inputMatrix.rows and k < inputMatrixTwo.cols:
                retMatrix[i][j] += (inputMatrix._matrix[i][k] *
                                    inputMatrixTwo._matrix[k][j])
                k += 1

def mirroredMatrices(inputMatrix, inputMatrixTwo, retMatrix):
    for i in range(inputMatrix.rows):
        for j in range(inputMatrixTwo.cols):
            k = 0
            while k <= inputMatrix.rows and k <= inputMatrixTwo.cols:
                retMatrix[i][j] += (inputMatrix._matrix[i][k] *
                                    inputMatrixTwo._matrix[k][j])
                k += 1
            

a= matrix()
b= matrix()

print(matrixMultiplication(a,b))

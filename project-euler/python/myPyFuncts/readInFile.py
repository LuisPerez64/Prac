'''
Manners of reading in a given file, and placing it into a given object
New Keyword: with | Syntax:
   with open('filename') as varName:
    Opens a file, gives it the var name, allows operations to be done on it
    closes the file right after. Can open as many files are as needed in that 
    scope. with ..., ..., ...: (... = open('...') as var)
New Keyword: open | Syntax:
   open("FileName", Arguments("r"=read,"w"=write,"a"=append, addable(+,b,b+))
     Self explanatory syntax, opens the file for whatever operation is wanted
     +  = read/ write||append
     b  = binary file operations
     b+ = binary read/write||append

First implementation: Write the files contents to a list, including newLine
'''

###
'''
First implementation of the readIn function
@Params:
  fileName: The given file to be opened, and read in

@Returns:
  returnedList: This is the list with all the read in values, inclusive of the
   newLine for this implementation.
'''
def readInFileToList(fileName):
    returnedList = []
    with open(fileName) as inFile:
        returnedList = inFile.readlines()
    return returnedList

'''
Builds on the function above.
Added functionality:
  Removes new lines from the given list objects.
'''
def readInFileToListNoNewLines(fileName):
    noNewLineList = readInFileToList(fileName)
#Strip the newlines from the list in itself. Basic point since they're strings
    noNewLineList = [x.strip('\n') for x in noNewLineList]
    return noNewLineList

'''
Builds again on the function above.
Added functionality:
  Converts every elt in the file into an integer instead of a string.
'''
def readInFileOfNumbers(fileName):
    arrayOfNums = readInFileToListNoNewLines(fileName)
    #Convert the strings to intgers, one variable at a time. 
    arrayOfNums = [int(x) for x in arrayOfNums]
    return arrayOfNums

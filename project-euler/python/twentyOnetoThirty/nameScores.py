'''
Problem 22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name 
score.
For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

Specs:
What is the total of all the name scores in the file?
'''
import string # string.ascii_uppercase, string of the uppercase ascii alphabet
def lettersDict(): #Create a dictionary with the keys being ascii letters.
    letters = dict.fromkeys(string.ascii_uppercase, 0) 
    count = 1
#Assign the proper key values to the letters in ranking of alphabetical order.
    for i in string.ascii_uppercase:
        letters[i] = count 
        count +=1
    return letters #Dictionary: Keys = Letters, values = 1 - 26, respectively.

'''
@Params:
  listIn: The list holding the read in chars from the inputFile
  inputList: The list to be mutated to hold in the strings with the names of 
   the people in question.
@Returns:
  A list with a group of strings, that are peoples names.

Function:
 Takes in the list, and strips it of all of it's ',' and '"', using the '"' as
 a delimiter for the occurence of a new name. Stores just the name into a 
 string, and stores that string in a new list.
'''
def cleanUpInput(listIn, inputList):
    count = 0 #Counter for the delimiter in the quotation marks
    inputString = '' #String to be stored in the list, renewed each new name.
    for char in listIn:
        if char != ',':               
            if char == '"': #Delimiter for a new name being brought in.
                count += 1
            else: #A new string is being fed in
                inputString += char
            if count == 2: #The second " is met, this is the end of the string
                count = 0 #Reset the count.
                inputList.extend([inputString]) #Place the string in the list
                inputString = '' #Renew the string.
'''
@Params:
  inputFileName: The file to be read into from the given directory.
  inputList: The list to be representative of the data collected.
@Returns:
  A list of names, unsorted.
Function:
  Reads the file into a temporary list, sends that list, and the list to be 
  returned to be filtered out, and made to look as it needs to in the cleanUp 
  function.
'''
def readInFile(inputFileName, inputList = None):
    if inputList == None:
        inputList = []
    with open(inputFileName, 'r') as inputFile:
        listIn = inputFile.read()
        cleanUpInput(listIn,inputList)
    return inputList 

'''
@Params:
  name: The name obtained from the list of names from file.
  index: The location of the name when filled in, in alphabetical order.
  lettersDict: The dictionary with which to find the needed value of each
  letter.
@Returns:
  The sum of all the letters in the name * the index location of the name in 
  the list.
'''
def attainNameScore(name, index, lettersDict):
    sum = 0
    for char in name:
        sum += lettersDict[char]
    return sum * index

listOfNames = readInFile("p022_names.txt")
listOfNames.sort()
letters = lettersDict() #Dictionary: Keys = Letters, Values = 1-26 Respectively
totalNameScore = 0
location = 1#Index of the name in the list, cannot start from 0.
for name in listOfNames:
    totalNameScore += attainNameScore(name, location, letters)
    location +=1

print(totalNameScore)

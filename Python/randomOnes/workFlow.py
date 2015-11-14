def runItAll():
    myDict = makeDict()
    print(myDict)
    populateDictList(myDict)
    print(myDict)
    printTheLists(myDict)

def remDups(inpList):
    retList = []
    for i in inpList:
        if i not in retList:
            retList.extend([i])
    inpList = retList 

def inputVal(inpList):
    inpVal = -1
    while(True): #0 To exit for the input val
        inpVal = int(input('Date:'))
        if inpVal == 0:
            break
        inpList.extend([str(inpVal)])
        inpList.sort()
    remDups(inpList)

def makeDict():
    names = int(input('How many people in dict:'))
    namesDict = dict()
    for i in range(names):
        name = input('What is the persons names at index ' + str(i+1) + ': ')
        namesDict[name] = []        
    return namesDict

def populateDictList(namesDict = None):
    if namesDict == None:
        print('Why are you here without a dict. Go away')
        return None
    month = input('What month is this for: ')
    for i in namesDict:
        print('Persons name at this index: ' + i)
        inputVal(namesDict[i])
            
def printTheLists(namesDict):    
    for k in range(1,32): #Numbers to test out 1 - 31
        for i in namesDict: # Dictionary entry scroll through
            print(i)
            if k in namesDict[i]: # Found the indexed variable in the list
                print(i, k)

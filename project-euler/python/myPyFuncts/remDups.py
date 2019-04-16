'''
Functions that when used, remove duplicates from a given list, making the list
hold only one of any given elt. If it can be optimized, will do so in the
future
'''
def remDup(inputList):
    newList = [] #List to be returned to the caller function.
    for inputListIndex in inputList:
        if inputListIndex not in newList:
            newList.extend([inputListIndex])
    return newList

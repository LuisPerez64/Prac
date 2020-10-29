def findInstances(inpString, searchItem):
    outList = []
    for ind, inp in enumerate(inpString):
        if inp == searchItem:
            outList.append(ind)
    return outList


inpString = input('Input the string to search through: ')
inpSearch = input('What character are we looking for: ')

inst = findInstances(inpString, inpSearch)
outString = ''
for i in range(len(inpString)):
    if i in inst:
        outString += inpString[i]
    else:
        outString += '_'
print('Blanks where letter not sought: {0}'.format(outString))

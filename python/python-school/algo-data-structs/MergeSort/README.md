# Implementation of the Merge Sort Algorithm. 
## Introduction to Divide & Conquer

    The merge sort algorithm is one of the initial uses of the divide and conquer algorithmic approach. Used mainly to help in the delegation of the work that needs to be done into multiple more manageable tasks. Bad part of it is the added space complexity O(n*2) as another list has to be created to hold the values, as they are zipped in.(Can be circumvented, but atm using base implementations.)

### Python Implementation
```python
'''
Implementation of the Merge Sort Algorithm.
Needs at least three functions.
Partition function:Selects the pivot (Partition Point)
Merge Function: Seperates the work that is being done, and zips the lists together 
Zip || Sort Function: Brings thetwo lists together, and sorts them, creating one list. 
'''
import random

# Can patrtition the data based on multiple schemes. Defaulst to 1/2 split.
def partition(inpList, partitionFunct=1):
    if partitionFunct == 0:
        part=random.randrange(1, len(inpList))
    elif partitionFunct == 1:
        part= int(len(inpList)/2)
    elif partitionFunct == 2:
        part=int(len(inpList)/3)
    # The two non random partition schemes can be 0, which would cause infinite looping.
    if part == 0:
            part+=1
    return part

def mergeSort(inpList, partFunct=0,smallFirst=True):
    # List is empty or one, can't partition it further.
    if len(inpList) <= 1:
        return inpList
    # Pick the pivot 
    part=partition(inpList,partFunct)
    # Continue cutting the items that will be re-organized slicing on pivot
    listA=mergeSort(inpList[0:part],partFunct,smallFirst)
    listB=mergeSort(inpList[part:],partFunct,smallFirst)
    # Zip them together. Sorting along the way. Can be replaced with a sorting algorithm
    return mergeZip(listA, listB, smallFirst)

# Zips the two lists that are given together, merging them along the way
def mergeZip(inpListA, inpListB, smallFirst):
    indA,indB=0,0
    outList=[]
    tog=None
    while True:
        # If needed then append the remainder of the list to the end
        # Select which list was depleted first, append remainder to outList
        if indA == len(inpListA):
            tog=0
        elif indB == len(inpListB):
            tog=1
        if tog is not None:
            break
        # Selectively appends the next element of the two lists to the end.
        if orderCheck(inpListA[indA],inpListB[indB], smallFirst):
            outList.append(inpListA[indA])
            indA+=1            
        else:
            outList.append(inpListB[indB])
            indB+=1
            
    #Append the remaining list to the list being returned.    
    if tog == 0:
        outList.extend(inpListB[indB:])
    elif tog == 1:
        outList.extend(inpListA[indA:])
    #print('--Sorted: ',outList)
    return outList

# Controls the orientation of the given list. A-Z | Z-A
def orderCheck(inp, inp2, order):
    val=False
    if inp < inp2:
        val=True
    if not order:
        val = not val
    return val
``` 
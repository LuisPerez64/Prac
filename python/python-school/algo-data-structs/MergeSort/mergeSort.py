"""
Implementation of the Merge Sort Algorithm.
Needs at least three functions.
Partition function:Selects the pivot
Merge Function: Separates the work that is being done, and zips the lists together 
Zip || Sort Function: Brings the two lists together, and sorts them, creating one list. 
"""
import random


# Can partition the data based on multiple schemes. Defaults to 1/2 split.
def partition(inpList, partition_funct=1):
    part = 0

    if partition_funct == 0:
        part = random.randrange(1, len(inpList))
    elif partition_funct == 1:
        part = int(len(inpList) / 2)
    elif partition_funct == 2:
        part = int(len(inpList) / 3)

    # The two non random partition schemes can be 0, which would cause infinite looping.
    if part == 0:
        part += 1
    return part


def mergeSort(inpList, part_funct=0, smallFirst=True):
    toggle = False
    # Sorting a string. Probably not going to happen with this sort.
    if type(inpList) == str:
        toggle = True
        inpList = list(inpList)

    # List is empty or one, can't partition it further.
    if len(inpList) <= 1:
        return inpList

    # Pick the pivot
    part = partition(inpList, part_funct)

    # Continue cutting the items that will be re-organized slicing on pivot
    listA = mergeSort(inpList[0:part], part_funct, smallFirst)
    listB = mergeSort(inpList[part:], part_funct, smallFirst)

    # Zip them together. Sorting along the way. Can be replaced with a sorting algorithm
    retList = mergeZip(listA, listB, smallFirst)

    if toggle:
        retList = ''.join(retList)

    return retList


# Zips the two lists that are given together, merging them along the way
def mergeZip(inpListA, inpListB, smallFirst):
    indA, indB = 0, 0
    outList = []
    tog = None

    while True:
        # If needed then append the remainder of the list to the end
        # Select which list was depleted first, append remainder to outList
        if indA == len(inpListA):
            tog = 0
        elif indB == len(inpListB):
            tog = 1
        if tog is not None:
            break
        # Selectively appends the next element of the two lists to the end.
        if orderCheck(inpListA[indA], inpListB[indB], smallFirst):
            outList.append(inpListA[indA])
            indA += 1
        else:
            outList.append(inpListB[indB])
            indB += 1

    # Append the remaining elelist to the list being returned.
    if tog == 0:
        outList.extend(inpListB[indB:])
    elif tog == 1:
        outList.extend(inpListA[indA:])

    # print('--Sorted: ',outList)
    return outList


# Controls the orientation of the given list. A-Z | Z-A
def orderCheck(inp, inp2, order):
    val = False
    if inp < inp2:
        val = True
    if not order:
        val = not val
    return val

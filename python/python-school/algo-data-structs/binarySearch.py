'''
Non recursive implementation of the binary search algorithm.
inpList is implied Sorted
'''


# Uses binary search,
def binarySearch(inpList, item):
    found = False
    firstInd = 0
    lastInd = len(inpList) - 1
    # Runs until either the item is found, or the first index crosses over the last
    while not found and firstInd < len(inpList):
        midInd = int((firstInd + lastInd) / 2)
        print(firstInd, midInd, lastInd)
        # Items found
        if inpList[midInd] == item:
            found = True
            break
        if item < inpList[midInd]:
            lastInd = midInd - 1
        # Current index 
        else:
            firstInd = midInd + 1
    if not found:
        midInd = -1
    return midInd

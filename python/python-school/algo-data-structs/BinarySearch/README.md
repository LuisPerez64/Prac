# Binary Search: Used to find an item within an ordered List.
## Pseudo Code Implementation of the Binary Search Algorithm
```
# While the item is not found based on whether it's bigger or smaller, than the element at the middle of the list, go to the middle(left|right) list.
1 . Found <- False
2 . while not Found and first <= top
3 .    Midpoint <- (First + Last) DIV 2
4 .    If List[Midpoint] = ItemSought Then
5 .        ItemFound <- True
6 .    Else
7 .       If First >= Last Then
8 .          SearchFailed <- True
9 .       Else
10.            If List[Midpoint] > ItemSought Then
11.                Last <- Midpoint - 1
12.            Else
13.                First <- Midpoint + 1
14.            EndIf
15.        EndIf
16.    EndIf
```
## Python Implementation
```python
# Uses binary search on a given list, returns index of found item or -1.      
def binarySearch(inpList, item):
    found=False
    firstInd=0
    lastInd=len(inpList)-1
    midInd=0
    # Runs until either the item is found, or the first index crosses over the last                  
    while firstInd < len(inpList):
        # Added for visualization    
        print('Current slice: {0}'.format(inpList[firstInd:lastInd+1]))
        midInd=int((firstInd+lastInd)/2)
        # Items found 
        if inpList[midInd] == item:
            found=True
            break
        if item < inpList[midInd]:
            lastInd =midInd - 1
        # Current index
        else:
            firstInd=midInd + 1
    if not found:
        midInd=-1
    return midInd
# Usage, Output
'''
l=[x for x in range(15) ]
binarySearch(l, 3)
Current slice: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Current slice: [0, 1, 2, 3, 4, 5, 6]
3
# Element not in list:
binarySearch(l, 15)
Current slice: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Current slice: [8, 9, 10, 11, 12, 13, 14]
Current slice: [12, 13, 14]
Current slice: [14]
-1
'''    
```

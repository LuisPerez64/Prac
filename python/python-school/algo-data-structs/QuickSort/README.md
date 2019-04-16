# Quick Sort
## Divide and conquer sorting algorithm
    Employs a pivot point, and with that pivot delegates swap indices. At the end of the partition phase under which the pivot is used, returns a list which holds the elements greater than the pivot at one end, and less than at the other, with the pivot being put in it's place.
    It is more efficient, for most cases, than merge sort.
## Python Implementation
```
'''
QuickSort:In place sorting algorithm. 
Implements the divide and conquer method as is done with Merge Sort with a few tweaks 
to eliminate overhead. Reduces space complexity to a O(n) as not sublist has to be 
created.
Two Functions:
QuickSort: Delegation of the work that is being done
Partition: Brunt of the sorting that is done within the algorithm is done here
  Returns the pivot point for the remaining lists. Pivot is the range at which everything
  to the left or right of is sorted.
'''
def quickSort_(inpList, start, end, smallFirst):
    # Break condition. Loop invariant
    if start >= end:
        return
    # Pick a pivot from the partition from which the list will be sorted
    pivot=partition(inpList, start, end, smallFirst)
    # Sort everything from the partition point forward
    quickSort_(inpList, start, pivot-1, smallFirst)
    quickSort_(inpList, pivot+1, end, smallFirst)

# Returns a Pivot point. Everything to the left will be less than the pivot
# Everything to the right will be greater, unless smallFirst is False then inverts
# Modifies the list that is passed in. With things sorted based on pivot point.
def partition(inpList, start, end, smallFirst):
    #Pick a pivot for now elt at start. Use that as the basis for sorting. 
    pivotInd=start #random.randrange(start,end)
    pivot=inpList[pivotInd]
    # Start sorting from pivot and above 
    start+=1
    while True:
        # Increment the start index until it's greater than the end or
        # the element it's pointing to is greater than the pivot 
        while start <= end and inpList[start] <= pivot:
            start+=1
        # Same as above, but for last > pivot
        while end >= start and inpList[end] >= pivot:
            end-=1
            # If the two indices have overlapped, then no need to swap anymore
        if end < start:
            break
        # Swap the two elements
        swap(inpList, start, end)
    # Put the pivot in it's place. No element past it is smaller than it
    # Swap it with the end value, as it will be handled on the next recursion
    swap(inpList, pivotInd, end)
    return end

def swap(inpList, indA, indB):
    temp=inpList[indA]
    inpList[indA]=inpList[indB]
    inpList[indB]=temp

# Wrapper for the quickSort Algorithm, makes use easier over head. Eliminates str check at each iteration.
def quickSort(inpList,smallFirst=True):
    toggle=False
    if type(inpList) == str:
        inpList=list(inpList)
        toggle=True
    quickSort_(inpList, 0, len(inpList)-1, smallFirst)
    if toggle:
        return ''.join(inpList) 
```
# Insertion Sort 
    Base sorting algorithms. Base implementation holds roughly the same complexity as bubble sort. But reduces the amount of work that's done with each run through. Since all elements prior to the pivot point are assumed sorted.
## Implementation
```python
# inp=list(...) # Some arbitrary List
def insertionSort(inp):
    last=len(inp)
    #Runs until the marker for the last unsorted element is at the ned of the list
    while pointer < last:
        #The first element being checked against is always the elt 1 ahead of the pointer            
        pointer+=1
        first=pointer+1
        while first < last:
            # The complexity is reduced each run, no need to check the elements before pointer.
            if orderCheck(inp[pointer], inp[first], smallFirst):
                temp=inp[pointer]
                inp[pointer]=inp[first]
                inp[first]=temp
            first+=1
```
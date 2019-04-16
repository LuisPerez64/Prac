# Linear search algorithm
## Used as a brute method to find an item in a list(Ordered | Unordered).

### Pseudo definition:
```
1. position <- 0
2. found <- False
3. while position < len(List) and not found:
4.  if List[position] = item:
5.     found <- True
6.  position <- position + 1
```
### Analysis
    Worst Case: Element being sought is last element in the list
    Best Case : Element being sought is the first element in the list
    Big-O(n)
    Big-Θ(1)

##### Implemented the algorithm in a few different manners. From the above, to the pythonic version of it, using built ins.
```python
# Straight forward brute method. Easy to read through, recognizeable
def brute(inpList, item, beginFrom=0):
    index=beginFrom
    found=False
    lengthOfList=(len(inpList))
    # Iterate through the list, incrementing the index as needed.
    while not found and index < lengthOfList:
        if list[index] == item:
            # Found the value that was being sought.
            found=True
            break
        else:
            index+=1
    if not found:
        index=-1
    return index

# Pythonic brute force method. 
# If familiar with the language simple to read through.
# Cuts down the amount of code considerably from normal brute
def brutePy(inpList, item, beginFrom=0):
    index=-1
    # Makes use of the enumerate iterator to assign an index to each list element
    for ind,inp in enumerate(inpList[beginFrom:]):
        # inp holds the current value at the ind point of the list 
        if inp == item:
            index=ind
            break
    return index

# Pythonic
# Implemented with the next generator
def pythonic(inpList, item, beginFrom=0):
    #Using next. Somewhat cheating, as next in itself is a search algorithm
    # Warp it in next, get the indexes from enumeration
    # If the items match at any point return index, else return -1
    return next( (ind for ind,inp in enumerate(inpList[beginFrom:]) if inp == item), -1)
```
#### Exercises (Both implemented in linearSearch.py)
1. [x] Implement the linear search as described in the video and using the algorithm. Test that it works with items in and not in the list
2. [x] Add the functionality to add an item to the list if it is not found.
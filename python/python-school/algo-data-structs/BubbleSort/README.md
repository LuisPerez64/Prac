# Bubble Sort Algorithm
## One of the base sorting algorithms.
### Pseudo Code Implementations

## Bubble Sort Implementation
```python
# Order a list from smallest to largest value.
noMoreSwaps=False
while noMoreSwaps == False:
    noMoreSwaps=True
    for ind in range(len(inpList)-1):
        # Largest element in the list bubbles up to the top
        # swapping along the way
        if inpList[ind] > inpList[ind+1]:
            noMoreSwaps=False
            tempElement=inpList[ind]
            inpList[ind]=inpList[ind+1]
            inpList[ind+1]=tempElement
```
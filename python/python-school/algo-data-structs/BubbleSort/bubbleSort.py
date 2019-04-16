# To avoid importing modules needed on each run throgh would need to use classes. (Not yet)
import itertools
'''
Implementation of the bubble sort algorithm. Sorts lists in place, strings not so much.
'''
def bubbleSort(inp, smallFirst=True):
    # Handles strings as well as lists, may extend to other object but not using this sort often    
    toggle=False
    if type(inp) == str:
        inp=list(inp)
        toggle=True
    noMoreSwaps=False
    count=0
    while noMoreSwaps == False:
        noMoreSwaps=True
        for ind in range(len(inp)-1):
            # Largest element in the list bubbles up to the top
            # swapping along the way
            count+=1
            if orderCheck(inp[ind],inp[ind+1],smallFirst):
                noMoreSwaps=False
                tempElement=inp[ind]
                inp[ind]=inp[ind+1]
                inp[ind+1]=tempElement
    print('Total Comparisons: {0}'.format(count))
    # If dealing with a string, then return it, as not worked in place    
    if toggle == True:
        # Base accumulation for strings is append to the end, each new char.    
        output=[ x for x in itertools.accumulate(inp)][-1]
        return output

# Defaults to order == True (small first) else (small last)
# Needed to manipulate the flow of the sorting algorithms, will most likely be heavily employed.
def orderCheck(inp, inp2, order):
    val=False
    if inp > inp2:
        val=True
    if not order:
        val = not val
    return val

'''
Implementation of the base insertion sort algorithm
'''


def insertionSort(inp, smallFirst=True):
    toggle = False
    if type(inp) == str:
        inp = list(inp)
        toggle = True
    count = 0
    last = len(inp)
    # Holds the marker for the sorted list. Since not pseudo code have to start indices at 0
    # saince the pointer determines what's been sorted, the -1th index is the sort point init
    pointer = -1
    # Runs until the marker for the last unsorted element is at the ned of the list
    while pointer < last:
        # The first element being checked against is always the elt 1 ahead of the pointer
        pointer += 1
        first = pointer + 1
        while first < last:
            count += 1
            if orderCheck(inp[pointer], inp[first], smallFirst):
                temp = inp[pointer]
                inp[pointer] = inp[first]
                inp[first] = temp
            first += 1

    print('Total Comparisons: {0}'.format(count))
    # If dealing with a string, then return it, as not worked in place    
    if toggle == True:
        # Base accumulation for strings is append to the end, each new char.    
        output = ''.join(inp)
        return output


# Defaults to order == True (small first) else (small last)
# Needed to manipulate the flow of the sorting algorithms, will most likely be heavily employed.
def orderCheck(inp, inp2, order):
    val = False
    if inp > inp2:
        val = True
    if not order:
        val = not val
    return val

"""
Implementation of the Merge Sort Algorithm.
Needs at least three functions.
Partition function:Selects the pivot
Merge Function: Separates the work that is being done, and zips the lists together 
Zip || Sort Function: Brings the two lists together, and sorts them, creating one list. 
"""


# Can partition the data based on multiple schemes. Defaults to 1/2 split.
def partition(inp_list, partition_func=1):
    part = 0

    if partition_func == 0:
        import random
        part = random.randrange(1, len(inp_list))
    elif partition_func == 1:
        part = int(len(inp_list) / 2)
    elif partition_func == 2:
        part = int(len(inp_list) / 3)

    # The two non random partition schemes can be 0, which would cause infinite looping.
    if part == 0:
        part += 1
    return part


def merge_sort(inp_list, part_func=0, small_first=True):
    toggle = False
    # Sorting a string. Probably not going to happen with this sort.
    if type(inp_list) == str:
        toggle = True
        inp_list = list(inp_list)

    # List is empty or one, can't partition it further.
    if len(inp_list) <= 1:
        return inp_list

    # Pick the pivot
    part = partition(inp_list, part_func)

    # Continue cutting the items that will be re-organized slicing on pivot
    list_a = merge_sort(inp_list[0:part], part_func, small_first)
    list_b = merge_sort(inp_list[part:], part_func, small_first)

    # Zip them together. Sorting along the way. Can be replaced with a sorting algorithm
    ret_list = merge_zip(list_a, list_b, small_first)

    if toggle:
        ret_list = ''.join(ret_list)

    return ret_list


# Zips the two lists that are given together, merging them along the way
def merge_zip(inp_list_a, inp_list_b, small_first):
    ind_a, ind_b = 0, 0
    out_list = []
    tog = None

    while True:
        # If needed then append the remainder of the list to the end
        # Select which list was depleted first, append remainder to out_list
        if ind_a == len(inp_list_a):
            tog = 0
        elif ind_b == len(inp_list_b):
            tog = 1
        if tog is not None:
            break
        # Selectively appends the next element of the two lists to the end.
        if order_check(inp_list_a[ind_a], inp_list_b[ind_b], small_first):
            out_list.append(inp_list_a[ind_a])
            ind_a += 1
        else:
            out_list.append(inp_list_b[ind_b])
            ind_b += 1

    # Append the remaining ele_list to the list being returned.
    if tog == 0:
        out_list.extend(inp_list_b[ind_b:])
    elif tog == 1:
        out_list.extend(inp_list_a[ind_a:])

    # print('--Sorted: ',out_list)
    return out_list


# Controls the orientation of the given list. A-Z | Z-A
def order_check(inp, inp2, order):
    val = False
    if inp < inp2:
        val = True
    if not order:
        val = not val
    return val

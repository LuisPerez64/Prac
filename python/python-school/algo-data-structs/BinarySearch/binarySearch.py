def binary_search(inp_list, item):
    """
    Non recursive implementation of the binary search algorithm.
    inpList is implied Sorted
    """
    found = False
    first_ind = 0
    last_ind = len(inp_list) - 1
    # Runs until either the item is found, or the first index crosses over the last
    while not found and first_ind < len(inp_list):
        mid_ind = int((first_ind + last_ind) / 2)
        # Items found
        if inp_list[mid_ind] == item:
            found = True
            break
        if item < inp_list[mid_ind]:
            last_ind = mid_ind - 1
        # Current index 
        else:
            first_ind = mid_ind + 1
    if not found:
        mid_ind = -1
    return mid_ind

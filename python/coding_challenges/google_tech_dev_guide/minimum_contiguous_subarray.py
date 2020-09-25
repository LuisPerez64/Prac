def contiguous_subarray_min_sum(inp_arr):
    if len(inp_arr) == 0:
        raise Exception("Invalid input of empty array")

    # Iterate over the full array finding the sub indices
    tally = 0
    for idx in range(len(inp_arr)):
        cur_min = float('inf')
        for j_idx in range(idx, len(inp_arr)):
            cur_min = min(cur_min, inp_arr[j_idx])
        tally += cur_min
    return tally

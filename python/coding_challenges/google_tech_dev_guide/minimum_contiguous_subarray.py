def contiguous_subarray_min_sum(inp_arr):
    """
    Get the minimum value in each contiguous sequence built from the inp_arr
    Example:
    input [1,2,3] creates subsequences => [[1], [1,2], [1,2,3], [2], [2,3], [3]]
        - min value in each array [1,1,1,2,2,3] summed up to yield 10

    Time Complexity: O(n ^ 2)
        Going over the list twice to get all subsequence combinations.
    Space Complexity: O(1)
        # Memo exists as a testing tool and can be removed so not counting it for a submitted solution.
    """
    if len(inp_arr) == 0:
        raise Exception("Invalid input of empty array")

    # Iterate over the full array finding the sub indices
    inf = float('inf')
    memo = {}
    tally = 0
    for idx in range(len(inp_arr)):
        cur_min = inf
        for j_idx in range(idx, len(inp_arr)):
            cur_min = min(cur_min, inp_arr[j_idx])
            # Get the minimum value across each sublist not just the min value in range(idx - j_idx)
            tally += cur_min
            memo[(idx, j_idx)] = dict(low=cur_min, arr=inp_arr[idx:j_idx + 1])
    return tally  # sum(x.get('low') for x in memo.values())


print(contiguous_subarray_min_sum([1, 2, 2, 3, 4, 5, 6, 7]))

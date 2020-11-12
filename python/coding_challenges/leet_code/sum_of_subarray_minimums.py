"""

"""
from typing import List


class Solution(object):
    def sumSubarrayMins(self, A: List[int]):
        return self.pulled_implementation(A)

    def first_implementation(self, inp_arr: List[int]):
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
        return tally

    def pulled_implementation(self, inp_arr):
        res = 0
        stack = []
        sub_arr = dict()
        # Append -inf on both ends of the input array to ensure that we eliminate all values in the stack.
        inp_arr = [float('-inf')] + inp_arr + [float('-inf')]
        for idx, num in enumerate(inp_arr):
            # Iterate over the monotonic stack ensuring we're always decreasing
            while stack and inp_arr[stack[-1][0]] > num:
                # The right most index where num is, currently, the minimum is 
                tmp = stack.pop()
                right_most = tmp[0]
                # The left most index in the stack where the subarray containing num is the smallest.
                left_most = stack[-1][0]
                # The range from the left most index to the right most index denotes the size of sub arrays
                res += inp_arr[right_most] * (idx - right_most) * (right_most - left_most)
            stack.append((idx, num))
        return res % (10 ** 9 + 7)


Solution().sumSubarrayMins([3, 1, 2, 4])

"""
Question: https://leetcode.com/problems/duplicate-zeros/

Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]


Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""
from collections import deque
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        What would happen if there were already consecutive 0s
        i.e. [1,0,0,2,3,5]
            => [1,0,0,0,0]
        TC: O(2n) => O(n)
        SC: O(2n) at worst case if N is an array of 0s
        """
        tmp = deque()
        # Create the actual sequence to inject into the array.
        for idx in range(len(arr)):
            if arr[idx] == 0:
                tmp.append(0)
                tmp.append(0)
            else:
                tmp.append(arr[idx])
            if len(tmp) > len(arr):
                break

        for idx in range(len(arr)):
            arr[idx] = tmp.popleft()

"""
REVISIT: Just a short review of the second implementation else I could rewrite the first pretty quickly.
Question: https://leetcode.com/problems/sliding-window-maximum/
You are given an array of integers nums, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.second_implementation(nums, k)

    def first_implementation(self, nums: List[int], k: int) -> List[int]:
        """
        First implementation works but is tripped up by the max idx going out of
        the range of the sliding window and having to recalculate the max based on the new window.
        Time Complexity: O(n^2) because of the recalculation of the max at the given window.
        Space Complexity: O(1)
        """
        if len(nums) < k:
            return []
        result = []
        neg_inf = float('-inf')
        cur_max = neg_inf
        max_idx = 0
        for idx in range(k):
            if nums[idx] > cur_max:
                cur_max = nums[idx]
                max_idx = idx
        left = 1
        right = k

        result.append(cur_max)
        while right < len(nums):
            # The cur max has to be within the range of the numbers visible.
            if left >= max_idx:
                # elect a new cur_max value.
                cur_max = neg_inf
                for idx in range(left, right + 1):
                    if nums[idx] >= cur_max:
                        cur_max = nums[idx]
                        max_idx = idx

            elif nums[right] >= cur_max:
                cur_max = nums[right]
                max_idx = right
            # cur_max = max(nums[right], cur_max)
            result.append(cur_max)
            left += 1
            right += 1
        return result

    def second_implementation(self, nums: List[int], k: int) -> List[int]:
        """
        Input: [1,3,-1,-3,5,3], k=3
        Algorithm:
            1) Process the first K elements to get the max at that window.
                Inserting indices into the Deque either at the end or beginning
                based on their order . dequeu = [3,1,-1]
            2) At each step
                clean the deque ensuring that all of the valus in it are
                    >= nums[cur_idx] and values outside of the current window are removed.
                append the current idx into the queue. The zero'th idx in the queue will always be the maximum
                due to the clean operation. So append that into the output.
        Time Complexity: O(n) + O(k) => O(n + k) => O(n)
            O(n): Iteration over the full array is unavoidable.
            O(k): k relays the operations done on the Queue
                  K will either be the size of the array or less so at worst case its O(2n) => O(n)
        Space Complexity: O(k) => O(1)
            Size of K would not change based on the len of nums.
            Output is not included in the complexity else it's O(n)
        """
        if len(nums) * k == 0:
            # Empty array or no window
            return []
        if k == 1:
            # Window size would just be the elements in the array
            return nums

        def clean(n_idx):
            """
            Ensure that the deque at index 0 is always the highest value
            and within the current sliding windows indices.
            """
            # remove indexes of elements not inside the current window if they're the 0th
            if dq and dq[0] == n_idx - k:
                # Max value is outside of the window.
                dq.popleft()

            # remove indexes of elements smaller than the current index.
            while dq and nums[n_idx] > nums[dq[-1]]:
                # pop them all off if need be
                dq.pop()

        dq = deque()
        result = []
        for idx in range(k):
            # Initialize the queue with the first elements of the sliding window.
            clean(idx)
            dq.append(idx)
        # populate the max from 0 -> k which is the first window.
        result.append(nums[dq[0]])

        for idx in range(k, len(nums)):
            clean(idx)
            dq.append(idx)
            result.append(nums[dq[0]])

        return result

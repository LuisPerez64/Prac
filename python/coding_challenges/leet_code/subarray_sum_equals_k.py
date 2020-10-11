"""
Question: https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return self.second_implementation(nums, k)

    def first_implementation(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n^2)
        """
        res = 0
        for idx_a in range(len(nums)):
            cur = 0
            for idx_b in range(idx_a, len(nums)):
                cur += nums[idx_b]
                if cur == k:
                    res += 1
        return res

    def second_implementation(self, nums: List[int], k: int) -> int:
        """
        Using the prefix sum algo.
        Example Run:
        [3, 4, 7, 2, -3, 1, 4, 2], k == 7
        Idx: 1 => Sum: 7 => Sum - K: 0, Pref_sum: {0: 1, 3: 1}
        Idx: 2 => Sum: 14 => Sum - K: 7, Pref_sum: {0: 1, 3: 1, 7: 1}
        Idx: 5 => Sum: 14 => Sum - K: 7, Pref_sum: {0: 1, 3: 1, 7: 1, 14: 1, 16: 1, 13: 1}
        Idx: 7 => Sum: 20 => Sum - K: 13, Pref_sum: {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1, 18: 1}
        """
        prefix_sum = defaultdict(int)
        prefix_sum[0] += 1
        acc = 0
        res = 0
        # print(nums)
        for idx, num in enumerate(nums):
            acc += num
            if acc - k in prefix_sum:
                # Given the array in the example run. If at the sum of the array being 14 we were valid then from each
                # instance we had that sum we could iterate over the array and get here as the sum difference
                # between the two points is 0
                res += prefix_sum.get(acc - k, 0)
                # print(f"Idx: {idx} => Sum: {acc} => Sum - K: {acc -k}, Pref_sum: {dict(prefix_sum)}")
            prefix_sum[acc] += 1
        # print(prefix_sum)
        return res

"""
REVISIT: The solution I got to took way too long to attain. Mainly through trial and error, so need to redo this problem
    The brute force solutions were insanely inefficient, and the space complexity of the final one is a bit much.

Question: https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.third_implementation(nums)

    def first_implementation(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force approach. Go through every possible combination of the array elements
        Time Complexity: O(n^3)
        Space Complexity: O(n)
        """

        ret_set = set()

        for idx_a in range(len(nums)):
            for idx_b in range(idx_a + 1, len(nums)):
                for idx_c in range(idx_b + 1, len(nums)):
                    if nums[idx_a] + nums[idx_b] + nums[idx_c] == 0:
                        ret_set.add(tuple(sorted([nums[idx_a], nums[idx_b], nums[idx_c]])))
        return [list(x) for x in ret_set]

    def second_implementation(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force approach with minor optimization.
        Go through every possible combination of the array elements and capture every non-unique element caught by the idx_a field
        They don't need to be recalculated
        Time Complexity: O(n^3)
        Space Complexity: O(n)
        """

        ret_set = set()
        seen_nums = set()

        for idx_a in range(len(nums)):
            if nums[idx_a] in seen_nums:
                continue
            seen_nums.add(nums[idx_a])
            for idx_b in range(idx_a + 1, len(nums)):
                for idx_c in range(idx_b + 1, len(nums)):
                    if nums[idx_a] + nums[idx_b] + nums[idx_c] == 0:
                        ret_set.add(tuple(sorted([nums[idx_a], nums[idx_b], nums[idx_c]])))
        return [list(x) for x in ret_set]

    def third_implementation(self, nums: List[int]) -> List[List[int]]:
        """
        Using the compliments method to remove a loop iteration from the call list.
        Sorting the values in the input to remove duplicates
        If the value being sought exists in the list then append the list to the end result.
        Time Complexity: O(n) + O(n^2) * O(n log(n)) + O(n) ~> O(n ^ 2)
        Space Complexity: O(n)
        """
        from collections import defaultdict
        exists = defaultdict(int)
        nums.sort()
        ret = set()
        for num in nums:
            # Slight implementation of a Counter to get the duplicated values handled and their occurrences logged
            exists[num] += 1

        # O(n^2)  Iterate over only paired elements no need to go through n a third time.
        for idx_a in range(len(nums)):
            if idx_a > 0 and nums[idx_a] == nums[idx_a - 1]:
                # Skip recalculating the duplicated values
                continue
            for idx_b in range(idx_a + 1, len(nums)):
                # Get the needed complimentary value to the current indices
                # checking if the value exists in the list (as many times as needed),
                diff = 0 - (nums[idx_a] + nums[idx_b])
                if diff in exists:
                    if diff in [nums[idx_a], nums[idx_b]] and exists[diff] < 2 or \
                            diff == 0 and exists[diff] < 3:
                        break
                    else:
                        # Remove permutations from the returned list by converting to a hashable sorted tuple
                        ret.add(tuple(sorted([nums[idx_a], nums[idx_b], diff])))

        return [list(x) for x in ret]


if __name__ == '__main__':
    print(Solution().third_implementation([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))

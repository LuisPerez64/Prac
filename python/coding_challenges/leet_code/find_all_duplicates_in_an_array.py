"""REVISIT: The constraint makes this an interesting question.
Question: https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> List[int]:
        """
        Using a set for duplicate check.

        TC: O(n)
        SP: O(n)
        """
        seen = set()
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)

        return res

    def second_implementation(self, nums: List[int]) -> List[int]:
        """
        Attempt to resolve this with O(1) space and O(n) time.
        Since all the integers that will appear in the array are within the
        constraint that they will be in the range of the size of the
        array (1 <= a[i] <= n) we can use the indexing property of the value
        to determine if it's been seen before. If the value is a negative value at the index
        when we encounter the offset again then we can assume that it's been flipped

        i.e. nums = [1,2,3,1,2,4]
        idx = 0, nums[1 - 1] *= -1, nums == [-1, 2,3,1,2,4]
        ...
        idx = 5, nums[4 - 1] *= -1, nums == [1,2,-3,-1,2,4]

        Solution is viable due to the constraint on the values in the array.
        If there were negatives interleaved or values > len(nums) then it would need reworking.
        """
        output = list()
        for idx in range(len(nums)):
            # Find the offset in the nums array that this number should flip the signs for.
            # Since the number may have been flipped. Flip its sign back
            offset = abs(nums[idx]) - 1
            if nums[offset] < 0:
                # the values been visited already, so add its result to the output
                output.append(offset + 1)
            else:
                # flip the sign on the value at the offset.
                nums[offset] *= -1
        return output

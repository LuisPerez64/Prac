"""
REVISIT: Floyds Algorithm needs a look through.

Question: https://leetcode.com/problems/find-the-duplicate-number/
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?

"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.first_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Use a set to get the first instance of a repeatd value.
        Time Complexity: O(n)
        Size Complexity: O(n)
        """
        occs = set()
        for num in nums:
            if num in occs:
                return num
            occs.add(num)
        # If no duplicates it should raise

    def pulled_implementation(self, nums: List[int]) -> int:
        """
        Using the same logic for finding a cycle in a linked list. But within an Array construct.
        Uses Floyds Algorithm which is ridiculous to have to think about in an interview...
        """
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

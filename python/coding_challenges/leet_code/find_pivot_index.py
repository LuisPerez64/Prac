"""
Question: https://leetcode.com/problems/find-pivot-index/
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is
equal to the sum of all the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes,
you should return the left-most pivot index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


Constraints:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].

"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        return self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Using the sliding window method incrementing the side of the window with the
        smallest sum at each point until they begin to cross.
        Edge case comes to play when the first value at either starting index is 0.
        Does not pass all test cases...
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        size = len(nums)
        if size == 0 or size == 2:
            return -1
        if size == 1:
            return 0

        def find_first_nonzero_index(start, inc):
            # Find the first index where the value isn't zero
            while start + inc != 0 and start + inc != len(nums):
                if nums[start] != 0:
                    break
                start += inc
            return start

        right = find_first_nonzero_index(size - 1, -1)
        left = find_first_nonzero_index(0, 1)
        left_sum = nums[left]
        left += 1
        right_sum = nums[right]
        right -= 1

        while left < right:
            # based on the sum on each side slide one part of the window.
            if left_sum > right_sum:
                right_sum += nums[right]
                right -= 1
            elif left_sum < right_sum:
                left_sum += nums[left]
                left += 1
            else:
                # they're equal sums but we've not exhausted the array yet increment everything.
                left_sum += nums[left]
                right_sum += nums[right]
                left += 1
                right -= 1
        if sum(nums[:right + 1]) == sum(nums[right:]):
            # The sums are equivalent and the arrays been exhausted.
            # we want the leftmost index of the array and the only way the array is exhausted is if the right crosses the left ptr.
            return right
        return -1

    def second_implementation(self, nums) -> int:
        """
        Simpler solution using one pointer and the sum calculation.
        We grab the total sum of the array and initialize the accumulator to 0
        iterate over the array checking if the total_sum - accumulator - cur_val are equivalent to the accumulators total.
        if they are we've found the leftmost index return it
        else increment the accumulator with the current value.
        Time Complexity: O(2n) => O(n)
            All elements have to be visited.
        Space Complexity: O(1)
        """
        total_sum = sum(nums)
        cur_sum = 0
        idx = 0
        for cur_val in nums:
            if cur_sum == total_sum - cur_sum - cur_val:
                return idx
            idx += 1
            cur_sum += cur_val

        return -1

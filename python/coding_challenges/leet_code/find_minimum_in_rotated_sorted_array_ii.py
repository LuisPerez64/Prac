"""
REVISIT: The first implementation does not change as it will catch both cases.
    The second is worth reviewing as well as the algo explanation below.
Question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return

    self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Initial approach iterate over the array, and at the point where arr[n-1] > arr[n] you've found the min.
        Same algo as
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if not nums:
            raise Exception("No base case for empty array.")
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            # Array is fully sorted.
            return nums[0]
        # initialize the max val and result as 0th element.
        # for the case where nums is fully sorted the value will keep increasing. and result will not change.
        max_val = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num >= max_val:
                max_val = num
            else:
                result = num
                break
        return result

    def second_implementation(self, nums: List[int]) -> int:
        """
        Finding the pivot index through modified binary search.
        In full we've got two sorted arrays in the worst case and one sorted array in the best case.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if not nums:
            raise Exception("No base case for empty array.")
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            # Array is fully sorted.
            return nums[0]

        def find_pivot():
            """
            Find the minimum value. This is a bit different from the implementation for the 1st part of this problem.
            We're not moving in as wide an angle as before as the start just needs to satisfy that every number before
            is smaller than it.
            The possible duplicated values add a level of complexity that's going to need to be revisited.
            The midpoint is then calculated as start_idx + (end_idx - start_idx) // 2
                This is a caveat and could be replaced with the normal use `mid_point = (end_idx + start_idx) // 2`
            Three base cases:
                1) the mid point is less than the end. => end = mid_point
                    Move the end down to the midpoint
                2) mid point > end  => start = mid_point + 1
                    Move the start forward to the mid point as every value before
                    it should be higher than the current bound.
                3) mid point and end are equivalent. => end = end - 1
                    Don't greedily decrement the end in this case, just decrease
                    it by one to get past the current duplicated values.
            """
            start_idx = 0
            end_idx = len(nums) - 1
            while start_idx <= end_idx:
                mid_point = start_idx + (end_idx - start_idx) // 2
                # mid_point = (end_idx + start_idx) // 2
                if nums[mid_point] < nums[end_idx]:
                    end_idx = mid_point
                elif nums[mid_point] > nums[end_idx]:
                    # Still increasing so start from here next round
                    start_idx = mid_point + 1
                else:
                    # just decrease the end_idx by 1 as its equal to the mid_point
                    end_idx -= 1
            # Handles cases where the array is all duplicates i.e. [1,1,1,1,1]
            # print(nums, start_idx, end_idx)
            return nums[start_idx]

        # The array is pivoted. Find the first instance satisfying nums[idx-1] > nums[idx]
        return find_pivot()


"""
Explanation:

Approach 1: Variant of Binary Search
Intuition

Given a sorted array in ascending order (denoted as L[i]), the array is then rotated over certain unknown pivot, 
(denoted as L'[i]). We are asked to find the minimum value of this sorted and rotated array, which is to find the value 
of the first element in the original array, i.e. L[0].

The problem resembles a common problem of finding a given value from a sorted array, to which problem one could apply 
the binary search algorithm. Intuitively, one might wonder if we could apply a variant of binary search algorithm 
to solve our problem here.

Indeed, this is the right intuition, though the tricky part is to figure out a concise solution
 that could work for all cases.

To illustrate the algorithm, we draw the array in a 2D dimension in the following graph, where the X axis indicates the
 index of each element in the array and the Y axis indicates the value of the element.

pic

The main structure of our algorithm remains the same as the classical binary search algorithm. 
As a reminder, we summarize it briefly as follows:

We keep two pointers, i.e. low, high which point to the lowest and highest boundary of our search scope.
We then reduce the search scope by moving either of pointers, according to various situations.
 Usually we shift one of pointers to the mid point between low and high, (i.e. pivot = (low+high)/2),
  which reduces the search scope down to half. This is also where the name of the algorithm comes from.
The reduction of the search scope would stop, either we find the desired
 element or the two pointers converge (i.e. low == high).
Algorithm

In the classical binary search algorithm, we would compare the pivot element (i.e. nums[pivot])
 with the value that we would like to locate. In our case, however, we would compare the pivot element to the element
  pointed by the upper bound pointer (i.e. nums[high]).

Following the structure of the binary search algorithm, the essential part remained is to design the cases on how to
 update the two pointers.

Here we give one example on how we can break it down concisely into three cases.
 Note that given the array, we consider the element pointed by the low index to be on the left-hand side of the array,
  and the element pointed by the high index to be on the right-hand side.

Case 1). nums[pivot] < nums[high]

pic

The pivot element resides in the same half as the upper bound element.
Therefore, the desired minimum element should reside to the left-hand side of pivot element.
 As a result, we then move the upper bound down to the pivot index, i.e. high = pivot.
Case 2). nums[pivot] > nums[high]

pic

The pivot element resides in the different half of array as the upper bound element.
Therefore, the desired minium element should reside to the right-hand side of the pivot element. 
As a result, we then move the lower bound up next to the pivot index, i.e. low = pivot + 1.
Case 3). nums[pivot] == nums[high]

pic

In this case, we are not sure which side of the pivot that the desired minimum element would reside.
To further reduce the search scope, a safe measure would be to reduce the upper bound by one (i.e. high = high - 1),
 rather than moving aggressively to the pivot point.
The above strategy would prevent the algorithm from stagnating (i.e. endless loop). More importantly, it maintains 
the correctness of the procedure, i.e. we would not end up with skipping the desired element.
To summarize, this algorithm differs to the classical binary search algorithm in two parts:

We use the upper bound of search scope as the reference for the comparison with the pivot element, 
while in the classical binary search the reference would be the desired value.

When the result of comparison is equal (i.e. Case #3), we further move the upper bound, 
while in the classical binary search normally we would return the value immediately.
"""

"""  **REVISIT**
Question: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

    1) What if the given array is already sorted? How would you optimize your algorithm?
    2) What if nums1's size is small compared to nums2's size? Which algorithm is better?
    3) What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into
 the memory at once?

Follow Up Answers:
    1) If the given array is already sorted then the heapify function would be removed
        and the operations would be done on a sorted list with no change past the way the pop is called.
    2) The implementation that takes place will find its bound based on the length of the arrays. The size
        discrepancy between the two would be neglected as the depletion of either would cause an exit
    3) If the values in either array need to be read from disk this complicates the current solution given
       possible size constraints. If they are sorted then iteration of the input would be handled in a helper function
       that would yield the same function signature (to ease implementation). If they are not sorted then the elements
       in the input would have to be placed in a map as they are read from the file (or searched for).
"""
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Iterating over the whole list of values for each would be the brute force solution and would yield
    an O(n^2) time complexity.

    Solution would sort the arrays and use pointers to keep track of the changes that are apparent in each.

    Sorting Algorithm: Heapsort
        Time Complexity: O(n log(n))
        Space Complexity: O(1)

    Time Complexity: O(n log(n)) + O(m log(m)) + O(n) -> O(n)
        Given O(n) asserting that n refers to the smaller array of the two.
    Space Complexity: O(1) + O(1) + O(n)
        The resulting array would be the bearer of the added space complexity.
    """
    if len(nums1) < 1 or len(nums2) < 1:
        return []

    # Sort both of the input arrays
    from heapq import heapify, heappop

    def safe_pop(inp_heap, prev_val=None):
        if len(inp_heap):
            return heappop(inp_heap)
        elif prev_val is not None:
            return prev_val
        else:
            return float('inf')

    heapify(nums1)
    heapify(nums2)

    small_heap, big_heap = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    result_arr = list()
    """
    As long as both heaps still have elements in them continue the operations. 
    """
    cur_small = heappop(small_heap)
    cur_big = heappop(big_heap)
    while len(small_heap) or len(big_heap):
        if cur_small != cur_big:
            # Only need to pop the value off of the heap that's smaller until they match.
            if cur_small < cur_big:
                cur_small = safe_pop(small_heap, None)
            else:
                cur_big = safe_pop(big_heap, None)
        else:
            # Both heaps match so the value needs to be added to the results and removed from both
            result_arr.append(cur_small)
            cur_small = safe_pop(small_heap, None)
            cur_big = safe_pop(big_heap, None)
    if (len(small_heap) == 0 or len(big_heap) == 0) and cur_small == cur_big:
        result_arr.append(cur_small)
    return result_arr
    #             # Pop the value off each of the heaps until the values they hold are equivalent.
    #             # This removes the need to keep track of multiple index pointers.
    #             while cur_small < cur_big and len(small_heap):
    #                 # keep popping off of the small heap until the values are the same
    #                 cur_small = heappop(small_heap)

    #             while cur_big < cur_small and len(big_heap):
    #                 cur_big = heappop(big_heap)

    #             if cur_small == cur_big:
    #                 result_arr.append(cur_small)

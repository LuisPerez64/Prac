"""
Question: https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

from typing import List


def first_implementation(nums: List[int]) -> int:
    """
    Implied linear runtime means that it should run in O(n).
    Using a map to ensure that the value exists yields a size complexity of O(n).
      Would use a set and operate on a in/out method but that's ineffective as the value could appear x*2 times

    Time Complexity: O(n) as the array is iterated over Once
    Space Complexity: O(n)
      The exists dict could grow to be at most n/2 in size and the just_once set could do the same
    """

    just_once = set()
    exists = dict()
    for num in nums:
        if num in exists:
            temp = exists[num] + 1
            exists[num] = temp
            if temp > 2:
                # Value exists too many times. Short circuit it here as only one failing case exists
                return num
            just_once.remove(num)
        else:
            exists[num] = 1
            just_once.add(num)

    # There should only be one element in the set given the constraints if it appears only once.
    # If the value appeared > 2 times then the dict check would catch it.
    return just_once.pop()


def second_implementation(nums: List[int]) -> int:
    """
    Implementation using a sorting algorithm to get the ordering of the list in place
     and then simple iteration to get the elements listing
    Sorting Algorithm: HeapSort
        Time Complexity: O(n log(n))
        Space Complexity: O(1)
    Time Complexity: O(n*log(n)) + O(n) -> O(n)
    Space Complexity: O(1)
    """
    from heapq import heapify, heappop
    heapify(nums)
    ret_val = heappop(nums)
    count = 1
    while len(nums):
        cur_val = heappop(nums)
        if ret_val == cur_val:
            count += 1
            if count > 2:
                break
        else:
            if count == 1:
                # The value only occurred once before a shift happened.
                break
            count = 1
            ret_val = cur_val

    return ret_val

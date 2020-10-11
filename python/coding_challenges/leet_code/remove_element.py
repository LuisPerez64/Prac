"""
Question: https://leetcode.com/problems/remove-element/
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
 extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to
the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return self.first_implementation(nums, val)

    def first_implementation(self, nums: List[int], val: int) -> int:
        """
        Using the two pointer approach.
        One pointer pointing to the new length of the array without the val
        Every time we encounter a number thats not val the len_ptr increases
        and the value at read_ptr is placed in it.
        Example:
        arr= [3,2,1,3], val = 2
            read=0, len=0 cur = 3 => inc read,len
            read=1 len=1 cur = 2 inc read
            read=2 len=1 cur = 1, arr[read] != val, swap val into len_ptr inc len,inc read
        arr = [3,1,1,3]
            read=3, len = 2, cur=3, arr[read] != val, swap val into len_ptr inc len,read
        arr = [3,1,3,3], len_ptr = 3
        """
        len_ptr = 0
        for read_ptr in range(len(nums)):
            if nums[read_ptr] != val:
                nums[len_ptr] = nums[read_ptr]
                len_ptr += 1

        return len_ptr

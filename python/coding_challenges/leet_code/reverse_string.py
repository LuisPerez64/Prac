"""
Question: https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.first_implementation(s)

    def first_implementation(self, inp_str: List[str]) -> None:
        """
        In place reversal of a string.
        """
        left = 0
        right = len(inp_str) - 1
        while left < right:
            inp_str[left], inp_str[right] = inp_str[right], inp_str[left]
            left += 1
            right -= 1

"""
Question: https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−2^31,  2^31 − 1].
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        return self.first_implementation(x)

    @staticmethod
    def first_implementation(inp: int) -> int:
        """
        Implementation running in O(n) time for the implied complexity of the reverse operation
        Space Complexity: O(n)
            -- Given that there needs to be a new string allocated of at least n size.
        """
        is_neg = False
        if inp < 0:
            is_neg = True
            inp *= -1
        outp = int(str(inp)[::-1])
        if outp > (2 ** 31 - 1) or outp < -2 ** 31:
            outp = 0
        return outp * -1 if is_neg else outp

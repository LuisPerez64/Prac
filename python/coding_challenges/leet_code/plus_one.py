"""
Question: https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    Constraint is not placed on the final digit in the sequence being < 9 so if the last digit causes an overflow
    it will need to be met with a trickling incrementation.
    """

    # Case 1: Final digit < 9 just increment it
    # Case 2: Final digit is 9 convert it to 0 and run increment on previous until a non 9 digit is found
    # Case 3: digits amount to 999 -> 1000 if this is met then increment the size of the array

    for dig_idx in range(len(digits) - 1, -1, -1):
        digit = digits[dig_idx]
        if digit != 9:
            digits[dig_idx] = digit + 1
            break
        digits[dig_idx] = 0
    else:
        digits.insert(0, 1)

    return digits

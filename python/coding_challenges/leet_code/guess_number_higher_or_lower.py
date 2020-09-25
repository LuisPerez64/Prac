"""
Question: https://leetcode.com/problems/guess-number-higher-or-lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""


def guess_number_higher_lower_one(n: int, picked) -> int:
    start = 1
    end = n
    mid_point = (start + end) // 2
    while start < end:
        is_valid = picked - mid_point
        if is_valid == 0:
            break
        if is_valid < 0:
            end = mid_point
        else:
            start = mid_point + 1
        mid_point = (start + end) // 2

    return start

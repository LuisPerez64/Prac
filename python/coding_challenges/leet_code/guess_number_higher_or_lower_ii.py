"""
Question: https://leetcode.com/problems/guess-number-higher-or-lower-ii/
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""


def guess_number_higher_lower_two(n: int) -> int:
    from functools import lru_cache
    # The equation comes down to exhausting the possible wrong guesses until a correct one is given.
    # Since the problem can be broken down into sub-problems then best would be a DP solution with memoization.

    memo = {}  # Key == (low, high) val == max amount of money needed to guarantee a win

    @lru_cache(maxsize=2 ** 16)
    def min_cost(low, high):
        if (low, high) in memo:
            return memo[(low, high)]
        if low >= high:
            # The values don't need to be calculated further as the mid points been met.
            return 0
        min_result = float('inf')
        for guess_value in range((low + high) // 2, high + 1):
            current_result = guess_value + max(min_cost(low, guess_value - 1), min_cost(guess_value + 1, high))
            min_result = min(min_result, current_result)
        memo[(low, high)] = min_result
        return min_result

    return min_cost(1, n)

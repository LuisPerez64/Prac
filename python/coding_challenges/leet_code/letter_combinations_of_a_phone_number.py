"""
Question: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
from typing import Dict, List


def letter_combinations(digits: str) -> List[str]:
    from functools import lru_cache
    # memoization indices to not repeat work. indices will be numeric strings for the possible combinations.
    # Input of the original possibles list.
    memo: Dict[str, list] = {
        "": [""],
        "0": [""],
        '1': [""],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['node_p', 'node_q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    # Combine function will iterate over every permutation for the given input.
    # Only ever really need to get combos for pairs of two

    @lru_cache(maxsize=None)
    def get_combinations(first_str, second_str):
        first = memo[first_str]
        second = memo[second_str]
        local_res = []
        # local_res_swapped = []
        # do_swapped = False
        if first_str + second_str in memo:
            # This case would never be met under the current implementation
            return memo[first_str + second_str]

        # Kill two birds with one stone if need be
        # do_swapped = second_str + first_str not in memo and first_str != second_str

        for elt_a in first:
            for elt_b in second:
                local_res.append(elt_a + elt_b)
                # if do_swapped:
                #     local_res_swapped.append(elt_b+elt_a)
        memo[first_str + second_str] = local_res
        # if do_swapped:
        #     memo[second_str + first_str] = local_res_swapped
        return local_res

    for idx in range(1, len(digits)):
        prev_str = digits[0:idx - 1]
        # Only really need to do the combination based on the previous and current digit which may would things up.
        cur_combo = get_combinations(digits[idx - 1], digits[idx])
        arr = []
        for prev in memo[prev_str]:
            for cur in cur_combo:
                arr.append(prev + cur)
        # Because [n:m] slices from n -> m-1 have to add in the added index to get the full string.
        memo[digits[0:idx + 1]] = arr

    # Need to take into account the invalid numbers producing empty strings. i.e. 123 == 23.
    # Given 1,0, or'' must return an empty array.
    return [x for x in memo[digits] if x]

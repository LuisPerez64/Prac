"""
Question: https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from typing import List


def generate_parenthesis(n: int) -> List[str]:
    # Can either go through every possible permutation explicitly or break the problem down dynamically
    results = list()

    # At each stage you can either choose to create a new parens or close the existing string
    # For each pair below the size of n so create dynamic values  based on whether you closed or opened a new parens
    def recursive_pairing(cur_string, num_left, num_right):
        if len(cur_string) == n * 2:
            results.append(cur_string)
            return
        if num_left < n:
            # Can still keep adding open parens to the current string
            recursive_pairing(cur_string + '(', num_left + 1, num_right)

        if num_left > num_right:
            # Need to close the current parent before trying to open the next
            recursive_pairing(cur_string + ')', num_left, num_right + 1)

    recursive_pairing('', 0, 0)
    return results
# print(len(generate_parenthesis(10)))
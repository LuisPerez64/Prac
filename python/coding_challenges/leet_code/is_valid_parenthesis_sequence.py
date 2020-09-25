"""
Question: https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


def valid_parenthesis(s: str) -> bool:
    parens_queue = []
    match = {'(': ')', '{': '}', '[': ']'}
    for x in s:
        if x in '([{':
            parens_queue.append(x)
            continue

        if len(parens_queue) == 0 or match[parens_queue[-1]] != x:
            # Cannot get here without something in the paren beforehand ']' is invalid
            return False

        parens_queue.pop()
    return len(parens_queue) == 0

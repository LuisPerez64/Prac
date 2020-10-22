"""
Question: https://leetcode.com/problems/backspace-string-compare/
Given two strings S and T, return if they are equal when both are typed
into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        use two stacks for comparison. If we see a '#' then we pop off of the stack.
        Could also use counters instead.
        """

        s_1 = list()
        s_2 = list()

        for k in S:
            if k == '#':
                if s_1:
                    s_1.pop()
            else:
                s_1.append(k)
        for l in T:
            if l == '#':
                if s_2:
                    s_2.pop()
            else:
                s_2.append(l)
        return s_1 == s_2

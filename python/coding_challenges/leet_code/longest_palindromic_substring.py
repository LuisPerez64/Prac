"""
Question: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""
from functools import lru_cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.is_palindrome(s):
            return s
        return self.second_implementation(s)

    def is_palindrome(self, inp_str) -> bool:
        left = 0
        right = len(inp_str) - 1
        while left < right:
            if inp_str[left] != inp_str[right]:
                return False
            left += 1
            right -= 1
        return True

    def first_implementation(self, inp_str) -> str:
        """
        Time Complexity: O(n^3)
        """

        longest = ""
        len_longest = 0
        for start in range(len(inp_str)):
            for end in range(len(inp_str), start, -1):
                if end - start < len_longest:
                    # Don't bother rechecking strings shorter than the known longest
                    continue
                cur_str = inp_str[start:end + 1]

                if self.is_palindrome(cur_str):
                    len_longest = len(cur_str)
                    longest = cur_str
                    break
        return longest

    def second_implementation(self, s) -> str:
        """
        Pulled from a comment on leetcode as the only part missing was the memoization aspect thats brought in to it.
        https://leetcode.com/problems/longest-palindromic-substring/discuss/759291/Straight-Forward-Short-and-Clean-Python-DP-with-Detailed-Simple-Explanation!
        """
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        dp, ans = [[0] * n for _ in range(n)], {}
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans[j - i + 1] = s[i:j + 1]
                else:
                    dp[i][j] = False
        return ans[max(ans)]

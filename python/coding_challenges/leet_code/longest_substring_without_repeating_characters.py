""" REVISIT: The sliding window concept deserves a review as it applies to a lot of problems with arrays.
Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Self note:
            This should really be the named longest substring of entirely unique chars
        """
        return self.second_implementation(s)

    @staticmethod
    def first_implementation(inp_str: str) -> int:
        """
        Naive attempt failing due to the fact that its not taking into accound repeating substrings
        i.e. "abcabc" longest unique substring should be "abc" this yields the original stric
        """
        if len(inp_str) <= 1:
            return len(inp_str)
        highest = 1
        cur_count = 1
        prev_char = inp_str[0]
        seen_substr = set(prev_char)
        for cur_char in inp_str[1:]:
            if cur_char == prev_char:
                highest = max(highest, cur_count)
                cur_count = 1
            else:
                cur_count += 1
            prev_char = cur_char

        return highest

    @staticmethod
    def second_implementation(inp_str: str) -> int:
        """
        Implementation with a sliding window concept on the data.
        Time Complexity: O(2n) ~ O(n)
        Space Complexity: O(min(m, n)) ~ O(k)
            m: Size of the input string
            n: Size of the lexicon used to create the characters (i.e. 26 letters in english alpha)
                as the elements that exist and have been seen will be removed.
        """
        start = end = 0
        seen = set()
        max_len = 0
        while start < len(inp_str) and end < len(inp_str):
            # Continue incrementing the window as long as the string it captures is not repeating
            if inp_str[end] not in seen:
                # Current char hasn't been seen yet so add it to the set and increment the windows end boundary
                seen.add(inp_str[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                # Theres been a duplicate characted found in the substring so increment the start index and
                # remove the character at that index to validate the window moving forward.
                seen.discard(inp_str[start])
                start += 1

        return max_len

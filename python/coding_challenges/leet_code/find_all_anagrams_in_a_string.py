""" REVISIT: The frequency calculation used is helpful. Sliding window is still used but only one living pointer.
Question: https://leetcode.com/problems/find-all-anagrams-in-a-string

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both
 strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.first_implementation(s, p)

    def first_implementation(self, inp_str: str, anagram: str) -> List[int]:
        """
        Measure if the count of the values from the inp_str in window (cur -> cur+len(anagram)) are equivalent to
        the count of their frequencies in the anagram string.
        """

        ana_count = defaultdict(int)
        cur_count = defaultdict(int)
        res = []
        for char in anagram:
            ana_count[char] += 1

        for idx in range(len(inp_str)):
            char = inp_str[idx]
            # increase the frequency counter for the given character.
            cur_count[char] += 1

            if idx >= len(anagram):
                out_char = inp_str[idx - len(anagram)]
                # If you're out of the range of the max size for the character then decrement your count.
                cur_count[out_char] -= 1
                if cur_count[out_char] == 0:
                    cur_count.pop(out_char)

            if ana_count == cur_count:
                res.append(idx - len(anagram) + 1)
        return res

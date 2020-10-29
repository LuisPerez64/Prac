"""
REVISIT: The Algorithm is straight forward, just need to review it.
    I got to the solution but way too many hiccups along the way,
Question: https://leetcode.com/problems/group-shifted-strings/
Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Sort by length to get the buckets as they must be in the same len for the strings to
        be grouped.
        """
        ord_base = ord('a')
        res = defaultdict(list)
        neg_inf = float('-inf')
        for word in strings:
            if len(word) <= 1:
                tmp = (neg_inf,)
            else:
                prev = ord(word[0]) - ord_base
                tmp = []
                # For each input check to see what value is needed for it to get to the next.
                for char in word[1:]:
                    cur = (prev - ord(char) - ord_base) % 26
                    tmp.append(cur)
                    prev = (ord(char) - ord_base) % 26
                tmp = tuple(tmp)
            res[tmp].append(word)
        # strings.sort(key=lambda k: (len(k), ))
        return res.values()

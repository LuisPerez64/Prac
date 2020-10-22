"""
Question: https://leetcode.com/problems/find-common-characters/

Given an array A of strings made only from lowercase letters, return a list of all characters
that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""
from collections import defaultdict
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        freq = defaultdict(int)
        if not A:
            return []
        for char in A[0]:
            freq[char] += 1

        for word in A[1:]:
            cur_freq = defaultdict(int)
            for char in word:
                if char in freq:
                    cur_freq[char] += 1
            for char in list(freq.keys()):
                freq[char] = min(freq[char], cur_freq[char])
                if freq[char] == 0:
                    freq.pop(char)
        res = []
        for char, occ in freq.items():
            res.extend([char] * occ)
        return res

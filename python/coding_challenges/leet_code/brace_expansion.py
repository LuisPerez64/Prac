"""
Question: https://leetcode.com/problems/brace-expansion/
A string S represents a list of words.

Each letter in the word has 1 or more options.
If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options.
For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.



Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]


Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
"""
from collections import defaultdict
from typing import List


class Solution:
    def expand(self, S: str) -> List[str]:
        """
        Grab the elements that are meant to be inserted into the final string.
        for each instance of the new characters insert a new string into output which is a combination of the previous
        elements and the current.
        """

        str_idx = defaultdict(list)
        idx = 0
        ingest = False
        for char in S:
            if char == ',':
                continue
            if char == '{':
                ingest = True
            elif char == '}':
                # stop ingesting.
                ingest = False
                idx += 1
            elif ingest:
                str_idx[idx].append(char)
            else:
                str_idx[idx].append(char)
                idx += 1
        output = ['']
        for idx in range(len(str_idx)):
            tmp = []
            for char in str_idx[idx]:
                in_cp = output.copy()
                for j_idx in range(len(in_cp)):
                    tmp.append(in_cp[j_idx] + char)
            output = tmp

        return sorted(output)
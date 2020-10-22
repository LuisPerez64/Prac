"""
Question: https://leetcode.com/problems/add-bold-tag-in-string/
Given a string s and a list of strings dict, you need to add a closed pair
of bold tag <b> and </b> to wrap the substrings in s that exist in dict.
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag.
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:

Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:

Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

Constraints:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def addBoldTag(self, s: str, dictionary: List[str]) -> str:
        intervals = []
        for word in dictionary:
            idx = 0
            while True:
                idx = s.find(word, idx)
                if idx < 0:
                    break
                heappush(intervals, [idx, idx + len(word)])
                idx += 1
        if not intervals:
            return s

        # intervals.sort(key=lambda k: k[0])
        merged = [heappop(intervals)]
        while intervals:
            interval = heappop(intervals)
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        tmp = [x for x in s]
        for interval in merged[::-1]:
            tmp.insert(interval[1], '</b>')
            tmp.insert(interval[0], '<b>')
        return ''.join(tmp)

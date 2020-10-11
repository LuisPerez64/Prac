"""
Question: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.second_implementation(strs)

    def first_implementation(self, strs: List[str]) -> str:
        """
        Input is not guaranteed to be sorted. So sort the input to make comparisons simpler.
        At each point from the first element in the array where the next has a word that doesn't overlap
        decrement it.
        Mainly try a startswith at the current element, and if it's not then remove letters until it does.

        Time Complexity: O(n log n) + O(n * m)
            O(n log n): Sorting algo tim sort
            O(n * min(m)) => O(n * m): n being the size of the input strs and n being the smallest word in the array.
        Space Complexity: O(1)
            O(1): array is sorted in place (use heapsort if needed instead of tim sort)
        """
        strs.sort()
        # ensure that we start with the smallest common root.
        prefix = strs[0]
        for cur in strs[1:]:
            if len(prefix) == 0:
                break
            new_pref = ""
            # check to see the longest match that can be attained between the two strings.
            for idx in range(len(prefix)):
                if prefix[idx] == cur[idx]:
                    new_pref += prefix[idx]
                else:
                    break
            prefix = new_pref
        return prefix

    def second_implementation(self, strs: List[str]) -> str:
        """
        Input is not guaranteed to be sorted.
        The greatest common match would be the match between the shortest string in the array
        and the longest.
        In a sorted array these would be first and last strings.
        If there is anything that's uncommon between these two strings then it follows that any string
        inside their range would have the same differences.

        Time Complexity: O(2n) + O(m) => O(n + m)
            O(2n): calling the min/max functions to get the smallest and biggest string. Both of which are O(n)
            Could optimize it and iterate over the array to find them both in one pass.
            O(m): Iteration over the size of the smallest string in the group.
            Complexity becomes O(m) when the array is sorted.
        Space Complexity: O(1)
            O(1): array is sorted in place (use heapsort if needed instead of tim sort)
        """
        if not strs:
            return ""
        # Get the shortest possible string and the longest possible string.
        # O(2n)
        first = min(strs)
        last = max(strs)
        prefix = ""
        # O(m)
        for idx in range(len(first)):
            if first[idx] == last[idx]:
                prefix += first[idx]
            else:
                break
        return prefix

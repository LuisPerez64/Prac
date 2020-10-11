"""
Question: https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine
if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.second_implementation(s, wordDict)

    def first_implementation(self, s: str, wordDict: List[str]) -> bool:
        """
        Iterate over the word and create an intervals array based off of the start_end
        intervals of the bounds in the wordDict.
        """
        intervals = []
        # O(k * n)
        for word in wordDict:
            start = 0
            while start != -1:
                # keep finding intervals at which the current word is found.
                start = s.find(word, start)
                if start >= 0:
                    intervals.append([start, start + len(word)])
                    # Start the next interval after the word is found
                    # can't start at the words bound because of strings like "aaaaaa" dict ["aaa"]
                    start += 1
        if not intervals:
            return False
        # iterate over the intervals after sorting them...
        # Complexity: O(k * num_occ)
        intervals.sort(key=lambda k: (k[0], k[1]))
        # print(intervals)

        no_gap = intervals.pop(0)
        for interval in intervals:
            if no_gap[1] == interval[0]:
                no_gap[1] = interval[1]
        # print(no_gap, len(s))
        return no_gap[0] == 0 and no_gap[1] == len(s)

    def second_implementation(self, s: str, wordDict: List[str]) -> bool:
        """
        Backtracked solution. Try to create the word from the input strings
        making different combinations as the string is ingested.
        Time Complexity: O(n ^ 2)
            O(n): Iteration over the length of the word.
            O(n): The memoization takes a bite out of this but its still visiting the wordDict
                until each combination hits the end of the string.
                For a case "aaaaa...aaa" wordDict ["a","aa",...] without memoization recursion would be ~ 2^n
        """
        seen = set()

        def valid(cur_word):
            is_valid = cur_word not in seen and s.startswith(cur_word)
            seen.add(cur_word)
            return is_valid

        def backtrack(cur_word):
            if not valid(cur_word):
                return False

            if cur_word == s:
                return True

            for cur in wordDict:
                if backtrack(cur_word + cur):
                    return True
            return False

        return backtrack("")

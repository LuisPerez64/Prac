"""
REVISIT: The logic held here is in line with the find_all_anagrams_in_a_string problem. It's a good concept
    to hold on to, and short in a review standpoint.
Question: https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating
 letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.pulled_algorithm(s, k)

    def first_implementation(self, s: str, k: int) -> int:
        """
        Find the intervals from which the longest string can be
        created.
        """
        if not s:
            return 0

        intervals = []
        prev_char = s[0]
        prev_idx = 0
        for idx in range(1, len(s[1:])):
            char = s[idx]
            if char != prev_char:
                intervals.append([prev_idx, idx - 1, prev_char])
                prev_char = char
                prev_idx = idx

    def pulled_algorithm(self, s: str, k: int) -> int:
        """
        Scan the array with 2 pointers: left and right
        Store the frequency of each character
        Compute the replacement cost: cells count between left and right pointers - the highest frequency
            if the replacement cost <= k: update longest string size
            if the replacement cost > k: decrease frequency of character at left pointer;
                increase left pointer and repeat
        Since we are looking for the longest sub-string,
            we don't need to shrink the sliding window by more than 1 character:
        When we reach a window of size W, we know that our target window size
            is higher or equal to the current one ( >= W).
        Therefore, we could continue sliding with a window of W cells until we find a larger window > W.
        """
        left = 0
        frequency = defaultdict(int)
        max_len = 0
        for right in range(len(s)):
            # Iterate with a given window cataloging the frequency of the letters used to generate the current string.
            frequency[s[right]] += 1
            window_size = right - left + 1

            # Compute the replacement cost by comparing the number of cells in the window and the frequency of the
            # characters inside of it.
            if window_size - max(frequency.values()) <= k:
                max_len = max(max_len, window_size)
            else:
                # remove an instance of the leftmost value and increment the leftmost pointer.
                frequency[s[left]] -= 1
                left += 1
        return max_len

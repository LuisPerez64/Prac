"""
Question: https://leetcode.com/problems/implement-strstr/
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0


Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.first_implementation(haystack, needle)

    def first_implementation(self, haystack: str, needle: str) -> int:
        """
        Search for the first occurence of needles first element.
        If found then continue on this path as long as elements match.
        If they don't continue from the next element that was found in the current search that could be
        the next search start candidate. The next_start is determined by either there is another viable start
        candidate in the string that was just searched or there's no need to visit any of the strings in the given
        range as none satisfy the startswith condition so the search resumes at the end of the previous search attempt.
        Time Complexity: O(n - k) * O(k) => O((n-k) * k)
            O(n - k) => O(n): Iteration over the whole string in the worst case
            O(k / 2) => O(k): k = len(needle) and iterations to find the match based on the start and end of the string.
        """
        size_str = len(needle)
        if size_str == 0:
            return 0
        idx = 0
        "O(n) for the while loop iterating over the whole string"
        while idx + size_str - 1 < len(haystack):
            if haystack[idx] == needle[0]:
                t_idx = idx + 1
                t_idx_right = idx + size_str - 1
                n_idx = 1
                n_idx_right = size_str - 1
                # The next start is the index to resume searching from that could
                # yield the proper result. If it's not found in the string then
                # search from end of last sequence.
                next_start = None
                found = True
                "O(k / 2) where k = len of input string."
                while t_idx < len(haystack) and t_idx_right >= t_idx and n_idx_right >= n_idx:
                    if next_start is None and needle[0] == haystack[t_idx]:
                        next_start = t_idx
                    if haystack[t_idx] == needle[n_idx] and haystack[t_idx_right] == needle[n_idx_right]:
                        t_idx += 1
                        n_idx += 1
                        t_idx_right -= 1
                        n_idx_right -= 1
                    else:
                        found = False
                        break
                if found:
                    return idx
                # increment the index by the fail point as the substring doesn't exist in that bound?
                idx = next_start or t_idx
            else:
                # increment the index normally.
                idx += 1
        return -1

"""
Question: https://leetcode.com/problems/minimum-window-substring/
Given a string S and a string T, find the minimum window in S which will
    contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.first_implementation(s, t)

    def first_implementation(self, inp: str, seeking: str) -> str:
        """
        Using the frequency calculation to determine if a set of letters
        are within the wanted window.
        The window would start at the first instance of finding any of the
        characters in the seeking string.
        Question: Would there be a possibility of repetition in T, or would the characters be unique.
        If the characters are unique then a set would be used else we'd use a dict.
        For this instance there are multiple instances of the same char possible. The dict works for
        both cases the set/dict combo may be a bit faster though.
        """

        # initialize the frequency dictionaries. And the needed pointers in the window.
        frequency = defaultdict(int)
        s_freq = defaultdict(int)
        for x in seeking:
            s_freq[x] += 1
        freq_keys = s_freq.items()
        min_word = ""
        left = 0
        right = 0

        def handle_freq(char, op=1):
            if char in s_freq:
                frequency[char] += op

        def is_valid():
            # ensure that the values being sought exist at the minimum frequency needed for the current window.
            for key, value in freq_keys:
                if key not in frequency or frequency[key] < value:
                    return False
            return True

        while left < len(inp):
            # check if the window contains the right set of letters
            # ensuring that the minimum occurrence of each key is in the sought frequency range.

            if right >= len(inp) or (min_word and right - left >= len(min_word)):
                # can't search right anymore, start trimming the window from the left.
                # If the size of the window is greater than the size of the smallest match then shrink it.
                handle_freq(inp[left], -1)
                left += 1
            else:
                # Keep trying to ingest from the right hand side until we've exhausted this pointer
                # then we'll play catchup from the left hand pointer validating as needed.
                handle_freq(inp[right], 1)
                right += 1

            if is_valid():
                if not min_word:
                    min_word = inp[left:right]
                else:
                    min_word = min(min_word, inp[left:right], key=len)
            # print(left, right, min_word)

            if len(min_word) == len(seeking):
                # early break case as the len of the word being sought cannot be smaller than this.
                return min_word
        return min_word


"""
Test Cases:

"abc"
"b"
"abc"
"a"
"abc"
"c"
"ab"
"a"
"ADOBECODEBANC"
"ABC"
"a"
"aa"
"""

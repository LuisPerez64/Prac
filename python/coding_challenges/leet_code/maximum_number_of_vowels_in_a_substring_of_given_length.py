"""
Question: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1


Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
"""
from collections import defaultdict


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        return self.first_implementation(s, k)

    def first_implementation(self, inp: str, k: int) -> int:
        """
        Use the simplified frequency calculation for these.
        """
        freq = defaultdict(int)

        def handle_freq(idx, op=1):
            if idx >= len(inp):
                return
            if inp[idx] in 'aeiou':
                freq[inp[idx]] += op

        def get_count():
            return sum(freq.values())

        for left in range(k):
            handle_freq(left, 1)
        max_len = get_count()
        handle_freq(0, -1)

        for left in range(1, len(inp)):
            handle_freq(left + k - 1, 1)
            max_len = max(get_count(), max_len)
            handle_freq(left, -1)
        return max_len

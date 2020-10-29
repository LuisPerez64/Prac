"""
REVISIT: Solution was straightforward, and the main optimization of memoization boosted perf.
    Need to verify there's not a mathematical way to get this to a resolved state
Question: https://leetcode.com/problems/sentence-screen-fitting/
Given a rows x cols screen and a sentence represented by a list of non-empty words,
find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
"""
from functools import lru_cache
from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        num_repeats = 0
        idx = 0

        @lru_cache(maxsize=2 ** 16)
        def get_next_row(w_idx):
            reps = 0
            if len(sentence[w_idx]) > cols:
                return w_idx, 0
            cur = len(sentence[w_idx])
            cur_row = sentence[w_idx]
            w_idx += 1

            while True:
                if w_idx >= len(sentence):
                    reps += 1
                    w_idx = 0
                if cur + len(sentence[w_idx]) >= cols:
                    break
                cur_row += " " + sentence[w_idx]

                cur += len(sentence[w_idx]) + 1
                w_idx += 1
            return w_idx, reps

        for row in range(rows):
            idx, rep = get_next_row(idx)
            num_repeats += rep
        return num_repeats

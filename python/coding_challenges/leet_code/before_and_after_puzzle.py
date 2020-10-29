"""
NOTE: Leetcode is not accepting this though the answer is correct...
Question: https://leetcode.com/problems/before-and-after-puzzle/
Given a list of phrases, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of distinct strings sorted lexicographically.

Example 1:

Input: phrases = ["writing code","code rocks"]
Output: ["writing code rocks"]
Example 2:

Input: phrases = ["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]
Output: ["a chip off the old block party",
         "a man on a mission impossible",
         "a man on a mission statement",
         "a quick bite to eat my words",
         "chocolate bar of soap"]
Example 3:

Input: phrases = ["a","b","a"]
Output: ["a"]


Constraints:

1 <= phrases.length <= 100
1 <= phrases[i].length <= 100
"""
from typing import List


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        return self.first_implementation(phrases)

    def first_implementation(self, phrases: List[str]) -> List[str]:
        """
        Covert the phrases list into array of intervals after sorting based on the starting string.
        i.e. ["start_str", "end_str", phrase_idx]
        """
        phrases.sort()
        phrase_intervals = []
        phrase_ret = []
        for idx, phrase in enumerate(phrases):
            tmp = phrase.split(' ')
            phrase_intervals.append([tmp[0], tmp[-1], idx])
        idx = 0
        prev_phrase = None
        while idx < len(phrases):
            cur_phrase = phrases[idx]
            # Eliminate duplicates
            if prev_phrase == cur_phrase:
                idx += 1
                continue
            prev_phrase = cur_phrase
            cur_phrase = cur_phrase.split(' ')
            match_end = cur_phrase[-1]
            cur_phrase.pop()
            # Check if the phrase at the current index overlaps
            for start, end, idx_p in phrase_intervals:
                if idx == idx_p:
                    # Can't combine phrase with itself.
                    continue
                # if match_end > start:
                #     # Phrases are sorted so no other phrase could match.
                #     break
                if match_end == start:
                    tmp = phrases[idx_p].split(' ')
                    phrase_ret.append(" ".join(cur_phrase + tmp))
            idx += 1

        # for idx, phrase in enumeraate(phrases_intervals):
        return sorted(phrase_ret)

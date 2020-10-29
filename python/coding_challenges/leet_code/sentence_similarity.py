"""
Question: https://leetcode.com/problems/sentence-similarity/
We can represent a sentence as an array of words, for example,
the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and
given an array of string pairs similarPairs where similarPairs[i] = [xi, yi]
indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e. the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is not transitive.
For example, if the words a and b are similar and the words b and c are similar, a and c are not necessarily similar.



Example 1:

Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"],
similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1
is also similar to the corresponding word in sentence2.
Example 2:

Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
Output: true
Explanation: A word is similar to itself.
Example 3:

Input: sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
Output: false
Explanation: As they don't have the same length, we return false.


Constraints:

1 <= sentence1.length, sentence2.length <= 1000
1 <= sentence1[i].length, sentence2[i].length <= 20
sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.
0 <= similarPairs.length <= 1000
similarPairs[i].length == 2
1 <= xi.length, yi.length <= 20
xi and yi consist of lower-case and upper-case English letters.
All the pairs (xi, yi) are distinct.
"""
from collections import defaultdict
from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        sim_dict = defaultdict(set)
        if len(sentence1) != len(sentence2):
            return False
        # There could be multiple mappings to the same word...
        for idx, (a, b) in enumerate(similarPairs, 1):
            sim_dict[a].update([b, a])
            sim_dict[b].update([b, a])

        col = []
        idx = -1
        for word, word2 in zip(sentence1, sentence2):
            if word not in sim_dict:
                sim_dict[word].add(word)
                idx -= 1
            if word2 not in sim_dict[word] or word2 not in sim_dict[word]:
                # break out from here as they're not similar
                return False
        return True

"""
Question: https://leetcode.com/problems/sentence-similarity-ii/
Given two sentences words1, words2 (each represented as an array of strings),
and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"]
are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"],
["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar,
and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as
"fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"],
words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words.
So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

"""
from collections import defaultdict
from typing import List

from implementations.data_structures import DSU


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        sim_dict = defaultdict(set)
        if len(words1) != len(words2):
            return False
        # There could be multiple mappings to the same word...
        for idx, (a, b) in enumerate(pairs, 1):
            sim_dict[a].update([b, a])
            sim_dict[b].update([b, a])
        dsu = DSU()
        for word, word2 in zip(words1, words2):
            if word in sim_dict:
                continue
            if word not in sim_dict:
                sim_dict[word].add(word)
            if word2 not in sim_dict:
                sim_dict[word2].add(word2)

        for k, v in sim_dict.items():
            for u in v:
                dsu.union(u, k)

        for word, word2 in zip(words1, words2):
            xr = dsu.find(word)
            yr = dsu.find(word2)
            if xr != yr:
                return False
        return True

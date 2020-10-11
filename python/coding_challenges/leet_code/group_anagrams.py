"""
Question: https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
from collections import defaultdict
from typing import List

from implementations.utils.list_utils import prod_list


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.second_implementation(strs)

    def first_implementation(self, strs: List[str]) -> List[List[str]]:
        """
        Place the strings in buckets under a sorted key.
        Using a hashmap to get their proper location in the dict bucket.
        Return the dict bucket
        Time Complexity: O(n * k log k)
            O(n): Iteration over the input strings
            O(k log k): Sorting the strs

        """
        buckets = defaultdict(list)

        # O(n)
        for cur in strs:
            # O( k log k)
            tmp = sorted(cur)
            buckets[tuple(tmp)].append(cur)

        return list(buckets.values())

    def second_implementation(self, strs: List[str]) -> List[List[str]]:
        """
        Eliminate the need to sort by assigning a weight to each letter in the alphabet.
        Can't use their order as 'c' => 'ab' in that case.
        Using prime numbers and their multiplied values producing unique hashes.
        Brings the complexity from O(n * k log k) => O(nk)
        """
        primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31,
                  'l': 37, 'm': 41, 'n': 43, 'o': 47, 'node_p': 53, 'node_q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73,
                  'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
        buckets = defaultdict(list)
        for cur in strs:
            buckets[prod_list([primes[c] for c in cur])].append(cur)

        return list(buckets.values())

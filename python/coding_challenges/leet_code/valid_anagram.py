"""
Question: https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Store the counted values of each letter from one string and place them into a hash map.
        Iterate over the next string removing an occurence of the letter from the hash maps count.
        If at any point the letter isn't found to exist in the map,
        or removing one of its elements yields < 0 occurs left its invalid.

        Time Complexity: O(2n) => O(n)
        Space Complexity: O(n)
        """
        from collections import defaultdict

        if len(s) != len(t):
            return False
        # Create a defaultdict of type int to eliminate the setdefault calls.
        occurs = defaultdict(int)
        total = 0
        for x in s:
            # occurs.setdefault(x, 0)
            occurs[x] += 1
            total += 1

        for x in t:
            if x not in occurs:
                return False
            occurs[x] -= 1
            # if occurs[x] == 0:
            #     occurs.pop(x)
            if occurs[x] < 0:
                return False
            total -= 1

        return total == 0

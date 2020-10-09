"""
Question: https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Create a get index function to pull the logic for scrapping the non_alphanum chars out
        Use the indexing function to get the left/right indices until left >= right pointer meaning we've
        reached the center of the string and its valid.
        Time Complexity: O(n)
            The while loop inside of the get_next_alphanumeric function will still not yield more than n loops
        Space Complexity: O(1)
        """
        left = 0
        right = len(s) - 1

        def get_next_alphanumeric(start: int, last: int, operation: int):
            """
            helper function to get to the next alphanumeric element.

            @param start: starting index to attempt to get the char
            @param last: point at which the char would be overlapping the other bound
            @param operation: dictates if we're adding or subtracting and is either 1, or -1
            """
            while start != last:
                if s[start].isalnum():
                    break
                start += operation
            return start

        while left < right:
            left = get_next_alphanumeric(left, right, 1)
            right = get_next_alphanumeric(right, left, -1)
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

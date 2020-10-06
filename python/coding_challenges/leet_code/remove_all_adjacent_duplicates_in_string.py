"""
Question: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters,
 and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal,
and this is the only possible move.  The result of this move is that the string is "aaca",
of which only "aa" is possible, so the final string is "ca".
Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        # return self.first_implementation(S)
        return self.second_implementation(S)

    def first_implementation(self, inp_str: str) -> str:
        """
        Using a sliding window that can move <> throught the input.
        If the elements at left/right match then remove them.
        Decreasing the windows slice just in case the new adjacent chars are duplicates.
        If the values are distinct then increment both boundaries
        """
        left = 0
        right = 1
        inp_arr = [x for x in inp_str]
        while True:
            if right >= len(inp_arr):
                break
            if inp_arr[left] == inp_arr[right]:
                inp_arr.pop(right)
                inp_arr.pop(left)
                if left - 1 >= 0:
                    # Shift the window back
                    left -= 1
                    right -= 1
            else:
                left += 1
                right += 1

        return ''.join(inp_arr)

    def second_implementation(self, inp_str: str) -> str:
        """
        Same as the first implementation but no conversion of the string to an array.
        Using a sliding window that can move <> throught the input.
        If the elements at left/right match then remove them.
        Decreasing the windows slice just in case the new adjacent chars are duplicates.
        If the values are distinct then increment both boundaries
        """
        left = 0
        right = 1
        while True:
            if right >= len(inp_str):
                break
            if inp_str[left] == inp_str[right]:
                inp_str = inp_str[:left] + inp_str[right + 1:]

                if left - 1 >= 0:
                    # Shift the window back
                    left -= 1
                    right -= 1
            else:
                left += 1
                right += 1
        return inp_str

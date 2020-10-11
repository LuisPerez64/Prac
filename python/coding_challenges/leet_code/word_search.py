"""
REVISIT: Explanation of the backtracking algorithm
Question: https://leetcode.com/problems/word-search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.first_implementation(board, word)

    def first_implementation(self, board: List[List[str]], word: str) -> bool:
        """
        Each cell in the grid has to be visited in the worst case, or maybe only up til the letters that remain are
        of smaller size than the length of the word being sought?
        """
        num_rows = len(board)
        num_cols = len(board[0])

        # if num_rows * num_cols < len(word):
        #     return False

        def backtrack(row: int, col: int, suffix):
            if len(suffix) == 0:
                # All letters have been found for the word being sought.
                return True

            # Do some bounds checking of the directions the
            # Indices won''t cause out of bounds errors, and that the current element is the one being sought
            if row < 0 or row == num_rows or col < 0 or col == num_cols \
                    or board[row][col] != suffix[0]:
                return False

            # the current letter being sought is matched.
            # Continue the operations marking that this cell should not be revisited.
            board[row][col] = '#'
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                    return True
            # unmark the work that's been done so another attempt could visit this cell
            board[row][col] = suffix[0]
            return False

        for row_start in range(len(board)):
            for col_start in range(len(board[0])):
                if backtrack(row_start, col_start, word):
                    return True
        return False

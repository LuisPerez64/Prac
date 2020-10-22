"""
REVISIT: Fix the first implementation up.
Question: https://leetcode.com/problems/alphabet-board-path/
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
You may return any path that does so.



Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"


Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        return self.second_implementation(target)

    def first_implementation(self, target: str) -> str:
        """
        Create the board with fillers for the boundaries that exist.
        Maybe creating an adjacency grid to relay where each node in the
        graph can point to.
        We can resolve the question with the divmod functionality.
        It's a circular sorted list...
        """
        # Place the letters in their grid points
        c = 0
        alpha_dict = {}
        for row in range(6):
            for col in range(5):
                alpha_dict[chr(ord('a') + c)] = (row, col)
                c += 1
        move_list = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
        cur_node = (0, 0)
        sequence = ''
        for char in target:
            to_node = alpha_dict[char]
            move_x = to_node[0] - cur_node[0]
            move_y = to_node[1] - cur_node[1]
            cur_node = to_node
            while move_x != 0:
                if move_x > 0:
                    # Move to the left
                    move_x -= 1
                    sequence += 'D'
                else:
                    move_x += 1
                    sequence += 'U'
            while move_y != 0:
                if move_y > 0:
                    move_y -= 1
                    sequence += 'R'
                else:
                    move_y += 1
                    sequence += 'L'
            sequence += '!'
        return sequence

    def second_implementation(self, target: str) -> str:
        m = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0: res.append('L' * int(y0 - y))
            if x < x0: res.append('U' * int(x0 - x))
            if x > x0: res.append('D' * int(x - x0))
            if y > y0: res.append('R' * int(y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)

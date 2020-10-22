"""
REVISIT: The permutation problems are a bit hit/miss at the moment need more practice.
Question: https://leetcode.com/problems/letter-tile-possibilities/
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can
make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1

"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Iterate over the string finding the possible combinations made from n amount
        of inputs.
        Combinations are
        cur + new, new + cur,
        """

        seen = set()

        def dfs(path, possible):
            if path in seen:
                return
            # print(locals())
            seen.add(path)
            for idx in range(len(possible)):
                # try the combinations of the string that are possible.
                # send out the slice with the substrings not including self.
                dfs(path + possible[idx], possible[:idx] + possible[idx + 1:])

        dfs('', tiles)
        # Remove the empty set
        seen.remove('')
        return len(seen)

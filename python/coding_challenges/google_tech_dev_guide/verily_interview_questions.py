"""
Interview 1
"""
from collections import deque
from heapq import heappushpop, heappush
from typing import List, Dict

inp_arr = ["CAT", "CUT", "DOG", "CATS", "CATERWAUL", "CATER", "COT"]


class Trie(object):
    end_marker = '#'
    free_match = '?'

    def __init__(self, words: List[str]) -> None:
        self.root: Dict[str, dict or str] = dict()
        for word in words:
            self.insert(word=word)

    def __str__(self):
        return str(self.root)

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root:
                root[char] = dict()
            root = root[char]
        root[self.end_marker] = word

    def search(self, word: str):
        root = self.root
        for char in word:
            if char not in root:
                return False
            root = root[char]
        is_end = self.end_marker in root
        return is_end

    def findMatches(self, word):
        ret_list = []

        def rec_search(wrd, cur_root):
            if len(wrd) == 0:
                if self.end_marker in cur_root:
                    ret_list.append(cur_root[self.end_marker])
                return

            ch = wrd[0]
            if ch in cur_root:
                rec_search(wrd[1:], cur_root[ch])
            elif ch == self.free_match:
                for child in cur_root.values():
                    rec_search(wrd[1:], child)

        rec_search(word, self.root)
        return ret_list


tmp = Trie(inp_arr)
print(tmp.search('CAT'), tmp.search('CAR'), tmp.search('CA'))
print(tmp.findMatches('C?T'), tmp.findMatches('C??'))
print(tmp.findMatches('FAT'))

"""
Interview 2
"""

"""
        *
* - - - *
*     * *
* * * * * *
-----------
3 1 1 2 4 1 5

        
*    
*     * 
* * * * * *
-----------
3 1 1 2 1 1
"""


def main(inp_arr: List[int]) -> int:
    """
    Base Cases:
      if all equivalent then 0 sum
      if left pointer reaches a value that's higher than the current right grab the area and move right to left
    """
    if len(inp_arr) <= 1:
        return 0
    left = 0
    right = 1
    total_area = 0
    dq = deque()
    while left <= right and right < len(inp_arr):
        if inp_arr[left] > inp_arr[right]:
            right += 1
            dq.append(inp_arr[left] - inp_arr[right])
        else:

            left = right
    return total_area


"""
Interview 3
# Suppose you’re at a gallery buying some art.
# The gallery has assigned each artwork a minimum price,
# and a "quality" score.
# You must pay at least the minimum price for each artwork,
# and if you buy more than one piece of art, the price
# you pay for each
# must be proportional to their relative quality score. For example,
# if artwork A has quality 1 and min-price $20, and artwork B has quality 2 and min-price $30,
# if you buy artwork A for $20, you must pay exactly $40
# to buy artwork B to fulfill the proportionality requirement.

# Q: Implement a function that takes a list of artworks and returns the amount of money you’ll
# need to buy all of them.
#
# Example:
#      Quality  Min Price  Actual Price
# A    1        10            20
# B    2        40            40
# C    5        50           100
#
# Total Price: ???
"""


def get_price(quality: List[int], price) -> int:
    """

    """
    q_ratio = float('-inf')
    for q, p in zip(quality, price):
        q_ratio = max(p / q, q_ratio)

    return sum(q * q_ratio for q in quality)


# print(get_price([1,2,5], [10, 40, 50]))

"""
// Q2 : Suppose you only need to buy K of the artworks. 
// In addition, there is an artwork you must buy (indicated by index i), 
// and you must pay exactly minimum price. You should still satisfy 
// the min price and proportionality rules. Implement a function that 
// returns the minimum amount you will need to spend. 
//
// Example with above artworks, i=1, k=2: ???
#      Quality  Min Price 
# A    1        30        
# B    2        40        
# C    5        50        
"""


def get_price_2(quality, price, must_buy, max_buys):
    """
    Get the ratio for the explicitly given element in the array

    """
    p_ratio = price[must_buy] / quality[must_buy]
    total = price[must_buy]
    buy = []
    for idx, (p, q) in enumerate(zip(price, quality)):
        if idx == must_buy:
            continue

        if buy and len(buy) >= max_buys - 1:
            heappushpop(buy, -q * p_ratio)
        else:
            heappush(buy, -q * p_ratio)
    return total + sum(-x for x in buy)


print(get_price_2([1, 2, 5], [10, 40, 50], 1, 2))

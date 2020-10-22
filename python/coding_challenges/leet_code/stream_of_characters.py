"""
REVISIT: The concept of the suffix trie being implemented here is a good one to look into.
Question: https://leetcode.com/problems/stream-of-characters/
mplement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the
last k characters queried (in order from oldest to newest,
including this letter just queried) spell one of the words in the given list.


Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist


Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""

# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self._stream_gen = self._cur_word_gen(words)
#         next(self._stream_gen)

#     def _cur_word_gen(self, words):
#         """
#         Create a generator to maintain the state instead of passing variables back/forth.
#         """
#         mark = '$'
#         trie_root = dict()
#         for word in words:
#             cur_root = trie_root
#             for letter in word:
#                 cur_root = cur_root.setdefault(letter, {})
#             cur_root[mark] = mark
#         match_count = 0
#         cur_root = trie_root

#         while True:
#             # Try to match against the current word. If words 'of' and 'off' in the stream
#             # then we continue until we find something that just doesn't match
#             letter = yield
#             # print('letter', letter)
#             if letter is StopIteration:
#                 return match_count
#             if letter not in cur_root:
#                 cur_root = trie_root
#                 if letter not in cur_root:
#                     yield False
#                     continue
#             cur_root = cur_root[letter]
#             valid = mark in cur_root
#             match_count += 1 if valid else 0
#             yield valid

#     def query(self, letter: str) -> bool:
#         valid = self._stream_gen.send(letter)
#         next(self._stream_gen)
#         return valid

# #self._stream_gen.send(letter)


# # Your StreamChecker object will be instantiated and called as such:
# # obj = StreamChecker(words)
# # param_1 = obj.query(letter)
from collections import deque
from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if ch not in node:
                return False
            node = node[ch]
        return '$' in node

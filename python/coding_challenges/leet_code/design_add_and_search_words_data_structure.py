"""
Question: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
 word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""

class DictNode(object):
    def __init__(self):
        self.child_nodes = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur_node = self.root
        for char in word:
            node = cur_node.child_nodes.get(char, DictNode())
            # Set the node back into its root struct and continue
            cur_node.child_nodes[char] = node
            cur_node = node
        cur_node.is_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(self.root, word)

    def _search(self, cur_node: 'TrieNode', word: str) -> bool:
        for idx, char in enumerate(word):
            char = word[idx]
            if char == '.':
                # If we encounter a '.' then check across all of the child nodes for the next char in the word.
                # done recursively, and bubbles up.
                for child in cur_node.child_nodes.values():
                    if self._search(child, word[idx+1:]):
                        return True
                return False
            else:
                node = cur_node.child_nodes.get(char)
            if not node:
                return False
            cur_node = node
        return cur_node.is_end



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
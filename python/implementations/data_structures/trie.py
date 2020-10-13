"""
Implementation of the Trie and TrieNode classes.
Used in decision making algorithms and basically produces an ordered graph object.
"""
__all__ = ["TrieNode", "Trie"]


class TrieNode(object):
    """
    TrieNode object which is the basis of the Trie.
    A Trie will have n Trie Nodes to branch off from.
    """

    def __init__(self):
        self.child_nodes = {}
        self._is_end = False

    def set_is_end(self, is_end=True):
        self._is_end = is_end

    def get_is_end(self) -> bool:
        return self._is_end


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Create a node structure that will hold the data wanted from the pool.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for char in word:
            node = cur_node.child_nodes.get(char, TrieNode())
            # Just in case a new node was created make sure it's linked to the current nodes root.
            cur_node.child_nodes[char] = node
            cur_node = node
        cur_node.set_is_end()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for char in word:
            node = cur_node.child_nodes.get(char)
            if not node:
                return False
            cur_node = node
        return cur_node.get_is_end()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for char in prefix:
            node = cur_node.child_nodes.get(char)
            if not node:
                return False
            cur_node = node
        return True

    def match(self, word: str) -> bool:
        """
        Same as the search but allows for wildcard matching based on '.'
        i.e. 'cat' in Trie  'c.t' will be found.
        """

        def helper(cur_node: TrieNode, inp_str: str) -> bool:
            for idx, char in enumerate(inp_str):
                char = inp_str[idx]
                if char == '.':
                    # If we encounter a '.' then check across all of the child nodes for the next char in the inp_str.
                    # done recursively, and bubbles up.
                    for child in cur_node.child_nodes.values():
                        if helper(child, inp_str[idx + 1:]):
                            return True
                    return False
                else:
                    node = cur_node.child_nodes.get(char)
                if not node:
                    return False
                cur_node = node
            return cur_node.is_end

        return helper(cur_node=self.root, inp_str=word)

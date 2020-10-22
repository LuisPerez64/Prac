"""
Question: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Serialization is the process of converting a data structure or object into a sequence of bits so that it can
be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
 in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a
 string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
 need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

from implementations.data_structures import TreeNode


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        Encode the binary tree in level order traversal format.
        Fill in the Null fields as needed.
        If the tree's value could be an extended data structure then it opens up
        a few more venues regarding marshalling/unmarshalling the data and would
        require a bit more tooling.

        Implied nodes will hold integers for their values.
        """

        return ','.join([str(x) for x in self.level_order_traversal(root)])

    def deserialize(self, data: str) -> TreeNode or None:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        nodes = deque([None if val == 'null' else TreeNode(int(val))
                       for val in data.split(',')])

        # Create a second deque to hold the structure of the nodes relationship to their parents.
        child_nodes = deque(nodes)
        root = child_nodes.popleft()
        for node in nodes:
            if node:
                if child_nodes:
                    node.left = child_nodes.popleft()
                if child_nodes:
                    node.right = child_nodes.popleft()
        return root

    def level_order_traversal(self, root: TreeNode):
        """
        Traverse the nodes in the Tree within the level order.
        root,left_child,right_child
        If the left or right child is None then null will be placed in the tree.
        """
        if not root:
            return []
        dq = deque([root])
        level = 0
        result = []
        while dq:
            level_length = len(dq)
            for nde in range(level_length):
                cur_node = dq.popleft()
                if cur_node:
                    result.append(cur_node.val)
                else:
                    result.append('null')
                    continue

                dq.append(cur_node.left)
                dq.append(cur_node.right)
            if not [x for x in dq if x is not None]:
                break
        return result

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

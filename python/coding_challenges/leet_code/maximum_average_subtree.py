"""
Question: https://leetcode.com/problems/maximum-average-subtree/

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants.
The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:
Input: [5,6,1]
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.


Note:

The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
"""
from typing import Tuple

from implementations.data_structures import TreeNode


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        return self.first_implementation(root)

    def first_implementation(self, root: TreeNode) -> float:
        """
        Do a postorder traversal of the tree and get the max_average at each path.
        If we're looking at a leaf then we return just the leaf's average.
        At every subtree evaluate the possible sum for each of the nodes.
        If any leaves exist then subtree average is root + the children.

        Had to do this recursively as the postorder traversal doesn't allow for much leeway.
        """
        if not root:
            return 0

        def get_max_average(node) -> Tuple[int, float, float]:
            if not node:
                return 0, 0, 0

            n_l, v_l, m_l = get_max_average(node.left)
            n_r, v_r, m_r = get_max_average(node.right)
            node_count = n_l + n_r + 1
            tally = node.val + v_l + v_r
            return node_count, tally, max(tally / float(node_count), m_l, m_r)

        nc, cur_tally, max_av = get_max_average(root)
        return max_av

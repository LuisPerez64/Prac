"""
Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes node_p and node_q as
the lowest node in T that has both node_p and node_q as descendants (where we allow a node to be a descendant of itself).”
Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], node_p = 2, node_q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], node_p = 2, node_q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], node_p = 2, node_q = 1
Output: 2


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
node_p != node_q
node_p and node_q will exist in the BST.

"""
from implementations.data_structures import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.first_implementation(root, p, q)

    def first_implementation(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Since this is a BST and is implied to be in order.
        We can check if a node fits the ancestor property through BST search.
        If at any point the root == the min or max value being sought then its the root.
        if the root is the mid point between the two nodes min < root < max then its the first common ancestor.
        Else if the value at root > max search to the left of it, or to the right if its < min
        """

        min_, max_ = min(q.val, p.val), max(q.val, p.val)

        while root:
            if root.val in [max_, min_] or root.val < max_ and root.val > min_:
                # Found the location where it's most likely the ancestor.
                return root
            if root.val > max_:
                # search to the left
                root = root.left
            else:
                root = root.right

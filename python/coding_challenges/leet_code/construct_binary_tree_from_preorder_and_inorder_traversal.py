"""
REVISIT: The second implementation is short and concise. Pull from that one.
Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List

from implementations.data_structures import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.second_implementation(preorder, inorder)

    def first_implementation(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Find the pattern.
        Preorder => root,left,right
        Inorder => left,root,right
        The Preorder establishes the root node.
        Pattern: p_idx =0, i_idx = 0, p_o = [3,9,20,15,7], i_o = 9,3,15,20,7, seen = []
            1) Root from PreOrder =>p_o[p_idx] => 3, p_idx +=1 => [3. []]
            2) Get Node from InOrd => i_idx = idx_of_3 = 1, i_o[i_idx-1] => 9 => [3, [9]]
            3) p_idx = idx_of_9 = 1 => p_o[p_idx + 1] =>
        """

        def get_tree_structure():
            tree_struct = []
            seen = set()
            p_idx = 0
            i_idx = 0
            in_order_idx = {val: idx for idx, val in enumerate(inorder)}
            while p_idx < len(preorder) and i_idx < len(inorder):
                tmp_p = preorder[p_idx]

                if tmp_p not in seen:
                    seen.add(tmp_p)
                    tree_struct.append(tmp_p)
                i_idx = inorder.index(tmp_p) - 1
                tmp_i = inorder[i_idx]
                if tmp_i not in seen:
                    seen.add(tmp_i)
                    tree_struct.append(tmp_i)
                p_idx = preorder.index(tmp_i) + 1

        return get_tree_structure()

    def second_implementation(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Logic is maintained from the first implementation. Find the root based on the PreOrder
        list and then find it in the InOrder list. Which will give the left/right nodes for the
        value.
        """

        # Create the map to not rely on index searching through the list each time through.
        in_order_map = {num: idx for idx, num in enumerate(inorder)}

        def helper(left_idx, right_idx):
            nonlocal pre_idx
            if right_idx == left_idx or pre_idx >= len(preorder):
                return

            # pre_order table denotes the root node to append
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            # Get the two child nodes from inorder array.
            in_order_idx = in_order_map[root_val]

            root.left = helper(left_idx, in_order_idx)

            root.right = helper(in_order_idx + 1, right_idx)
            return root

        pre_idx = 0
        return helper(left_idx=0, right_idx=len(inorder))

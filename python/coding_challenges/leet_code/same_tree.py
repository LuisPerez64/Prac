"""
Question: https://leetcode.com/problems/same-tree/
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
from collections import deque
from typing import List

from implementations.data_structures import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.third_implementation(p, q)

    def first_implementation(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Do a level order traversal of both trees and return if they're equivalent.
        This is a modified format that will place a 'null' in empty node locations
        The comparison of the two trees is just list equivalency..
        Could do the comparisons in one iteration instead and verify at each level.
        Time Complexity: O(n)
        Space Complexity: O( 2(n +log n)) => O(n)
            O(log n) for the queue in a perfectly balanced list. else O(n)
            O(n) for the levels array returned.
        """

        def level_order_traversal(root: TreeNode, with_null=True):
            if not root:
                return []
            levels = []
            level = 0
            queue = [root]
            while queue:
                level_length = len(queue)

                for idx in range(level_length):
                    cur_node = queue.pop(0)
                    cur_val = 'null'
                    if cur_node:
                        cur_val = cur_node.val

                    levels.append(cur_val)
                    if not cur_node:
                        continue
                    if cur_node.left or with_null:
                        queue.append(cur_node.left)
                    if cur_node.right or with_null:
                        queue.append(cur_node.right)
                level += 1

            return levels

        return level_order_traversal(p) == level_order_traversal(q)

    def second_implementation(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Do an inorder traversal of both trees and see if the array they produce is the same.
        Time Complexity: O(2n) => O(n)
        Space Complexity: O(n)
        """
        if not p and not q:
            # Two empty trees are equivalent.
            return True
        if not p or not q:
            # One empty tree and a populated tree
            return False

        def in_order_traverse(cur_root) -> List[int or None]:
            """
            Traverse the trees in order Left, Root, Right
            Adding in padding for when the right node is null seems a bit of an anti pattern.
            Time Complexity: O(n)
            Space Complexity: O(n)
            """
            # already handled the null root case above but
            if not cur_root:
                return []
            stack = []
            result = []
            while True:

                while cur_root:
                    # keep ingesting left nodes until the last child is found.
                    # placing the parent onto the stack before going to the child.
                    stack.append(cur_root)
                    cur_root = cur_root.left

                if cur_root is None and stack:
                    cur_root = stack.pop()
                    # add the left value into the results.
                    result.append(cur_root.val)
                    # place the pointer to the right node (which should be empty)
                    cur_root = cur_root.right
                    # Handle cases where the right is populated and left is not.
                    result.append(cur_root and cur_root.val or None)

                if not stack and not cur_root:
                    break
            return result

        return in_order_traverse(p) == in_order_traverse(q)

    def third_implementation(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Same as first approach but without the added space for the
        levels array and comparisons are done in place.
        Time Complexity: O(n)
        Space Complexity: O(2 log n) => O(log n)
        """
        if not p and not q:
            # Two empty trees are equivalent.
            return True
        if not p or not q:
            # One empty tree and a populated tree
            return False
        queue = deque([p, q])

        while queue:
            p_node = queue.popleft()
            q_node = queue.popleft()
            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False
                queue.append(p_node.left)
                queue.append(q_node.left)
                queue.append(p_node.right)
                queue.append(q_node.right)
            elif p_node or q_node:
                # One of them is pointing to a NULL node
                return False

        return True

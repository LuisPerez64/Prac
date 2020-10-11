"""
REVISIT: Good recursion use case, and technically DP solution, but not in full.
NOTE: Pretty proud of coming up with this solution in ~ 5 minutes
Question: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
from implementations.data_structures import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.first_implementation(root)

    def first_implementation(self, root: TreeNode) -> int:
        """
        A path is defined as any connected path that does not visit the same node twice.
        i.e. left -> parent -> right, left -> parent -> parent, right -> parent -> parent
        Max value possible at a node is calculated through:
            max(left + parent, right + parent, parent)
            With a closed cycle maximum found through either a combination of the current node and its children
                or a single node.
                max(cur_max_closed_cycle, left + right + parent, parent, left, righ)
        """
        neg_inf = float('-inf')
        closed_cycle = [neg_inf]

        def get_max_sum(cur_root) -> int or float:
            """
            Handle the possible combinations and return the max sum from the current selection.
            Returns the max value in the current cycle (children (and their children) + parent)
            updates the max closed_cycle.
            """
            if not cur_root:
                return neg_inf
            par = cur_root.val
            left = get_max_sum(cur_root.left)
            right = get_max_sum(cur_root.right)

            closed_cycle[0] = max(closed_cycle[0], left + right + par, par, left, right)
            cur_max = max(left + par, right + par, par)
            # print(cur_root, cur_max)
            return cur_max

        return max(get_max_sum(root), closed_cycle[0])

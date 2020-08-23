from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: Any = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.iterative_solution(root)

    def recursive_solution(self, cur_root: TreeNode) -> List[int]:
        cur_val = []
        if cur_root:
            cur_val.append(cur_root.val)
            cur_val.extend(self.recursive_solution(cur_root.left))
            cur_val.extend(self.recursive_solution(cur_root.right))

        return cur_val

    def iterative_solution(self, cur_root: TreeNode) -> List[int]:
        parent_nodes = []
        val = []
        if not cur_root:
            return []
        parent_nodes.append(cur_root)

        while parent_nodes:
            cur_root = parent_nodes.pop()
            val.append(cur_root.val)
            if cur_root.right:
                parent_nodes.append(cur_root.right)
            if cur_root.left:
                parent_nodes.append(cur_root.left)

        return val


sol = Solution()
root_node = TreeNode(val='F',
                     left=TreeNode(val='B',
                                   left=TreeNode(val='A'),
                                   right=TreeNode(val='D',
                                                  left=TreeNode(val='C'),
                                                  right=TreeNode(val='E'))),
                     right=TreeNode(val='G',
                                    right=TreeNode(val='I',
                                                   left=TreeNode(val='H'))))

print(sol.iterative_solution(cur_root=root_node))

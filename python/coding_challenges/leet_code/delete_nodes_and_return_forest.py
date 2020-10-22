"""
REVISIT: Pull the functions for deletion, and create adjacency relations for future use.
Question: https://leetcode.com/problems/delete-nodes-and-return-forest/

Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Constraints:
The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""
from typing import Dict, Union, List

from implementations.data_structures import TreeNode, DSU


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        return self.first_implementation(root, to_delete)

    def first_implementation(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """
        Find the nodes that exist in the tree and what they're connected to.
        Using UnionFind to grab the roots after finding the adjacency matrix for the tree.
        """

        def get_adjacency(root, delete_nodes: List[int] = None):
            adjacency = []

            def helper(node, parent):
                if not node:
                    return
                tmp = [parent.val, node.val]
                if delete_nodes:
                    for idx in range(len(tmp) - 1, -1, -1):
                        if tmp[idx] in delete_nodes:
                            tmp.pop(idx)
                    if len(tmp) == 1:
                        tmp += tmp
                if tmp:
                    adjacency.append(tmp)

                helper(node.left, parent=node)
                helper(node.right, parent=node)

            helper(root, root)
            return adjacency

        def delete_nodes(root):
            """
            Recursively delete the nodes wanted. Afterwards returns a list of the tree nodes
            that are new roots.
            """

            roots: Dict[int, Union[TreeNode, None]] = {}
            dsu = DSU()
            for u, v in adjacency:
                dsu.union(u, v)

                # Mark each of the roots and store their value to grab them on the deletion traversal
                roots[dsu.find(u)] = None
                roots[dsu.find(v)] = None

            def helper(node):
                # Delete the nodes in the tree while preserving the children.
                if not node:
                    return False
                if node.val in roots:
                    # Capture the node as a new root value.
                    roots[node.val] = node
                if helper(node.left):
                    node.left = None
                if helper(node.right):
                    node.right = None
                return node.val in to_delete

            if helper(root):
                # the root node itself may have been marked for deletion.
                root.left = None
                root.right = None
            return list(roots.values())

        adjacency = get_adjacency(root, delete_nodes=to_delete)

        return delete_nodes(root)

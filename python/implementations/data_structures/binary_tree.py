"""
REVISIT: Review all of these methods until they are damn near second nature.
Binary Tree Node to be used as the base for Binary Trees.
Implementation of multiple operations on the data structure.
"""

__all__ = ['TreeNode']

from typing import Any, List

from implementations.utils.list_utils import flatten_list


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.filled = False

    def __str__(self):
        levels = self.level_order_traversal(self, True)
        return str(levels)

    @property
    def height(self):
        if not self:
            return 0
        root = self
        stack = [(1, root)]
        depth = 0

        while stack:
            cur_d, cur_root = stack.pop()
            if cur_root:
                depth = max(depth, cur_d)
                stack.append((cur_d + 1, cur_root.left))
                stack.append((cur_d + 1, cur_root.right))
        return depth

    @classmethod
    def level_order_traversal(cls, root: 'TreeNode', with_null=False, partitioned: bool = True):
        if not root:
            return []
        levels = []
        level = 0
        queue = [root]
        while queue:
            levels.append([])
            level_length = len(queue)

            for idx in range(level_length):
                cur_node = queue.pop(0)
                cur_val = 'null'
                if cur_node:
                    cur_val = cur_node.val

                levels[level].append(cur_val)
                if not cur_node:
                    continue
                if cur_node.left or with_null:
                    queue.append(cur_node.left)
                if cur_node.right or with_null:
                    queue.append(cur_node.right)
            level += 1

        return levels if partitioned else flatten_list(levels)

    @classmethod
    def pre_order_traversal(cls, root: 'TreeNode'):
        """
        Postorder traversal sequence: Left, Right, Root
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            cur_root = stack.pop()
            result.append(cur_root.val)
            if cur_root.right:
                stack.append(cur_root.right)
            if cur_root.left:
                stack.append(cur_root.left)

        return result

    @classmethod
    def in_order_traversal(cls, root: 'TreeNode'):
        """
        Inorder traversal sequence: Left, Root, Right

        """
        if not root:
            return []
        stack = []
        result = []
        cur_root = root
        while True:
            while cur_root:
                stack.append(cur_root)
                cur_root = cur_root.left
            if cur_root is None and stack:
                cur_root = stack.pop()
                result.append(cur_root.val)
                cur_root = cur_root.right

            if len(stack) == 0 and cur_root is None:
                break
        return result

    @classmethod
    def post_order_traversal(cls, root: 'TreeNode'):
        """
        PostOrder Traversal sequence: Left,Right,Root
        """
        if not root:
            return []
        root_nodes = [root]
        result = []
        while root_nodes:
            cur_root = root_nodes.pop()
            result.insert(0, cur_root.val)

            if cur_root.left:
                root_nodes.append(cur_root.left)
            if cur_root.right:
                root_nodes.append(cur_root.right)
        return result

    @classmethod
    def insert(cls, head, element: list):
        for val in element:
            stack = [head]
            node = cls(val=val)
            while stack:
                root = stack.pop()
                if not root.left:
                    root.left = node
                elif not root.right:
                    root.right = node
                else:
                    stack.append(root)
                    stack.append(root.right)
                    stack.append(root.left)
                    continue
                break

    @classmethod
    def same_tree(cls, root_a: 'TreeNode', root_b: 'TreeNode'):
        tree_a = cls.level_order_traversal(root=root_a, with_null=True, partitioned=True)
        tree_b = cls.level_order_traversal(root=root_b, with_null=True, partitioned=True)
        return tree_a == tree_b

    @classmethod
    def invert_tree(cls, root):
        """
        Maybe this method shouldn't have side effects?
        Invert the Binary tree.
        1 <- 2 -> 3  => 3 <- 2 -> 1
        """
        if not root:
            return

        def swap_children(parent: TreeNode):
            """
            This will do the swapping based on a given nodes children.
            """
            if not parent:
                return
            tmp_node = parent.left
            parent.left = parent.right
            parent.right = tmp_node

        queue = [root]
        while queue:
            cur_root = queue.pop()
            swap_children(cur_root)
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    @classmethod
    def lowest_common_ancestor(cls, root: 'TreeNode', node_p: 'TreeNode', node_q: 'TreeNode'):
        """
        Start from the root node and traverse the tree.
        Until we find node_p and node_q both, keep storing the parent pointers in a dictionary.
        Once we have found both node_p and node_q, we get all the ancestors for node_p using the parent dictionary and
        add to a set called ancestors.
        Similarly, we traverse through ancestors for node node_q.
        If the ancestor is present in the ancestors set for node_p, this means this is the first ancestor
        common between node_p and node_q (while traversing upwards) and hence this is the LCA node.
        """

        stack = [root]
        parents = {root: None}

        while node_p not in parents or node_q not in parents:
            # Keep searching until both are in the dict.
            # Doing a level order traversal until both sides are exhausted.
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)

        # Create an ancestors set to grab all of the ancestors for the individual nodes.
        ancestors = set()

        # Grab all of the parents that lead up to P
        while node_p:
            ancestors.add(node_p)
            # Find the current ancestors parent until we get all the way to the root node.
            node_p = parents[node_p]

        while node_q not in ancestors:
            # Keep going up the to the parent node for node_q as long as its not in Ps ancestors list.
            # We'll either get to a common node or reach the point where node_q == root.
            node_q = parents[node_q]

        return node_q

    @classmethod
    def create_from_pre_order_in_order_traversal(cls, preorder: List[Any], inorder: List[Any]):
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

"""
REVISIT: Review all of these methods until they are damn near second nature.
Binary Tree Node to be used as the base for Binary Trees.
Implementation of multiple operations on the data structure.
"""

__all__ = ['TreeNode']

from collections import deque
from typing import Any, List, Dict, Union

from implementations.data_structures import DSU
from implementations.utils.list_utils import flatten_list


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.filled = False

    def __str__(self):
        levels = self.level_order_traversal(self, with_null=True, partitioned=False)
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
    def create_from_list(cls, data):
        """
        Create a Binary Tree from a list.
        Format for the list [root, left, right, left.left, left.right,right.left, right.right,...]
        Example: [1,2,3,'null','null',4,5]
        """
        if not data:
            return None

        nodes = deque([None if val == 'null' or val is None else TreeNode(int(val))
                       for val in data])

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
        levels = [lvl for lvl in levels if not all(val == 'null' for val in lvl)]
        return levels if partitioned else flatten_list(levels)

    @classmethod
    def pre_order_traversal(cls, root: 'TreeNode'):
        """
        Pre Order traversal sequence: Left, Right, Root
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
        stack = [root]
        stack_2 = []
        result = []
        while stack:
            node = stack.pop()
            stack_2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while stack_2:
            result.append(stack_2.pop())
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

    @classmethod
    def get_adjacency(cls, root, delete_nodes: List[int] = None):
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

    @classmethod
    def delete_nodes(cls, root: 'TreeNode', to_delete: List[int]) -> List['TreeNode']:
        """
        Recursively delete the nodes wanted. Then returns a list of the tree nodes that are marked as new roots.
        """
        adjacency = cls.get_adjacency(root=root, delete_nodes=to_delete)

        roots: Dict[int, Union['TreeNode', None]] = {}
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

            if node.val in to_delete:
                # The node is marked for deletion.
                # If it is to be deleted then the parent will handle it.
                # the child nodes are left untouched, but traversed for any further operations.
                helper(node.left)
                helper(node.right)
                return True

            # We cut the link from the parent to its children if either of them are pointing to a node that was deleted.
            if helper(node.left):
                node.left = None
            if helper(node.right):
                node.right = None
            return node.val in to_delete

        if helper(root):
            # The root node itself may have been marked for deletion. Handle this case here.
            root.left = None
            root.right = None
        return list(roots.values())
#
# def drawtree(root):
#     def height(root):
#         return 1 + max(height(root.left), height(root.right)) if root else -1
#
#     def jumpto(x, y):
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#
#     def draw(node, x, y, dx):
#         if node:
#             t.goto(x, y)
#             jumpto(x, y - 20)
#             t.write(node.val, align='center', font=('Arial', 12, 'normal'))
#             draw(node.left, x - dx, y - 60, dx / 2)
#             jumpto(x, y - 20)
#             draw(node.right, x + dx, y - 60, dx / 2)
#
#     import turtle
#     t = turtle.Turtle()
#     t.speed(0)
#     turtle.delay(0)
#     h = height(root)
#     jumpto(0, 30 * h)
#     draw(root, 0, 30 * h, 40 * h)
#     t.hideturtle()
#     turtle.mainloop()
#
#
# if __name__ == '__main__':
#     drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
#     drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))

"""
REVISIT: Review all of these methods until they are damn near second nature.
Binary Tree Node to be used as the base for Binary Trees.
Implementation of multiple operations on the data structure.
"""

__all__ = ['TreeNode']


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.filled = False

    def __str__(self):
        elements = self.level_order_traversal(root=self, with_null=True)
        levels = [[]]
        level = 0
        for elt in elements:
            level_length = 2 ** level
            if len(levels[level]) == level_length:
                level += 1
                levels.append([])
            levels[level].append(elt)
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

    # @classmethod
    # def create_from_list(cls, inp_list: list):
    #     if not inp_list:
    #         return None
    #     # List formatted in level_order [1,2,None,3,None,None,None] and the elements are inserted into the first empty
    #     root_node = cls(val=inp_list[0])
    #     stack = [root_node]
    #     while stack:
    #         for idx in range(len(stack)):
    #             pass
    #     for idx, elt in enumerate(inp_list[1:]):
    #         if idx % 2 == 0:
    #             # insert into left and move to the next node
    #         else:
    #             # insert into right

    @classmethod
    def level_order_traversal(cls, root: 'TreeNode', with_null=False):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            for idx in range(len(queue)):
                cur_node = queue.pop(0)
                result.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                elif with_null:
                    result.append('null')
                if cur_node.right:
                    queue.append(cur_node.right)
                elif with_null:
                    result.append('null')

        return result

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
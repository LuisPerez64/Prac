"""
Creation of base data structure nodes, and when applicable generating small helper functions that occur accross
 implementations.
"""


class ListNode(object):
    """
    List Node object. To be used when dealing with Singly/Doubly Linked Lists
    For Singly Linked Lists do not populate the prev_node value.
    """

    def __init__(self, val=0, next_node=None, prev_node=None, next=None, prev=None):
        self.val = val
        self.next = next_node or next
        self.prev = prev_node or prev

    def __str__(self):
        ret_list = []
        cur_node = self
        while cur_node:
            ret_list.append(str(cur_node.val))
            cur_node = cur_node.next
        return ' -> '.join(ret_list)

    def __len__(self):
        cur_node = self
        size = 0
        while cur_node:
            size += 1
            cur_node = cur_node.next
        return size

    @classmethod
    def convert_from_list(cls, inp_list):
        head_node = cls(val=inp_list[0], next_node=None)
        cur_node = head_node
        for x in inp_list[1:]:
            cur_node.next = cls(val=x, next_node=None)
            cur_node = cur_node.next
        return head_node


class TreeNode(object):
    """
    Binary Tree Node to be used as the base for Binary Trees
    """

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    #     # List formatted in level_order [1,2,None,3,None,None,None]
    #     root_node = cls(val=inp_list[0])
    #     cur = root_node
    #     for node in inp_list[1:]:
    #         cur_root.left

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

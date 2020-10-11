# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from implementations.data_structures import TreeNode


class Codec:
    def pre_order_traversal(self, root: 'TreeNode'):
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

    def in_order_traversal(self, root: 'TreeNode'):
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

    def recreate_from_pre_order_in_order(self, preorder, inorder):
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

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        Do an Inorder and PreOrder traversal of the tree.
        Store those two arrays in a comma separated string.
        """
        ret_str = ""
        pre_order = self.pre_order_traversal(root)
        in_order = self.in_order_traversal(root)
        return ",".join([str(x) for x in pre_order + in_order])

    def deserialize(self, data: str) -> TreeNode or None:
        """Decodes your encoded data to tree.
        Create the BST from the pre_order and in_order traversal of the data.
        Deserialize if through a split. And segment the data into two equal lists.
        """
        cur = [x for x in data.split(',') if x]
        if not cur:
            return None
        cur = [int(x) for x in cur]
        split = len(cur) // 2
        return self.recreate_from_pre_order_in_order(cur[:split + 1], cur[split:])

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

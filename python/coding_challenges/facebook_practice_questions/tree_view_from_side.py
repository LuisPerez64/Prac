"""
Given a tree root. Return the nodes that would be able to be seen if the
tree was viewed from one of it's sides (left/right)
i.e.
            4
           / \
          1   2
               \
                3
Produces [4,2,3] if viewed from the right, and [4,1,3] if from the left
"""
from collections import deque
from implementations.data_structures import TreeNode


def view_from_the_side(root: TreeNode, view=-1):
    if not root:
        return []
    result = []
    dq = deque([root])
    while dq:
        result.append(dq[view].val)
        for _ in range(len(dq)):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return result

tree = TreeNode.create_from_list([4,1,2,None, None, None, 3])
print(view_from_the_side(tree, 0))
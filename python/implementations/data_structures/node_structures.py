"""
Creation of base data structure nodes, and when applicable generating small helper functions that occur accross
 implementations.
"""


class ListNode(object):
    """
    List Node object. To be used when dealing with Singly/Doubly Linked Lists
    For Singly Linked Lists do not populate the prev_node value.
    """

    def __init__(self, val=0, next_node=None, prev_node=None,next=None, prev=None):
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

    @classmethod
    def create_from_list(cls, inp_list):
        pass

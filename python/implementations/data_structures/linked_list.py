"""
List Node object. To be used when dealing with Singly/Doubly Linked Lists
For Singly Linked Lists do not populate the prev_node value.
"""

__all__ = ['ListNode']


class ListNode(object):
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

    # def __len__(self):
    #     cur_node = self
    #     size = 0
    #     while cur_node:
    #         size += 1
    #         cur_node = cur_node.next
    #     return size

    @property
    def size(self):
        pass


    @classmethod
    def convert_from_list(cls, inp_list):
        head_node = cls(val=inp_list[0], next_node=None)
        cur_node = head_node
        for x in inp_list[1:]:
            cur_node.next = cls(val=x, next_node=None)
            cur_node = cur_node.next
        return head_node

"""
List Node object. To be used when dealing with Singly/Doubly Linked Lists
For Singly Linked Lists do not populate the prev_node value.
"""

__all__ = ['ListNode']


# noinspection PyShadowingBuiltins
class ListNode(object):
    def __init__(self, val=0, next_node=None, prev_node=None, next=None, prev=None, random=None, down=None):
        self.val = val
        self.next = next_node or next
        self.prev = prev_node or prev
        self.random = random
        self.down = down

    def __str__(self):
        ret_list = []
        cur_node = self
        while cur_node:
            ret_list.append(str(cur_node.val))
            cur_node = cur_node.next
        return ' -> '.join(ret_list)

    def __len__(self) -> int:
        """
        Get the len/size of the linked list. If it's a cyclic list returns -1
        """
        has_cycle = self.check_if_cycle(self)
        count = 0
        if not has_cycle:
            head = self
            while head:
                count += 1
                head = head.next
            return count
        return -1

    @classmethod
    def convert_from_list(cls, inp_list):
        head_node = cls(val=inp_list[0], next_node=None)
        cur_node = head_node
        for x in inp_list[1:]:
            cur_node.next = cls(val=x, next_node=None)
            cur_node = cur_node.next
        return head_node

    @classmethod
    def check_if_cycle(cls, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            # Increment the second pointers as needed.
            slow = slow.next
            fast = fast.next.next
        return True

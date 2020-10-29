"""
Question: https://leetcode.com/problems/reorder-list/
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
from collections import deque

from implementations.data_structures import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        return self.first_implementation(head)

    def first_implementation(self, head: ListNode) -> None:
        """
        Constraint: Do not return anything, modify head in-place instead.
        Iterate over the list and place all of its nodes into a deque.
        Based on the idx % 0 pop from the left or right making the nodes point to their next element
        """
        if not head:
            return
        nodes = deque()
        while head:
            nodes.append(head)
            head = head.next

        head = nodes.popleft()
        idx = 0
        while nodes:
            idx += 1

            if idx % 2 == 0:
                # pop from the start
                node = nodes.popleft()
            else:
                node = nodes.pop()
            # Remove the history of the node to avoid circular paths (even if temporary)
            node.next = None
            head.next = node
            head = head.next


print(Solution().reorderList(head=ListNode.convert_from_list([1, 2, 3, 4])))

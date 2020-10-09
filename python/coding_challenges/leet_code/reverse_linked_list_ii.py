"""
REVISIT: The concept is there, just need to drill it in some more and find the importance of the
    two added pointers.
Question: https://leetcode.com/problems/reverse-linked-list-ii/
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

from implementations.data_structures import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        return self.first_implementation(head, m, n)

    def first_implementation(self, head: ListNode, start_idx: int, end_idx: int) -> ListNode:
        """
        Iterate over the LinkedList until the start_idx is met.
        Grab the pointers for correction in case the swaps don't occur from the 0th index the prev node
        could cause a cycled list to get produced
        Iterate once more until the end_idx is met doing swaps of adjacent nodes
        """
        if start_idx == end_idx or not head:
            return head
        prev = None
        cur = head
        while start_idx > 1:
            prev = cur
            cur = cur.next
            start_idx -= 1
            end_idx -= 1

        tail = cur
        reconnect = prev

        while end_idx:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            end_idx -= 1
        if reconnect:
            reconnect.next = prev
        else:
            head = prev
        tail.next = cur
        return head

    # def second_implementation(self, head: ListNode, start_idx: int, end_idx: int) -> ListNode:
    #     """
    #     Using a queue to ingest the list nodes after the start point
    #     and reverse them as needed when popping off of said queue.
    #     """
    #     if start_idx == end_idx or not head:
    #         return head
    #     from collections import deque
    #     nodes = deque()
    #     cur = head
    #     last_node = cur
    #     while start_idx > 1:
    #         start_idx -= 1
    #         end_idx -= 1
    #         last_node = cur
    #         cur = cur.next
    #
    #     while end_idx:
    #         end_idx -= 1
    #         nodes.append(cur)
    #         cur = cur.next
    #     if cur is None:
    #         # Running into an issue with reversing the list in full.
    #         head = last_node
    #         ret = head
    #         while nodes:
    #             cur = nodes.pop()
    #             cur.next = None
    #             head.next = cur
    #             head = head.next
    #         return ret
    #     else:
    #         while nodes:
    #             node = nodes.pop()
    #             next_node = node.next
    #             last_node.next = next_node
    #             last_node = node
    #
    #         last_node.next = cur
    #         return head


node_r = ListNode.convert_from_list([1, 2, 3, 4, 5])
print(Solution().reverseBetween(head=node_r, m=2, n=4))

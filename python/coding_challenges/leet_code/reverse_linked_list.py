"""
Question: https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from collections import deque

from implementations.data_structures import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.first_implementation(head)
        # return self.second_implementation(head)

    def first_implementation(self, head: ListNode) -> ListNode:
        """
        Push nodes onto a deque as long as they have a next node
        The last node in the list becomes the new head.
        Pop nodes off of the deque appending them to the linked list.
        Time Complexity: O(n-1) + O(n) => O(n)
        Space Complexity: O(n-1)
            Deque will grow to the size of the input listNode
        """
        if not head:
            return head
        nodes = deque()

        while head.next:
            nodes.append(head)
            head = head.next
        c = head
        while nodes:
            cur = nodes.pop()
            cur.next = None
            head.next = cur
            head = head.next
        return c


    def second_implementation(self, head: ListNode) -> ListNode:
        """
        Go through the list with three pointers prev, cur, next
        Do in place swapping of the nodes until the last node is found.
        return the pointer to the previous node as the current node should be pointing to null
        Time Complexity: O(n)
        Space Complexity: O(3) => O(1)
        """
        if not head:
            return head
        prev = None
        cur = head

        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n

        return prev

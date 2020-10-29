"""
REVISIT: The implementation of the cyclic list from the separate heads is worth reviewing.
Question: https://leetcode.com/problems/intersection-of-two-linked-lists/
Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not
be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5].
From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.

"""
from implementations.data_structures import ListNode


class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> ListNode:
        return self.first(head1, head2)

    def first(self, head1, head2):
        """
        Modify the list to create a cycle, then find the node that exists in that cycle.
        Once we find an instance of the two nodes being the same iterate over the cycled list
        until we get to an element that's different.
        Break out and rever the changes made to the input lists.
        """
        if not head1 and not head2:
            return head1
        if not head1 or not head2:
            return None
        tmp_h = head1
        while head1.next:
            head1 = head1.next
        # concatenate the two linked lists. Appending The start of the 2nd list to the end of the firsts.
        head1.next = head2
        s_p = f_p = tmp_h
        while f_p and f_p.next:
            f_p = f_p.next.next
            s_p = s_p.next
            if s_p == f_p:
                # Found an intersection point. Now find the start
                f_p = tmp_h
                while f_p != s_p:
                    # Since it's a cyclic list we're not going to meet the null pointer
                    # iterate over these until they no longer point to the same value
                    # this is the second stage of the fast/slow pointer as we have s_p inside the cycle and
                    # f_p needs to reach it. If we're at the start of the cycle i.e. 0 -> 2 -> null and 0-> null
                    # we'd just never enter this loop.
                    f_p, s_p = f_p.next, s_p.next
                head1.next = None
                return s_p
        head1.next = None
        return None

    def second(self, head1, head2):
        """
        Simulate the tortoise and hare solution with independent node pointers.
        Two pointer solution to the problem. We iterate over the two lists.
        If the two lists intersect then they share the same last node. If they don't then we break out
        of the loop.
        """
        if not head1 and not head2:
            return head1
        if not head1 or not head2:
            return None
        pa = head1
        pb = head2

        va = None
        vb = None

        while pa != pb:
            pa = head2 if pa is None else pa.next
            pb = head1 if pb is None else pb.next
            if pa and pa.next is None and va is None:
                va = pa
            if pb and pb.next is None and vb is None:
                vb = pb
        return pa

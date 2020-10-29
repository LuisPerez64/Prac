"""
Question: https://leetcode.com/problems/copy-list-with-random-pointer/
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer
points to, or null if it does not point to any node.


Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.


Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.
"""
from implementations.data_structures.linked_list import ListNode as Node


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        return self.first_implementation(head)

    def first_implementation(self, head: Node) -> Node:
        """

        Iterate over the linked list, and interleave the Nodes that are there with their copy.
        For each of those nodes then point to the random node the original node pointed to, and get its next value.
            Since we're basically skipping the node and the new node is at position node.next
        Unlink the two lists, returning the original list to the structure it had initially, and a completely separate
            new linked list.
        e.g. format : [[Node, IndexOfRand], ...]  input = [[7, None], [13, 0], [10, 1]]
            representation:
                NEXT: 7 -> 13 -> 10
                RAND: 7 -> None 13 -> 7 10 -> 13
                JOIN: 7 -> 7' -> 13 -> 13' -> 10 -> 10' -> None
            random pointer of any node would then be orig_node.random.next if it exists else None
        """
        if not head:
            return head

        def interleave(node):
            if node:
                new_node = Node(val=node.val, next=node.next, random=None)
                node.next = new_node

        pointer = head
        while pointer:
            interleave(pointer)
            pointer = pointer.next.next

        pointer = head
        while pointer:
            # Point the new node to the random pointer for the value before it.
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next

        # Iterate over the list once more, and unlink the interleaved nodes.
        ret = head.next
        old = head
        new = head.next
        while old:
            # Set the values in the original list to point back to where they pointed before.
            # no need to check the existence of a next node for the original list as its guaranteed with the interweave
            old.next = old.next.next
            # Reattach the new node values next pointers without the old list's values
            new.next = new.next.next if new.next else None

            old = old.next
            new = new.next

        return ret

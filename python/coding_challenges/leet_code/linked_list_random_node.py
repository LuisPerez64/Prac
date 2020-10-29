"""
Question: https://leetcode.com/problems/linked-list-random-node/
Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
"""
from random import randint

from implementations.data_structures import ListNode


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        head = self.head
        count = 0
        result = None
        # TC: O(n * log2 n)
        # The random.randint runs at O(log n) TC based on the number of bits held in the N val
        while head:
            # Use reservoir sampling to select a given node in the current range.
            count += 1
            choice = randint(1, count)
            if choice == 1:
                # elect a new node
                result = head.val
            head = head.next
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
Question: https://leetcode.com/problems/linked-list-cycle/
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""
from implementations.data_structures import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return self.second_implementation(head)

    def first_implementation(self, head: ListNode) -> bool:
        """
        Collect the nodes and place them into a bucket.
        If the current node points to a node in the bucket
        then its been visited before. Continue the check until list is exhausted or node exists.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        l_bucket = set()
        while head:
            if head in l_bucket:
                return True
            l_bucket.add(head)
            head = head.next
        return False

    def second_implementation(self, head: ListNode) -> bool:
        """
        Use two pointers one incrementing by 1 step the other by 2.
        If the two pointers ever intersect then there's a cycle in place.
        i.e. input [1,2,3,2,5] # input[n] relays the node they're pointing to in the list
            0) slow = 0->1, fast = 0->2
            1) slow = 1->2, fast = 2->3->2
                # They're both pointing to the same node. There's a cycle.
        """
        if not head:
            return False
        if not head.next:
            # Base case list of one node with no next pointer
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
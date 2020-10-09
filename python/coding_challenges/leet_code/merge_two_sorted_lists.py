"""
Question: https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""
from implementations.data_structures import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time Complexity: O(n + m) ~> O(n)
            The m/n being the length of the two lists
        Space Complexity: O(n)
            The space required for the second array

        Move through the two lists and move the pointer on the smaller one until both the lists are exhausted
        """
        h = float('inf')
        ret_node = cur_node = None

        def get_val(node: ListNode):
            if node:
                return node.val
            return h

        while l1 or l2:
            l1_val = get_val(l1)
            l2_val = get_val(l2)

            if l1_val < l2_val:
                l1 = l1.next
            else:
                l2 = l2.next

            next_node = ListNode(min(l1_val, l2_val))
            if ret_node is None:
                ret_node = next_node
                cur_node = next_node
            else:
                cur_node.next = next_node
                cur_node = cur_node.next

        return ret_node

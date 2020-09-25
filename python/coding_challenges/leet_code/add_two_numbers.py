"""
Question: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
from implementations.data_structures.node_structures import ListNode


class Solution:

    @classmethod
    def first_implementation(cls, l1: ListNode, l2: ListNode):
        """
        Time Complexity: O(n)
            Iterates over both lists and finds the longest of them to use as the baseline.
        Space Complexity: O(n + 1)
            Creation of a new linked list of the size of the input list + 1 at most for the overflow value.
        """
        ret_linked_list = None
        head_node = None
        carry_over = None

        def get_val(l_node):
            # For the case of one list being longer than the other the calculation will yield 0 for its value
            ret_val = 0
            if l_node:
                ret_val = l_node.val
                l_node = l_node.next
            return ret_val, l_node

        while l1 or l2:
            # Ingest the values from the list until both are exhausted
            l1_val, l1 = get_val(l1)
            l2_val, l2 = get_val(l2)
            # Add the two values and if needed append the carry_over from the previous calculation
            # This will be ingested after this loop if it still exists so 9 + 9 => 18 => 8 -> 1 in the list
            cur_val = l1_val + l2_val + (carry_over or 0)
            if cur_val >= 10:
                # The div mod operation will return the current value along with its remainder.
                carry_over, cur_val = divmod(cur_val, 10)
            else:
                carry_over = None

            node = ListNode(val=cur_val, next=None)
            if ret_linked_list is None:
                ret_linked_list = node
                head_node = ret_linked_list
            else:
                ret_linked_list.next = node
                ret_linked_list = ret_linked_list.next

        if carry_over is not None:
            ret_linked_list.next = ListNode(val=carry_over, next=None)

        return head_node


print(Solution.first_implementation(l1=ListNode.convert_from_list([2, 4, 3]),
                                    l2=ListNode.convert_from_list([5, 6, 4])))

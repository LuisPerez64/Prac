"""
REVISIT: The concepts are solid for the second implementation, but need to do a brute force third implementation.
Question: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.



(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]


Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""

from implementations.data_structures.node_structures import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        return self.first_implementation(head)

    def first_implementation(self, head: ListNode) -> ListNode:
        """
        """

        # Gather the elements into a list initially to make the operations more comfortable
        values = []
        compliments = {}
        while head:
            values.append(head.val)
            compliments[head.val] = 0 - head.val
            head = head.next

        # Slide back/forth in the window if a pair of values becomes 0 move the start idx back
        start = 0
        end = 1
        while True:
            if start > len(values) - 1 and end >= len(values):
                break
            if values[start] + values[end] == 0:
                values.remove(end)
                values.remove(start)
            else:
                start += 1
                end += 1
        if values:
            head = ListNode(val=values[0])
            cur = head
            for elt in values[1:]:
                cur.next = ListNode(val=elt)
                cur = cur.next
        return head

    def second_implementation(self, head: ListNode) -> ListNode:
        """
        Inspired by this discussion comment.
        https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/414285/Python-easy-to-understand-solution-with-explanations

        Run Notes for Input [1,2,-3,3,1]
        We start with the 0 value to ensure that we have the base case in the dict.

        The sequence creates a dictionary with the keys generated from the summation on the sequence pointing to nodes
            that hold the next sought after value. The list below are the list nodes in list format.
            Creates {0: [-3,3,1], 1: [1,2,-3,3,1], 3: [3, 1], 4: [1]}
        When we iterate over the generated node we find the locations where an accumulated sum is found.

        """

        ret_node = ListNode(val=0)
        compliments = {0: ret_node}
        cur_sum = 0
        ret_node.next = head

        while head:
            cur_sum += head.val
            compliments[cur_sum] = head
            head = head.next

        head = ret_node
        cur_sum = 0
        while head:
            cur_sum += head.val
            # Find the next accumulated sequence where the current sum is found
            head.next = compliments[cur_sum].next
            head = head.next
        return ret_node.next


print(Solution().second_implementation(head=ListNode.convert_from_list([4, 1, 2, -3, 3, 1])))

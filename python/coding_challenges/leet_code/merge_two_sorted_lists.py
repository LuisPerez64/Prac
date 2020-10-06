from implementations.data_structures.node_structures import ListNode


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

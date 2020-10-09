"""
REVISIT: Just as a refresher. The code in itself is straight forward.

Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/?currentPage=1&orderBy=hot&query=&tag=python-3

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
from implementations.data_structures import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode or None:
        return self.first_implementation(head, n)

    def first_implementation(self, head: ListNode, n: int) -> ListNode or None:
        """
        Iterate over the full list to find its size, and place its nodes references
        in a dict with their index as the key.
            NOTE: Could also use a stack and then pop until N elements are found but thats a possible 2nd pass
        Subtract n from the idx(last index in the list) to get the node that needs to be replaced and get its previous pointer
        Make that nodes next point to the deleted nodes next index.

        Edge cases
         -> n == index meaning removal of the first node making its node.next be the new root.
         -> n == index == 1: Size of the  linked list is 1 and its only node is being removed. Retun empty list.

        Time Complexity: O(n) + O(1) => O(n)
            Single Pass through the list and a hashmap get operation O(1)
        Space Complexity: O(n)
            Dict holding all of the nodes in the input list needs to be created.
        """
        node_dict = {0: None}
        ret_node = head
        idx = 0
        while head:
            node_dict[idx] = head
            head = head.next
            idx += 1

        if n == idx:
            # Return the list with the exclusion of its first node. If list of size 1 then returns None
            return node_dict.get(1, None)

        # Find the index of the node preceding the last i.e. list idx is 5 removing idx - 1 yields the fourth node
        # subtract one more from this to get to its previous nodes pointer, and set that ones "next" to the node at
        # idx + 1 - n. If this is the last node from the list being removed then it will simulate a pop operation.
        node_dict[idx - n - 1].next = node_dict.get(idx - n + 1, None)
        return ret_node


print(Solution().removeNthFromEnd(head=ListNode.convert_from_list([1,2,3]), n=3))

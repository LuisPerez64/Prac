"""
Question: https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

"""
from typing import List

from implementations.data_structures import ListNode


def first_implementation(lists: List[ListNode]) -> ListNode:
    head_node = None
    ret_node = None
    while True:
        cur_min = None
        cur_idx = 0
        for idx in range(len(lists)):
            cur_list_head = lists[idx]
            if cur_list_head is None:
                continue
            if cur_min is None:
                cur_min = cur_list_head
                continue
            if cur_min.val < cur_list_head.val:
                cur_min = cur_list_head
                cur_idx = idx
        if cur_min is None:
            # No list had a value to ingest
            break
        if head_node is None:
            head_node = cur_min
            ret_node = cur_min
        else:
            head_node.next = cur_min
            head_node = head_node.next
        lists[cur_idx] = lists[cur_idx].next

    return ret_node


def second_implementation(lists: List[ListNode]) -> ListNode or None:
    """
    Ingest the lists into a heap through the heap sort algorithm
    Time Complexity: O(nk) + O(n log n) + O(n) + O(n) -> O(3n) + O(n log n) -> O(n) + O(n log n) -> O(n log n )
        O(n * k) - Iterate over the list (n) of listNodes (k)
        O(n * log(n)) - Heapify
        O(n) - Iteration over the k elements in the list into a flattened structure of length n
        O(n) - Creation of the final LinkedList with the heappop
    Space Complexity: O(n)
        O(n) - min_heap size as it will ingest all elements in the flattened list
    """

    from heapq import heapify, heappop
    min_heap = []

    for idx in range(len(lists)):
        # O(n * k)
        # for the size of the initial list * the length of each Linked List
        head_node = lists[idx]
        while head_node is not None:
            min_heap.append(head_node.val)
            head_node = head_node.next
    if len(min_heap) == 0:
        return None
    # Heapify algorithm Time Complexity O(n * log(n))
    heapify(min_heap)
    head_node = ListNode(val=heappop(min_heap), next_node=None)
    cur_node = head_node

    while min_heap:
        # TC: O(n-1) -> O(n) - Iterate over the whole heap
        cur_node.next = ListNode(val=heappop(min_heap), next_node=None)
        cur_node = cur_node.next

    return head_node


def third_implementation(lists: List[ListNode]) -> ListNode or None:
    """
    Ingest the lists into a heap through the heap sort algorithm
    Time Complexity: O(nk) + O(n log n) + O(n) + O(n) -> O(3n) + O(n log n) -> O(n) + O(n log n) -> O(n log n)
        O(n * k) - Iterate over the list (n) of listNodes (k)
        O(n) - Iteration over the k elements in the list into a flattened structure of length n
        O(n) - Creation of the final LinkedList with the heappop
    Space Complexity: O(n)
        O(n) - min_heap size as it will ingest all elements in the flattened list
    """

    from heapq import heappush, heappop
    min_heap = []

    for idx in range(len(lists)):
        # Time Complexity: O(n * k) -> O(nk) * O(1)
        # for the size of the initial list * the length of each Linked List
        head_node = lists[idx]
        while head_node is not None:
            # O(1) - Heap push average case worst case O(log(n))
            heappush(min_heap, head_node.val)
            head_node = head_node.next
    if len(min_heap) == 0:
        return None
    head_node = ListNode(val=heappop(min_heap), next_node=None)
    cur_node = head_node

    while min_heap:
        # TC: O(n-1) -> O(n) - Iterate over the whole heap
        cur_node.next = ListNode(val=heappop(min_heap), next_node=None)
        cur_node = cur_node.next

    return head_node


def fourth_implementation(lists: List[ListNode]) -> ListNode or None:
    """
    Time Complexity: O(nk) * O(k) -> O(n * k^2)
        -- Time complexity grows with the number of lists given, and the trade off in space vs time diminishes.
    Space Complexity: O(1) as the nodes are swapped around in place.
    """

    def get_min_node() -> ListNode or None:
        min_node = None
        min_idx = -1
        for idx, node in enumerate(lists):
            if node and (min_node is None or node.val < min_node.val):
                min_node = node
                min_idx = idx

        if min_node:
            # Place the pointer into an accessor, point the pointer to the new accessor location (next),
            # return the new accessor
            tmp_node = min_node.next
            min_node.next = None
            lists[min_idx] = tmp_node

        return min_node

    cur_min_node = get_min_node()
    if cur_min_node is None:
        return None

    head_node = cur_min_node
    cur_node = head_node

    while True:
        cur_min_node = get_min_node()
        if cur_min_node is None:
            break
        cur_node.next = cur_min_node
        cur_node = cur_node.next

    return head_node


if __name__ == '__main__':
    long_test = [[7], [49], [73], [58], [30], [72], [44], [78], [23], [9], [40], [65], [92], [42], [87], [3], [27],
                 [29], [40], [12], [3], [69], [9], [57], [60], [33], [99], [78], [16], [35], [97], [26], [12], [67],
                 [10], [33], [79], [49], [79], [21], [67], [72], [93], [36], [85], [45], [28], [91], [94], [57], [1],
                 [53], [8], [44], [68], [90], [24], [96], [30], [3], [22], [66], [49], [24], [1], [53], [77], [8], [28]]
    ret_list = third_implementation([ListNode.convert_from_list(x) for x in long_test])

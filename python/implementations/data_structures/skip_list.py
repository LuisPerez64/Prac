"""
Implementation of the SkipList Probabilistic Data Structure
In computer science, a skip list is a probabilistic data structure that allows
O(log n) search/insertion time complexity within an ordered sequence of n elements.
Thus it can get the best features of a sorted array (for searching) while maintaining a
linked list-like structure that allows insertion, which is not possible in an array.
Fast search is made possible by maintaining a linked hierarchy of subsequences,
with each successive subsequence skipping over fewer elements than the previous one.
Searching starts in the sparsest subsequence until two consecutive elements have been found,
one smaller and one larger than or equal to the element searched for.
Via the linked hierarchy, these two elements link to elements of the next sparsest subsequence,
where searching is continued until finally we are searching in the full sequence.
The elements that are skipped over may be chosen probabilistically or deterministically
with the former being more common.

Resources:
* https://en.wikipedia.org/wiki/Skip_list
* http://cglab.ca/~morin/teaching/5408/refs/p90b.pdf

Operations:
* Search(x) :
* Insert(x) :
* Delete(x) :
"""
from .linked_list import ListNode as Node


class SkipList(object):
    def __init__(self):
        self.levels = []
        self.head = Node(val=float('-inf'))

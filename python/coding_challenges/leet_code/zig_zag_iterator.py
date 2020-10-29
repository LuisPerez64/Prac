"""
REVISIT: Base generator function usage
Given two 1d vectors, implement an iterator to return their elements alternately.



Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements
 returned by next should be: [1,3,2,4,5,6].

Follow up:
What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].

"""
from typing import List, Generator


class ZigzagIterator:
    def __init__(self, *inp_lists: List[int]):
        """
        Create a generator to yield the needed values instead of
        preprocessing on the initial call of the constructor.

        Due to the check in the hasNext function. We have to store
        the next yielded value else we'd lose it in between the calls.
        """
        self._generator = self._cycle_list(*inp_lists)
        self._store_next = None

    def _cycle_list(self, *inp_lists: List[int]) -> Generator[int, None, None]:
        """
        Iterate over the values in the list until they are all exhausted.
        """
        cur_idx = 0
        idx_list = 0
        while any(cur_idx < len(x) for x in inp_lists):
            cur_list = inp_lists[idx_list]
            if cur_idx < len(cur_list):
                yield cur_list[cur_idx]
            idx_list = (idx_list + 1) % len(inp_lists)
            if idx_list == 0:
                # Back at the top of the lists so increment the next idx pointer.
                cur_idx += 1

    def next(self) -> int or None:
        """
        Leave the heavy lifting of attaining the next value to the hasNext function.
        It has the side effect of storing the next value if needed inside of the _store_next variable.
        """
        if not self.hasNext():
            return None
        cur, self._store_next = self._store_next, None
        return cur

    def hasNext(self) -> bool:
        """
        See if there's a value queued up to be pushed up next already.
        If it's not yet been pulled from the generators then grab it and queue it up
        for the next call to this iterator. If we've reached the end of the lists then
        return False.
        """
        if self._store_next is None:
            # Try to pulled the next yielded value from the generator function.
            try:
                self._store_next = next(self._generator)
            except StopIteration:
                # Reached the end of the generators
                return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5], [-2, -4, -6]), []
# while i.hasNext(): v.append(i.next())
# print(v)

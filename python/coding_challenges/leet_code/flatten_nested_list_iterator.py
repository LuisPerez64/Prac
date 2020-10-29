"""
Question: https://leetcode.com/problems/flatten-nested-list-iterator/
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].
"""


class NestedInteger:
    def __init__(self, value: int or list):
        self.value = value

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.value, int)

    def getInteger(self) -> int or None:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if isinstance(self, int):
            return self
        else:
            return None

    def getList(self) -> ['NestedInteger'] or None:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        if isinstance(self.value, list):
            return self.value
        else:
            return None


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        Use a generator to get the values back from the NestedInteger object without pre processing
        the data.

        _store_next is used as a proxy value as peeking at the value in the generator is a
        destructive operation and cannot be rewound.
        """
        self._generator = self._flatten(nestedList)
        self._store_next = None

    def _flatten(self, nested_list: [NestedInteger]):
        for cur in nested_list:
            if cur.isInteger():
                yield cur.getInteger()
            else:
                yield from self._flatten(cur.getList())

    def next(self) -> int or None:
        if not self.hasNext():
            # No more values exist in the list
            return None
        # place the stored next value from the hasNext call into the response,
        # and clear it for the next called instance.
        cur, self._store_next = self._store_next, None
        return cur

    def hasNext(self) -> bool:
        if self._store_next is not None:
            # We've got the next value queued up, so don't pop from the list
            return True
        # Try to get the next value, and if possible store it as the next value to pull.
        try:
            self._store_next = next(self._generator)
        except StopIteration:
            return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

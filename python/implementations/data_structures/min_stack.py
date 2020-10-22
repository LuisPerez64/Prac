"""
MinStack data structure.
Stack modified to allow polling for the minimum value inside of it in O(1) time.
"""
__all__ = ['MinStack']

from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        Using a list as the basis for the min stack.
        Ensuring that on each push operation the min value is maintained.
        """
        # Tuple holding array. Will record the minimum value at the point of insertion.
        # Also holding in the current value. Format [(10, 10), (12, 10), (2,2)]
        # The min only has to check against the last element on the array to determine if it's the smallest.
        self.stack = deque()

    def __iter__(self):
        return map(lambda cur: cur[0], self.stack)

    def push(self, x: int) -> None:
        """
        Push a tuple onto the array maintaining the minimum value at the curent point.
        """
        if not self.stack:
            self.stack.append((x, x, x))
        else:
            prev_min = self.stack[-1][1]
            prev_max = self.stack[-1][2]
            # If X is pointing to the new min replace it.
            self.stack.append((x, min(prev_min, x), max(prev_max, x)))

    def pop(self) -> None:
        """
        Normal pop operation. Just getting out the current value instead of the min at the current stage.
        """
        return self.stack.pop()[0]

    def top(self) -> int:
        """
        Peek operation
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        Get min is the function that cares about the current minimum value in the stack.
        """
        return self.stack[-1][1]

    def getMax(self) -> int:
        """
        Get the maximum value currently held in the array.
        """
        return self.stack[-1][2]

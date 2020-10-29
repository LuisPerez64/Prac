"""
Question: https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""
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

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

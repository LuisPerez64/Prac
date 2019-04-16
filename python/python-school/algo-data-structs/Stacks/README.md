# Implementation of the Stack Data Structures
## Stack. A Last in First Out data structure
### Functions of the Stack Class
    Push: Put an element at the top of the stack
    Pop : Remove the element at the top of the stack, Popping it off, and returning it to the user.
    Peek: View the last element on the top of the stack.
    Search: Implementation of the Search algorithm within the stack. Done with a linear search, implemented before.
    Added Function: PrintStack: Prints out the stack in a visible manner.
### Implementation
```python
'''
Implementation of the stack data structure
At it's core implementation will be a class wrapper based on the list data type
WIll implement with nodes at one point. Most likely when dealing with the Intensive Course.
'''
import linearSearch

class Stack(object):
    """docstring for stack
    Object Oriented approach at the stack object.
    Available functions:
    Push: Pushes an element onto the stack
    Pop: Pops the last element off the stack
    Peek: View the last element placed in the stack
    Size: Return the size of the stack
    Search: Search for an element in the stack (Done with Linear Search ). Returns Index or -1
    """
    def __init__(self, arg=None):
        if arg is None:
            arg=50
        super(stack, self).__init__()
        self.__capacity = arg
        # Can't do pointer arithmetic in python. No idea of how to implement
        # Unless the Node module facilitates it, not sure as of yet.
        # Simulate the C Stack by creating a list at capacity of Nulls.
        self.__stack = [None for x in range(arg)]
        self.__top  = -1
        self.__full = False
        self.__empty= True

    def push(self, elt=None):
        if elt is None:
            print('Need an element to push on to the stack')
            return 1
        elif self.isFull():
            print('Stack is at capacity. Need to pop an element off. Then push again.')
            return 2
        self.__top += 1
        self.__stack[self.__top]=elt
        print('Added the element ({0}) to the top of stack.'.format(elt))

    def pop(self):
        if self.isEmpty():
            print('Stack is empty. Cannot pop anything off.')
            return 3        
        elt=self.__stack[self.__top]
        self.__stack[self.__top]=None
        self.__top-=1
        return elt

    # Peek is able to return an element if wanted, but defaults to not
    def peek(self, ret=None):
        if self.isEmpty():
            print('No elements in the stack. It\'s empty')
            return 4
        elt=self.__stack[self.__top]
        print('Last element in the stack ({0})'.format(elt))
        if ret is not None:
            return elt

    # Returns the first element in the stack that matches the element
    def search(self, elt=None):
        if elt is None:
            print('Need an element to search for.')
            return 5
        if self.isEmpty():
            return 6
        #Have to reverse the list to get the index
        ind=linearSearch.pythonic(self.__stack, elt)
        if ind == -1:
            print('Element does not exist in the stack.')
        return ind

    def isFull(self):
        tog=False
        if self.__top == self.__capacity -1:
            tog=True
        self.__full = tog
        return self.__full

    def isEmpty(self):
        tog=False
        if self.__top == -1:
            tog=True
        self.__empty =tog
        return self.__empty

    def getSize(self):
        return self.__top

    def printStack(self):
        if self.isEmpty():
            print('Empty Stack nothing to output.')
            return 7
        #Maybe format this better.
        for ind,elt in enumerate(self.__stack[self.__top::-1]):
            print(elt)


```
"""
Implementation of the Doubly Linked List Data Structure.
Attempting to simulate a Python List with Linked List DS
"""
import nodeLinkedList


class DoublyLinkedList(object):
    # Facilitators for the Node Management
    left, right, this = 'left', 'right', 'this'
    """docstring for doublyLinkedList
	Doubly Linked List Data Structure
	Allows you to traverse the Linked List,
	and access elements to the left or right of current node
	    Functions:
        AddToList(Left | Right): Add a node to the list, syntactic sugar for it
			addToLeft, addToRight
        DeleteNode: Removes a node based off of the index given
        GetElement: Retireves the element at index given (Peek Function)
        WalkList: Get the current Head to the given index
        Search: Search for an element in the List, returns it's index
        FreeList: Removes all elements within the list.
        PrintList: Output the List to the user, from lowest index to highest
        Getter And Setter Functions:
            (get|set)Node: Returns or alters the Node wanted(Left, Self, Right)
            (get|set)Content: Returns or alters the content at Node at head
            (get|set)Index: Returns or modifies the index being pointed to by Node at head.
            getSize: Returns the size of the LinkedList  
	"""

    def __init__(self, contents=None, listDataType=None, ordered=False):
        # Initialization of the List, if given dataType, then strict type checking, if also ordered
        # Keeps list in order on each insertion.
        super(DoublyLinkedList, self).__init__()
        self.__size = 0
        # These two values will be used for list index calculations
        # To attempt to remain at the midpoint
        self.__maxNegIndex = 0
        self.__maxPosIndex = 0
        # Can sort the list as is needed, if an incomparable type is added at any point
        # then switch it off, if removed then back on, and so forth.
        self.__canSort = True
        # If the list is an inOrder list then keep it organized at each point.
        self.__ordered = ordered
        # If none. No type safety for the created list. Else strict insertion
        # safety.
        self._setDataType(listDataType)

        # Create the first Node.
        self.addToList(contents)

    # Wrappers for the addToList function. Add syntactic sugar, and make things
    # More user friendly.
    def addToLeft(self, contents=None):
        return self.addToList(contents, self.left)

    def addToRight(self, contents=None):
        return self.addToList(contents, self.right)

    # Can be called directly, but recommend above.
    # If list is empty upon trying to add to it, then Just create a new Node
    def addToList(self, contents=None, direction=None):
        # If the list is empty, then initialize a new node, else will be pointing to
        # Null objects. increment the size as well as setting the dataType if list had
        # TypeSafety enabled initially.
        if self.getSize() == 0:
            if self.getDataType() != type(None):
                self._setDataType(contents)
            self._Node = nodeLinkedList.Node(contents)
            self.__size += 1
            return 0

        # Strict checking of data types being input is enabled.
        if self.getDataType() != type(None) and type(contents) != self.getDataType():
            if not self._canSort(direction, contents):
                # Limited type check warning
                print('Strict Type Checking Enabled. Element not inserted into List.')
                return 2

        # Iniated the list with nothing, so place contents at this index.
        # Special case for empty List Creation. List=DoublyLinkedList()
        if self.getContent() == None:
            self.setContent(contents)
            return

        if self.__ordered:
            if contents >= self.getContent():
                direction = self.right
                # If get to the end of the list(next is None), insert at end
                while self.getNode(direction):
                    # Found a location that is greater than content, and content >= currentNode
                    if contents < self.getNode(direction).get_content():
                        break
                    self._Node = self.getNode(direction)
            else:
                direction = self.left
                while self.getNode(direction):
                    # Found a location that is less than content, and content <= currentNode
                    if contents > self.getNode(direction).get_content():
                        break
                    self._Node = self.getNode(direction)
        else:
            # Keep moving until the next empty placeholder is met.
            while self.getNode(direction):
                self._Node = self.getNode(direction)

        # Found an element that is none. Place the newly created node in its place
        # Appends the node to the list, and, make sure they are connected.

        self.addNode(direction, contents)
        # self._Node = self.getNode(direction)
        self.__reIndexList(direction)
        # List has grown in size. Been brought back to center index as well.
        self.__size += 1
        self.walkList()

    def addNode(self, direction, node=None):
        if direction == self.right:
            self.__maxPosIndex += 1
        else:
            self.__maxNegIndex -= 1
        ##!! Within this context the node is directly being mutated, so no need to return it
        self._Node.add_node(self.getNode(self.this), direction, node)

    def isEmpty(self):
        tog = False
        if self.getSize() == 0:
            tog = True
        return tog

    # Equivalent to a peek function. Does not alter the list, but can peek at an element
    # Returns the element if given a direct index, if index does not exist, return failure
    def getElement(self, index=None):
        curIndex = self.getIndex()
        if index == None:
            return self.getContent()

        if self.walkList(index) == 1:
            return 1

        # Gets the element at the index passed in, then returns to the index of the variable that was called.
        elt = self.getContent()
        self.walkList(curIndex)
        return elt

    # Remove a node from the list, effectively deleting it, as it cannot be accessed.
    # Return it's contents
    def deleteNode(self, index):
        if self.isEmpty():
            print("No elements in the List.")
            return 1

        # Get to the element being indexed.
        if self.walkList(index) == 1:
            print("No elements will be removed.")
            return 1

        # If removing the element will make the list empty
        # do not try and assign anything to node. Make None
        self.__size -= 1
        if self.isEmpty():
            self.__delLastNode()
            return

        # Catch the contents of the current node.
        elt = self.getContent()

        # Alter the list, make it point to the next logical node, from previous.
        # _delNode Requires the direction of the node preceding the the one being removed.
        if index >= 0:
            self.__maxPosIndex -= 1
            self._delNode(self.right)
        elif index < 0:
            self.__maxNegIndex += 1
            self._delNode(self.left)

        return elt

    # Takes the index that is wanted,and places the head there.
    # After Effect. The List is now pointing directly to the indexed node
    # that is being sought.
    def walkList(self, index=None):
        # List remains at the midpoint, allows for easier insertion/deletions.
        if index is None:
            index = int((self.__maxNegIndex + self.__maxPosIndex) / 2)

        if self.getIndex() > index:
            while self.getNode(self.left):
                self._Node = self.getNode(self.left)
                if self.getIndex() == index:
                    return

        elif self.getIndex() < index:
            while self.getNode(self.right):
                self._Node = self.getNode(self.right)
                if self.getIndex() == index:
                    return

        elif self.getIndex() == index:
            return

        # Element is out of the range of the list. IE Does not Exist
        # print("That Indexed Value does not exist.")
        return 1

    def search(self, elt):
        inpIndex = self.getIndex()
        # Might get lucky, and elt is pointed to at curIndex
        if self.getContent() == elt:
            return inpIndex
        eltIndex = None

        # Go to middle of the list
        self.walkList()
        if self.getContent() == elt:
            eltIndex = self.getIndex()

        # Try and find from middle of the list to the left most element
        # Until the element is found, else try again below.
        while self.getNode(self.left) and eltIndex == None:
            self._Node = self.getNode(self.left)
            if self.getContent() == elt:
                eltIndex = self.getIndex()

        if eltIndex is None:
            self.walkList()
        while self.getNode(self.right) and eltIndex == None:
            self._Node = self.getNode(self.right)
            if self.getContent() == elt:
                eltIndex = self.getIndex()

        # Returns the list to the index it started at.
        self.walkList(inpIndex)
        return eltIndex

    '''
	Implementation of the bubble Sort Algorithm with one slight list optimization.
	'''

    def sort(self):
        # Get to the left most element in the list.
        self.walkList(self.__maxNegIndex)

        # Bidirectional Bubble Sort.
        # Puts elements in order in half the time, since walk would have to
        # occur regardless with the pointer structure. Makes It even more efficient
        # than bubble sort, for a nearly sorted list. Since on the walk back it could
        # Satiate it's sortednes...(Not a word)

        # Parameter. Makes sure the list is sortable each time it tries to go
        # through it, just the first way. Setting exceptions are expensive.
        checkSort = True
        while True:
            if self.__swapCheck(self.right, checkSort) or not self.__canSort:
                break
            checkSort = False
            # If going to be running along the list do the sorting both ways.
            if self.__swapCheck(self.left):
                break

        if not self.__canSort:
            print('List not sorted. Corrupted with unsortable Data Types. ')

    # Delete all the nodes in the list. List destruction.
    def freeList(self):
        if self.isEmpty():
            return
        # Cant remove the nodes to the left, until handle to first node's met
        while self.getNode(self.left):
            self._Node = self.getNode(self.left)

        # Begin deletion of the node to the left at each node.
        while True:
            if self.getNode(self.right) is None:
                ''' 
				There seems to be little to no way of termination of self.
				From within the node class the syntax self.setNode(self.this, None)
				does not address the node, and as such, it's dangling.
				'''
                self.__delLastNode()
                break
            self._Node = self.getNode(self.right)
            self.setNode(self.left, None)

    # Outputs the list to the user, from lowest index to highest.
    def printList(self, curIndex=0):
        if self.isEmpty():
            print("Nothing in the list")
            return 1

        # First get to the Left Most element
        while self.getNode(self.left):
            self._Node = self.getNode(self.left)

        # Walk along the list, until the right most element is met.
        while True:
            print('Index: {0:<5} Element: {1}'.format(self.getIndex(), self.getContent()))
            if self.getNode(self.right) is None:
                break
            self._Node = self.getNode(self.right)

        self.walkList(curIndex)

    # Convert the List to a Base Python List
    def __iter__(self):
        if self.isEmpty():
            return

        self.walkList(self.__maxNegIndex)
        while True:
            yield self.getContent()
            if self.getNode(self.right) is None:
                break
            self._Node = self.getNode(self.right)

    def getSize(self):
        return self.__size

    def getDataType(self):
        return self.__dataType

    def getIndex(self):
        return self._Node.get_index()

    def getContent(self):
        return self._Node.get_content()

    # Returns a handle to the node referenced by direction
    def getNode(self, direction):
        return self._Node.get_node(direction)

    # Returns the amount of node instances that had to be created.
    def getTotalNodes(self):
        # Function to get the total nodes that were created
        return self._Node.__totalNodes

    def setNode(self, direction, node=None):
        if direction == self.this:
            # Can't mutate the node if pointing to self, need to mutate it
            # directly.
            self._Node = node
            return
        self._Node.set_node(direction, node)

    def setContent(self, contents):
        self._Node.set_content(contents)

    def setIndex(self, index):
        self._Node.set_index(index)

    # Internal Functions. Helpers to achieve goals needed, should not be called directly by user.
    def _delNode(self, previous):
        # Index for the list element that is being prior to the insertion point.
        prevIndex = self.getIndex() - 1 if previous == self.left else self.getIndex() + 1
        next = self.left if previous == self.right else self.right

        # Case of only element is handled prior to this call being made, no need to handle.
        # If there's a node before and one after current index. Join those two nodes
        if self.getNode(next) and self.getNode(previous):
            # PrevNode.Next = NextNode.Prev, Cur Node becomes None
            # Create a temporary pointer to the next node
            tempNode = self.getNode(next)
            # Go to the node that precedes the node being removed
            self.walkList(prevIndex)

            # Set the node referenced initially to "Null"
            self.setNode(next, None)

            # Attach the next Node to the Preceding node
            # Temp Nodes, previous Node is the current Node
            self.setNode(next, tempNode)
            tempNode.set_node(previous, self.getNode('this'))
        # self.getNode(previous).setNode(next, self.getNode(previous))

        # Case under which the node being removed is the last node in the list.
        elif not self.getNode(next) and self.getNode(previous):
            self.walkList(prevIndex)
            self.setNode(next, None)
        # Keep the list's index structure, by re-indexing from the node pointing to
        # currently til the last node in the list, in the direction of the node pointed to
        self.__reIndexList(previous)

    # Function to basically kill the list off completely. No more node handles
    # Done when no other nodes exist but self. Resets all parameters as well.
    def __delLastNode(self):
        self._Node = None
        self.__size = 0
        self.__maxNegIndex = 0
        self.__maxPosIndex = 0

    # Helper function for the sort algorithm
    def __swapCheck(self, direction, checkSort=None):
        # Results of checking validity must equal the below check as well.
        # Logic (moving Left, < must be True, if not true then elt > next)
        # If < is True and localCheck is True, then swap(Reverse for >)
        localCheck = True if direction == self.left else False
        noSwaps = True
        while self.getNode(direction):
            # Runs one time per sort attempt.
            if checkSort:
                self._canSort(direction)
                if not self.__canSort:
                    break

            if (self.getContent() < self.getNode(direction).get_content()) == localCheck:
                temp = self.getContent()
                self.setContent(self.getNode(direction).get_content())
                self.getNode(direction).set_content(temp)
                noSwaps = False
            self._Node = self.getNode(direction)
        return noSwaps

    # FUnction to bring the indexed values of the input list to where they rest
    # After effect, if an element is removed indices were 0 1 3 4 -> 0 1 2 3
    def __reIndexList(self, next, curIndex=None):
        prev = self.left if next == self.right else self.right
        # If next == right, previous == left, increment all until Null is found
        # Else decrement all untill Null is found
        nextInc = 1 if next == self.right else -1
        # If an element is removed from the List then the indexing will
        # run re-indexing every item to the left or right of the list respectively
        nextInd = self.getIndex()
        if self.getNode(prev):
            nextInd = self.getNode(prev).get_index()
        while True:
            nextInd += nextInc
            self.setIndex(nextInd)
            if self.getNode(next) is None:
                break
            self._Node = self.getNode(next)

        self.walkList(curIndex)

    # Sets the data type that will be adhered to for each creation of a new Linked List.
    # If set to none with optional parameter, No Type Safety granted within the list
    # It cannot be sorted, within some ridiculous amounts of data analyzing.
    def _setDataType(self, listDataType):
        self.__dataType = type(listDataType)

    # Check if a node that is added will cause an exception. Done on sort
    # Can be called externally, not in sort...
    def _canSort(self, next=None, contents=None):
        # Call to see if adding the element will disrupt the lists integrity.
        # Done only when strict type checking is enabled.
        if contents is not None:
            try:
                self.getNode(self.this).get_content() < contents
                return True
            except:
                return False

        if next is None:
            return
        self.__canSort = True
        # If the two contents cannot be sorted then list is corrupted. Sort Wise
        try:
            self.getNode(self.this).get_content() < self.getNode(next).get_content()
        except:
            self.__canSort = False

    def _printIndices(self):
        print(self.__maxNegIndex, self.__maxPosIndex, self.getIndex(), )


import random

O = DoublyLinkedList(None, int)
for i in range(500):
    O.addToLeft(random.randint(0, 500))
print('Done')

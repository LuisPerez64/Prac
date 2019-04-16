# Linked List
## Implementation of the Linked List Data Strucutre, with the use of the Nodes Data Strucutre. Using only primitive types. 
##### Node Implementation is within this directory
    The Implementation of the Node Struct was pivotal for the attempt to use only primitive types in the creation of the linked list data type. Because of the doubly linked nature of the list that was implemented, things could be added or deleted from either side of the List. Which caused a minor complication, mainly due to Pythons lack of pointer access.

## Notable Functions Wihtin Node Struct:
```python
class Node()
##    ...
    def __init__(self, contents=None,leftNode=None, rightNode=None):
        super(Node, self).__init__()
        self.__leftNode = leftNode
        self.__rightNode= rightNode
        self.__contents = contents
        self.__index = 0
        # Datatype of the content contained in the node.
        self.__setDataType(contents)
        # Increment the count of the nodes that have been created.
        self.__totalNodes=self.__totalNodes.__next__()    
##    ...
    # OverLoad the str function. Prints the address of the Node, and it's contents.
    def __str__(self):  
        addr=repr(self).split(' ')[-1][:-1]
        return str('Addr: {0}\tContents: {1}'.format(addr, self.__contents))
##    ...
    # Node Insertion.
    '''
    Add a node to the list being dealt with. 
    If adding a node to the left, make the newNode that is 
    created point to the previous node. Ie.
    if adding a node to the left of the list, then 
    then the new nodes rightNode has to be the left Node
    of the node that called it, and vice versa.
    '''
    def addNode(self, prevNode, nextDir, contents=None):
        prevDir = 'right' if nextDir == 'left' else 'left'
        # Appending the new node in between two nodes, if NexNode is not none.
        nextNode = self.getNode(nextDir)

        # Create a new node
        addNode=Node(contents)
        
        # Make the new node point to the one that called it, based on direction
        # And also the node after it, if not null
        addNode.setNode(prevDir, prevNode)
        addNode.setNode(nextDir, nextNode)
        
        # Make the node that called add acknowledge that the node 
        # that is created is to be pointed to next.
        prevNode.setNode(nextDir, addNode)
        # If there exist a node after the newly created Node, point it back to new node as well.
        if nextNode is not None:
            nextNode.setNode(prevDir, addNode)
```
## Notable Functions for The Linked List Data Structure.
```python
class DoublyLinkedList(object):
    # Facilitators for the node management
    left, right, this='left','right', 'this'
##  ...
    def __init__(self, contents=None, listDataType=None):
        super(DoublyLinkedList, self).__init__()
        self.__size=0
        # These two values will be used for list index calculations
        # To attempt to remain at the midpoint
        self.__maxNegIndex=0
        self.__maxPosIndex=0
        # Can sort the list as is needed, if an incomparable type is added at any point
        # then switch it off
        self.__canSort=True
        # If none. No type safety for the created list. Else strict insertion
        # safety. 
        self._setDataType(listDataType)

        # Create the first Node.
        self.addToList(None,contents)
##  ...
    def addToLeft(self, contents=None):
        return self.addToList(self.left, contents)  
    def addToRight(self, contents=None):
        return self.addToList(self.right, contents)

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
            self.__size+=1          
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
                    if contents < self.getNode(direction).getContent():
                        break
                    self._Node = self.getNode(direction)
            else:   
                direction = self.left
                while self.getNode(direction):
                    # Found a location that is less than content, and content <= currentNode
                    if contents > self.getNode(direction).getContent():
                        break
                    self._Node = self.getNode(direction)                
        else: 
            # Keep moving until the next empty placeholder is met.
            while self.getNode(direction):
                self._Node = self.getNode(direction)
        
        # Found an element that is none. Place the newly created node in its place
        # Appends the node to the list, and, make sure they are connected.  
        
        self.addNode(direction, contents)
        #self._Node = self.getNode(direction)
        self.__reIndexList(direction)
        # List has grown in size. Been brought back to center index as well.
        self.__size+=1
        self.walkList()

#   ...
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
        self.__size-=1  
        if self.isEmpty():
            self.__delLastNode()
            return

        # Catch the contents of the current node.
        elt=self.getContent()

        # Alter the list, make it point to the next logical node, from previous.
        #_delNode Requires the direction of the node preceding the the one being removed.
        if index >= 0:
            self.__maxPosIndex-=1
            self._delNode(self.right)
        elif index < 0:
            self.__maxNegIndex+=1
            self._delNode(self.left)

        return elt

    # Internal Functions. Helpers to achieve goals needed, should not be called directly by user.
    def _delNode(self, previous):
        # Index for the list element that is being prior to the insertion point.
        prevIndex = self.getIndex() -1 if previous == self.left else self.getIndex() + 1
        next = self.left if previous == self.right else self.right

        #Case of only element is handled prior to this call being made, no need to handle.
        # If there's a node before and one after current index. Join those two nodes    
        if self.getNode(next) and self.getNode(previous):
            # PrevNode.Next = NextNode.Prev, Cur Node becomes None
            # Create a temporary pointer to the next node
            tempNode=self.getNode(next)
            # Go to the node that precedes the node being removed
            self.walkList(prevIndex)
            
            # Set the node referenced initially to "Null"
            self.setNode(next, None)
            
            # Attach the next Node to the Preceding node
            # Temp Nodes, previous Node is the current Node
            self.setNode(next, tempNode)
            tempNode.setNode(previous, self.getNode('this'))
            # self.getNode(previous).setNode(next, self.getNode(previous))

        # Case under which the node being removed is the last node in the list.
        elif not self.getNode(next) and self.getNode(previous):
            self.walkList(prevIndex)
            self.setNode(next, None)
        # Keep the list's index structure, by re-indexing from the node pointing to
        # currently til the last node in the list, in the direction of the node pointed to
        self.__reIndexList(previous)
                
#   ...
    # Takes the index that is wanted,and places the head there. 
    # After Effect. The List is now pointing directly to the indexed node
    # that is being sought.
    def walkList(self,index=None):
        # List remains at the midpoint, allows for easier insertion/deletions.
        if index is None:
            index=int((self.__maxNegIndex + self.__maxPosIndex)/2)

        if self.getIndex() > index:
            while self.getNode(self.left):
                self._Node=self.getNode(self.left)
                if self.getIndex() == index:
                    return

        elif self.getIndex() < index:
            while self.getNode(self.right):
                self._Node=self.getNode(self.right)
                if self.getIndex() == index:
                    return

        elif self.getIndex() == index:
            return

        #Element is out of the range of the list. IE Does not Exist
        print("That Indexed Value does not exist.")
        return 1 
#   ...
'''
    Implementation of the bubble Sort Algorithm with one slight list optimization.
    '''
    def sort(self):
        # Get to the left most element in the list.
        self.walkList(self.__maxNegIndex)

        # Bidirectional Bubble Sort.
        # Puts elements in order in half the time, since walk would have to 
        # occur regardless with the pointer structure. 

        # Makes sure the list is sortable first time through.
        checkSort = True
        while True:
            # Place Elements in highest position.
            if self.__swapCheck(self.right, checkSort) or not self.__canSort :
                break
            checkSort =False    
            # If going to be running along the list do the sorting both ways.  
            if self.__swapCheck(self.left):
                break

        if not self.__canSort:
            print('List not sorted. Corrupted with unsortable Data Types. ')

    # Helper function for the sort algorithm
    def __swapCheck(self, direction, checkSort=None):
        # Results of checking validity must equal the below check as well. 
        # Logic (moving Left, < must be True, if not true then elt > next)
        # If < is True and localCheck is True, then swap(Reverse for >) 
        localCheck= True if direction == self.left else False       
        noSwaps = True
        while self.getNode(direction):
            # Runs one time per sort attempt.
            if checkSort:
                self._canSort(direction)
                if not self.__canSort:
                    break
#   ...
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
                self.__delLastNode() self.setNode(self.left, None)
                break
            self._Node=self.getNode(self.right)
            self.setNode(self.left, None)
```
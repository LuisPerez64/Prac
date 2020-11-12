'''
Base Binary Search Tree Implementation
'''


class NodeBST(object):
    """docstring for NodeBST
    Binary Search Tree Node Base implementation
    Node will hold just the basic format for the tree. Functions mutating the
    Node will be implemented here. Addition location, Node Creation, Tree balance, and other
    operations will be handled by the Tree Struct itself._Leaf.
    """
    leftChild, rightChild, thisNode = 'left', 'right', 'this'

    def __init__(self, contents, rootNode=None, left_child=None, rightChild=None):
        super(NodeBST, self).__init__()
        self._contents = contents
        self._rootNode = rootNode
        self._leftChild = left_child
        self._rightChild = rightChild
        # Allow for multiple elements of same value in the Trie
        self._instances = 0
        if contents is not None:
            self._instances += 1

    # OverLoad the str function. Prints the address of the Node, and it's contents.
    def __str__(self):
        addr = repr(self).split(' ')[-1][:-1]
        return str('Addr: {0}\tContents: {1}'.format(addr, self._contents))

    def getContents(self):
        return self._contents

    def newLeaf(self, newLeaf, direction):
        # Add the new leaf either to the left or right of root
        if direction == self.leftChild:
            self._leftChild = newLeaf
        elif direction == self.rightChild:
            self._rightChild = newLeaf
        newLeaf._rootNode = self

    def addDelNode(self, add=True):
        if add:
            self._instances += 1
        else:
            self._instances -= 1
        # Remove the node completely from the tree.
        if self._instances == 0:
            # Default to
            if self._leftChild is not None:
                self._leftChild.rightChild = self._rightChild
                self._leftChild._rootNode = self._rootNode
            elif self._rightChild is not None:
                self._rightChild.leftChild = self._leftChild
                self._rightChild._rootNode = self._rootNode
            else:
                # Has no children, no rotation on its end to do.
                pass
            del self


class BinarySearchTree(object):
    leftChild, rightChild, thisNode, parentNode = 'left', 'right', 'this', 'parent'
    """docstring for BinarySearchTree
    Binary Tree Implementation. No balancing, no rotations. Just in order insertion.
    Does not allow duplicates in the Tree.
    """

    def __init__(self, contents=None):
        # Creation of the tree itself is just initialization of a node.
        super(BinarySearchTree, self).__init__()
        self._Leaf = None
        self._Root = None
        if contents:
            self.addChild(contents)

    def addChild(self, contents, direction=None):
        if self._Leaf is None:
            # The tree itself is uninitiated.
            self._Leaf = self._newNode(contents)
            self._Root = self._Leaf
        # Place the node in the empty slot.
        elif direction is not None and self.getLeaf(direction) is None:
            self.setLeaf(direction, contents)
            self._Leaf = self._Root
        else:
            curCont = self.getContents(self.thisNode)
            if contents > curCont:
                next = self.getLeaf(self.rightChild)
                if next:
                    self._Leaf = next
                direction = self.rightChild
            elif contents < curCont:
                next = self.getLeaf(self.leftChild)
                if next:
                    self._Leaf = next
                direction = self.leftChild
            else:
                print('Element ({0}) is in the Tree already. Incrementing Exists Count.'.format(contents))
                self.getLeaf(self.thisNode)._addDelNode('add')
                return
            # Element is now in a place it could be added
            self.addChild(contents, direction)

    def findElt(self, element):
        if self.getLeaf(self.thisNode) is None:
            # Got to the end, and the element does not exist in the Tree.
            print('Element ({0}) is not in the Tree.'.format(element))
            self._Leaf = self._Root
            return None

        contents = self.getContents(self.thisNode)
        if element < contents:
            self._Leaf = self.getLeaf(self.leftChild)
        elif element > contents:
            self._Leaf = self.getLeaf(self.rightChild)
        elif contents == element:
            # Found the element. Return the node that houses it.
            return self.getLeaf(self.thisNode)
        return self.findElt(element)

    def deleteLeaf(self, elt):
        nodeLocation = self.findElt(elt)
        if nodeLocation is None:
            return
        nodeLocation._addDelNode('del')

    def getContents(self, direction='this'):
        return self.getLeaf(direction).getContents()

    def getLeaf(self, direction):
        # Gets the leaf being pointed to, or the parent node that called it. Returns a handle to it.
        # Only real accessor that should be called past Tree Creation.
        if direction == self.leftChild:
            return self._Leaf.leftChild
        elif direction == self.rightChild:
            return self._Leaf.rightChild
        elif direction == self.thisNode:
            return self._Leaf
        # Node which connects the children, or None if top of tree.
        elif direction == self.parentNode:
            return self._Leaf._rootNode

    def setLeaf(self, direction, contents):
        # Gets a reference to the leaf in the direction wanted. Sets up a new Node in it's place.
        # The New Node will point to the root node that was created before it, and attach itself to it at
        # as a leaf, in the input direction.
        newLeaf = self._newNode(contents)
        self.getLeaf(self.thisNode).newLeaf(newLeaf, direction)

    # Which order dictates the order in which the Tree will be traversed.
    def traverse(self, order: str = 'inOrder'):
        if self._Leaf is None:
            return
        if order == 'inOrder':
            if self.getLeaf(self.thisNode) is None:
                return
            temp = self._Leaf
            if self._Leaf.leftChild is not None:
                self._Leaf = self._Leaf.leftChild
                self.traverse()
                self._Leaf = temp
            if self._Leaf.rightChild is not None:
                self._Leaf = self._Leaf.rightChild
                self.traverse()
                self._Leaf = temp
            print(self._Leaf.contents)
        if order == 'postOrder':
            pass
        if order == 'pre-order':
            pass
        if order == 'printTree':
            curLevel = [self._Root]
            # Print the head first, keeps things cleaner, the method below iterates over the nodes, but does not actively change
            # the location of the pointer within the tree. Causes less of a need to actively swap the leaf being dealt with.
            print(self._Leaf.getContents())
            while curLevel:
                nextLevel, thisStr = [], ''
                # Iterates over the level that the tree is currently on
                for node in curLevel:
                    # Add the nodes to the next iteration that will be run through, allowing the next level that will be iterated
                    # to house itself based on the nodes in the level being iterated over.
                    if node.leftChild:
                        # Add the node to the list, and add it's contents to the elements to be printed out.
                        nextLevel.append(node.leftChild)
                        thisStr += str(node.leftChild.getContents()) + ' '
                    if node.rightChild:
                        nextLevel.append(node.rightChild)
                        thisStr += str(node.rightChild.getContents()) + ' '
                print('{0}'.format(thisStr))
                # Swap the next Level with the current one.
                curLevel = nextLevel

    # Only manner of creation of a new Node Type. The BST is just a bunch of Nodes
    # Pointing to their children, and their root.
    def _newNode(self, contents, rootNode=None, ):
        return NodeBST(contents, rootNode)

    def _addDelNode(self, add):
        self.addDelNode(add)


import random

random.seed(0)
O = BinarySearchTree()
for i in range(20):
    O.addChild(random.randint(-100, 100))
O.traverse('printTree')
O.deleteLeaf(3)
O.traverse('printTree')

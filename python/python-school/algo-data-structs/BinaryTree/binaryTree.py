"""
Implementation of the Binary Tree Data Structure.
"""


class Node(object):
    """docstring for Node
    Node Data Structure for the Binary Tree
    """

    def __init__(self, contents=None, left_child=None, right_child=None):
        super(Node, self).__init__()
        self._contents = contents
        self._leftChild = left_child
        self._rightChild = right_child

    # OverLoad the str function. Prints the address of the Node, and it's contents.
    def __str__(self):
        addr = repr(self).split(' ')[-1][:-1]
        return str('Addr: {0}\tContents: {1}'.format(addr, self._contents))


class BinaryTree(object):
    left, right, thisNode = 'left', 'right', 'thisNode'
    """docstring for BinaryTree
    Binary Tree Data Structure. Attains elements & places them in order in the
    first slot that is available from given tree traversal."""

    def __init__(self, contents=None):
        super(BinaryTree, self).__init__()
        self.tree = self.newNode(contents)

    '''
    Adds a child to the Binary Tree, at the first available slot
    '''

    def add_child(self, contents):
        # Special case where tree was just initialized
        if self.getContents() is None:
            self.setContents(contents)
            return

        cur_level = [self.tree]
        # Runs as long as the List is not empty. Should run only when the tree's level is full.
        while cur_level:
            next_level = []
            for node in cur_level:
                # Assume that the node will find it's home.
                placed = True
                # If found an empty slot, place it there, break out.
                if not node._leftChild:
                    node._leftChild = self.newNode(contents)
                    break
                elif not node._rightChild:
                    node._rightChild = self.newNode(contents)
                    break

                # Neither slot was Null, append both to next level
                next_level.append(node._leftChild)
                next_level.append(node._rightChild)
                # Assumption was wrong, element was not placed this run through.
                placed = False
            # Node was placed in it's rightful location in the Tree
            if placed:
                break
            cur_level = next_level

    def deleteChild(self, elt):
        node = self.search(elt, False)
        if not node:
            return

        if node._leftChild is None and node._rightChild is None:
            print(node)
            node = None
            print(node)

    # Binary Tree is not sorted, search is linear in nature, O(n) time
    # Works for a sorted, or unsorted tree depends on sortedTree value.
    def search(self, elt, sortedTree=True):
        if self.tree is None:
            return
        # Unsorted Binary Tree. Search goes through all elements. Linear in complexity
        if not sortedTree:
            curLevel = [self.tree]
            if self.getContents() == elt:
                return self.tree
            while curLevel:
                nextLevel = []
                for node in curLevel:
                    if node._leftChild:
                        if node._leftChild._contents == elt:
                            return node._leftChild
                        nextLevel.append(node._leftChild)
                    if node._rightChild:
                        if node._rightChild._contents == elt:
                            return node._rightChild
                        nextLevel.append(node._rightChild)
                curLevel = nextLevel
        elif sortedTree:
            # Attain the element from within a binary Search Tree format.
            node = self.tree
            while node:
                val = node._contents
                if elt == val:
                    return node
                elif elt > val:
                    node = node._rightChild
                elif elt < val:
                    node = node._leftChild

        print('Element: {0} is not in the Tree.'.format(elt))

    # Wrapper for the attainment of the height of the given tree.
    def height(self):
        return self._height(self.tree)

    # Wrapper for the path from root to each of it's leaves
    def printLeafPaths(self):
        self._printLeafPaths(self.tree, '')

    # Outputs the elements of the tree on a per level basis
    def printTree(self, reversed=False):
        if self.tree is None:
            return
        curLevel = [self.getNode()]
        levelPrint = [self.getContents()]
        # Iterate through the levels in the node
        while curLevel:
            outStr = ''
            nextLevel = []
            # For each of the levels, if a child is found
            # add the child to the list of the next elements that will be validated.
            for node in curLevel:
                # Add the child nodes, and also add the contents to the next Level Print out.
                if node._leftChild:
                    nextLevel.append(node._leftChild)
                    outStr += str(node._leftChild._contents) + ' '
                if node._rightChild:
                    nextLevel.append(node._rightChild)
                    outStr += str(node._rightChild._contents) + ' '
            # Loop validation, and also add the created string
            levelPrint.append(outStr)
            curLevel = nextLevel

        if reversed:
            levelPrint.reverse()
        for i in levelPrint:
            print(i)

    # Traverse the tree recusively, printing out the lowest level first.
    # Printing of the tree in reverse level order.
    def reverseTraverseRecursive(self, level):
        pass

    # Prints the path from the root node to it's leaves for each of the leaves that occur
    def _printLeafPaths(self, node, contents=None):
        # If at a leaf, then print out the contents
        if node is None:
            print(contents)
            return
        lCont, rCont = '', ''
        if contents:
            lCont = ' -L-> '
            rCont = ' -R-> '
        val = str(node._contents)
        # Continue printing out the needed paths for the branches
        self._printLeafPaths(node._leftChild, contents + lCont + val)
        # Add a constraint to not print out the same Leaf Path twice
        if node._rightChild:
            self._printLeafPaths(node._rightChild, contents + rCont + val)

    # Recursively attain the height of a given tree, max height
    # Must pass the root node of the tree in.
    def _height(self, rootNode):
        if rootNode is None:
            return 0

        # Attain the height from each sides nodes, as the recursion goes along
        leftHeight = self._height(rootNode._leftChild)
        rightHeight = self._height(rootNode._rightChild)

        # Return the biggest subTree that is found in this recursion, adding the height to the tally.
        if leftHeight > rightHeight:
            return leftHeight + 1
        return rightHeight + 1

    def newNode(self, contents):
        return Node(contents)

    def getNode(self, node='thisNode'):
        if node == self.left:
            return self.tree._leftChild
        elif node == self.right:
            return self.tree._rightChild
        elif node == self.thisNode:
            return self.tree

    def getContents(self):
        return self.getNode()._contents

    def setContents(self, contents):
        self.getNode()._contents = contents


O = BinaryTree()
for i in range(10):
    O.add_child(i)

O.printTree()
O.printLeafPaths()

O.search(3, False)
O.deleteChild(7)

O.printLeafPaths()

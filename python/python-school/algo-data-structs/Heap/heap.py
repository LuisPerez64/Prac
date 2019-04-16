"""
Heap data structure implementation.
"""
import random

left, right, thisNode = 'left', 'right', 'thisNode'


class Node(object):
    """
    docstring for Node
    Node Data Structure for the Binary Tree
    """

    def __init__(self, contents = None, leftChild = None, rightChild = None):
        super(Node, self).__init__()
        self._contents = contents
        self._leftChild = leftChild
        self._rightChild = rightChild

    # OverLoad the str function. Prints the address of the Node, and it's contents.
    def __str__(self):
        addr = repr(self).split(' ')[-1][:-1]
        return str('Addr: {0}\tContents: {1}'.format(addr, self._contents))

    def get_child(self, direction) -> 'Node':
        if direction == 'left':
            return self._leftChild
        return self._rightChild

    def set_child(self, direction, new_node):
        if direction == 'left':
            self._leftChild = new_node
        else:
            self._rightChild = new_node

    def get_contents(self):
        return self._contents

    def set_contents(self, contents):
        self._contents = contents

    def print_structure(self, print_me = ""):
        l_child = self.get_child(left)
        r_child = self.get_child(right)
        if l_child is None and r_child is None:
            print(print_me)
            return
        l_cont, r_cont = "", ""
        if print_me:
            l_cont = ' -L-> '
            r_cont = ' -R-> '

        val = str(self.get_contents())
        if l_child:
            l_child.print_structure(print_me + l_cont + val)
        if r_child:
            r_child.print_structure(print_me + r_cont + val)


class Heap(object):
    heap: 'Node' = None

    def __init__(self, initializer = None):
        if type(initializer) is list:
            for element in initializer:
                self.add_node(element)
        elif type(initializer) in [int, float]:
            self.add_node(initializer)

    def add_node(self, contents):
        """
        Add a node to the heap
        :param contents: Contents to add to the heap
        :return:
        """
        if self.heap is None:
            self.heap = self.new_node(contents)
            return
        top_node = self.heap
        new_node = self.new_node(contents)
        while True:
            direction = random.choice(['left', 'right'])
            l_ch = top_node.get_child('left')
            r_ch = top_node.get_child('right')
            if top_node is None:
                top_node = new_node
            if l_ch is None and r_ch is None:
                top_node.set_child(direction, new_node)
                break
            elif l_ch is None:
                top_node.set_child(left, new_node)
                break
            elif r_ch is None:
                top_node.set_child(right, new_node)
                break

            top_node = top_node.get_child(direction)
            cur_contents = top_node.get_contents()

            if cur_contents > contents:
                print('swapping', contents, cur_contents)
                top_node.set_contents(contents)
                contents = cur_contents

    def get_contents(self):
        return self.get_node().get_contents()

    def get_node(self, node = thisNode):
        if node == left:
            return self.heap.get_child(left)
        elif node == right:
            return self.heap.get_child(right)
        else:
            return self.heap

    def new_node(self, contents):
        return Node(contents)

    def print_all(self):
        self.heap.print_structure()


O = Heap()
inp = [4, 12, 7, 10, 5,8]
for x in range(len(inp)):
    # print(inp[x])
    O.add_node(inp[x])

O.print_all()

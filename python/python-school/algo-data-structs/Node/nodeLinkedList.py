class Node(object):
    __totalNodes = 0
    """docstring for Node
    Implementation of the Node Structure.
    Used to simulate the Node Structs within C, and other languages that 
    allow for pointer arithmetic.
    Base Functionality: An ability to get to the next Node from the current one
        addNode(): Append a node to the input (List)
        setNode(): Sets the value of the left, or right node of current node being pointed to.
        getContent(): Get __contents__ of the current Node Pointed To.

    """

    def __init__(self, contents=None, left_node=None, right_node=None):
        super(Node, self).__init__()
        self.__leftNode = left_node
        self.__rightNode = right_node
        self.__contents = contents
        self.__index = 0
        # Datatype of the content contained in the node.
        self.__set_data_type(contents)
        # Increment the count of the nodes that have been created.
        self.__totalNodes += 1

    # Destructor Function. Can do a bit of error Logging, but don't need to atm.
    def __del__(self):
        self.__totalNodes -= 1

    # OverLoad the str function. Prints the address of the Node, and it's contents.
    def __str__(self):
        addr = repr(self).split(' ')[-1][:-1]
        return str('Addr: {0}\tContents: {1}'.format(addr, self.__contents))

    '''
    Add a node to the list being dealt with. 
    If adding a node to the left, make the newNode that is 
    created point to the previous node. Ie.
    if adding a node to the left of the list, then 
    then the new nodes rightNode has to be the left Node
    of the node that called it, and vice versa.
    '''
    def add_node(self, prev_node, next_dir, contents=None):
        prev_dir = 'right' if next_dir == 'left' else 'left'

        # Create a new node
        next_node = Node(contents)

        # Make the new node point to the one that called it, based on direction
        next_node.set_node(prev_dir, prev_node)

        # Index is incremented if adding to the right of the list, else decrement
        next_ind = prev_node.get_index() + (-1 if next_dir == 'left' else 1)
        next_node.set_index(next_ind)

        # Make the node that called add acknowledge that the node
        # that is created is to be pointed to next.
        prev_node.set_node(next_dir, next_node)

    '''
    Getter Functions for the Node Class
    Return the needed element contained in the node, and do so without mutating anything
    '''

    # Gets the next node, to the left or right based on direction0|1
    # Useful for traversal of the given list that is brought in.
    def get_node(self, direction):
        if direction == 'left':
            return self.__leftNode
        elif direction == 'right':
            return self.__rightNode
        elif direction == 'this':
            return self

    # Returns the content of current node.
    def get_content(self):
        return self.__contents

    # Return the index of the value that is being referenced.
    def get_index(self):
        return self.__index

    def get_data_type(self):
        return self.__dataType

    '''
    Setter functions for the Node Class.
    Mutate the value that is needed, obscuring the class as much as possible.
    '''

    def set_index(self, ind):
        self.__index = ind

    def set_content(self, contents):
        # Changing content, might change the data type.
        self.__set_data_type(contents)
        self.__contents = contents

    # Simulation of the freeing up the node. Destructor, past __del__
    def set_node(self, direction, node=None):
        # Free's up either the left or right node, if no new node is passed in
        # Else makes the left|right point to the node passed in.
        if direction == 'left':
            self.__leftNode = node
        elif direction == 'right':
            self.__rightNode = node
        # The setter function will not work properly if referenced.
        # Have to create the wrapper on the actual Node created.
        elif direction == 'this':
            if node is None:
                self.__del__()
        else:
            print('Not given a handle to operate on.')
            return 1

    # User should absouletly never call this function. Done on creation of new
    # Nodes. Will attempt to grant type safety if appending a node to an existing
    # Data Structure.
    def __set_data_type(self, new_content):
        self.__dataType = type(new_content)

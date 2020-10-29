class ListBST(object):
    """docstring for ListBST
    Binary Search Tree implementation with the List Data Structure
    Implementation of the Binary Search Tree Data Structure, with a list data structure.
    Format: [Root[Left[Lefts_Left][Lefts_Right]][Right[Rights_Left][Rights_Right]]]
    """

    def __init__(self, arg=None):
        super(ListBST, self).__init__()
        self._tree = [arg, [None, None]]

    def add(self, elt):
        new_node = [None, None]
        self._tree.append()

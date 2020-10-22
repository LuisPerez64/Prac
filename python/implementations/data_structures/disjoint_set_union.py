"""
Disjoint Set Union Data Structure

In computer science, a disjoint-set data structure, also called a union–find data structure or merge–find set,
is a data structure that stores a collection of disjoint (non-overlapping) sets. Equivalently, it stores a partition of
a set into disjoint subsets. It provides operations for adding new sets, merging sets (replacing them by their union),
and finding a representative member of a set. The last operation allows to find out efficiently if any two elements are
in the same or different sets.

Resources:
* https://en.wikipedia.org/wiki/Disjoint-set_data_structure
* https://en.wikipedia.org/wiki/Tree_(graph_theory)#Forest

Operations:
* MakeSet(x) : Add a new element, and if not in the forest then add it and if needed set it as it's own root.
* Find(x)    : Follow the chain of parent pointers from a specified node until it reaches a root element.
* Union(x, y): replaces the set containing x and the set containing y with their union.

Use Cases:
* Find Intersections between disjoint sets based on some parameter.
"""
from typing import Any, Dict


class DSU(object):
    def __init__(self):
        self.forest: Dict[int, dict] = {}
        self.number_of_joins = 0

    def make_set(self, node: Any) -> Any:
        if node not in self.forest:
            self.forest[node] = {'parent': node, 'rank': 0}
        return node

    def find(self, node: Any) -> Any:
        root = self.make_set(node)

        while self.forest[root]['parent'] != root:
            root = self.forest[root]['parent']

        while self.forest[node]['parent'] != root:
            parent = self.forest[node]['parent']
            self.forest[node]['parent'] = root
            node = parent
        return root

    def union(self, x: Any, y: Any) -> bool:
        """
        Merge two sets based on their rank.
        Return if there was an actual union operation.
        """
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.forest[xr].get('rank') < self.forest[yr].get('rank'):
            xr, yr = yr, xr
        self.forest[yr]['parent'] = xr
        self.forest[xr]['rank'] += 1
        self.number_of_joins += 1
        return True


class DSUNode(object):
    def __init__(self, val: Any, rank: int = 0):
        self.parent: 'DSUNode' or None = None
        self.val = val
        self.rank = rank

    def __str__(self):
        parent = self.parent if self.parent != self else 'null'
        return f"Rank: {self.rank} Parent: {parent}"

    def __eq__(self, other):
        return self.val == other.val


class DSUComplex(object):
    def __init__(self, find_function: str = 'compression'):
        if find_function not in ['compression', 'halving', 'splitting']:
            raise Exception(f"Invalid find ({find_function}) function specified.")
        self.forest = {}
        self.find_function = find_function
        self.number_of_joins = 0

    def make_set(self, node: DSUNode):
        """
        Create a new set object if needed and attach it to the the forest.
        """
        if node not in self.forest:
            node.parent = node
            node.rank = 0
            self.forest[node] = node
        return node

    def find(self, node: DSUNode) -> DSUNode:
        """
        Find the root node of the given input by tracing its path until its found.
        """
        if self.find_function == 'compression':
            return self._find_path_compression(node)
        elif self.find_function == 'splitting':
            return self._find_path_splitting(node)
        elif self.find_function == 'halving':
            return self._find_path_halving(node)

    def union(self, node_x: DSUNode, node_y: DSUNode) -> bool:
        """
        Combine two disjoint sets into one by making the lesser set's root point to the greater set's root.
        Selection of the new root is done by comparing either the size of the sets or the rank if needed.
        Returns if a join occurred over the two edges presented.
        """
        node_x = self.find(node_x)
        node_y = self.find(node_y)

        # Already the same parent, so they're in the same set.
        if node_x == node_y:
            return False

        # If necessary rename variables to ensure that x.prop < y.prop to determine which set swallows the other.
        if node_x.rank < node_y.rank:
            node_x, node_y = node_y, node_x
        if node_x.rank == node_y.rank:
            node_x.rank += 1

        # Set the lesser node as a part of the greater nodes set.
        self.forest[node_y] = node_x
        self.number_of_joins += 1
        node_y.parent = node_x
        return True

    def _find_path_compression(self, node: DSUNode) -> DSUNode:
        root = node
        while root.parent != root:
            root = root.parent

        while node.parent != root:
            parent = node.parent
            node.parent = root
            node = parent

        return root

    def _find_path_splitting(self, node: DSUNode) -> DSUNode:
        while node.parent != node:
            node, node.parent = node.parent, node.parent.parent
        return node

    def _find_path_halving(self, node: DSUNode) -> DSUNode:
        while node.parent != node:
            node.parent = node.parent.parent
            node = node.parent
        return node

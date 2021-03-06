"""
Implementation of the Graph Abstract Data Type.

Resources:
* https://en.wikipedia.org/wiki/Graph_(abstract_data_type)

TODO: Implement the methods outlined in the Wiki article.
"""
__all__ = ['GraphNode', 'Graph']

from typing import List, Any


class GraphNode(object):
    def __init__(self, val, neighbors: List['GraphNode'] = None, is_directed: bool = False):
        self.val = val
        self.neighbors = neighbors
        self.is_directed = is_directed


class Graph(GraphNode):
    def __init__(self, val=None, neighbors: List[GraphNode] = None, is_directed=False):
        super(Graph, self).__init__(val=val, neighbors=neighbors, is_directed=is_directed)

    @classmethod
    def create_from_adjacency_list(cls, adjacency_list: List[List[Any]]) -> 'Graph':
        """
        Given an adjacency list create the graph object that needs to be referenced
        Example list:
            [[1,2], [2,3], [2,4]]
        """
        pass

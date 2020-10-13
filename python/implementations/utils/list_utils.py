"""
Common utilities that could be useful to hold in one location.
"""
from functools import reduce
from typing import List, Any


def flatten_list(inp_list: List[list]) -> List:
    return reduce(lambda acc, cur: acc + cur, inp_list, [])


def prod_list(inp_list: List[int]) -> int or float:
    """
    Given a list of values. Returns the product of multiplying them all
    """
    return reduce(lambda acc, cur: acc * cur, inp_list, 1)

def print_matrix(inp_matrix: List[List[Any]]):
    for row in inp_matrix:
        print(inp_matrix[row])
"""
Base implementation of the defaultdict object extending the base dict class.

"""
__all__ = ["DefaultDict"]

from typing import Callable


class DefaultDict(dict):
    def __init__(self, missing_func: Callable, **kwargs):
        self.missing_func = missing_func
        super(DefaultDict, self).__init__(**kwargs)

    def __missing__(self, key):
        res = self.missing_func(key)
        super(DefaultDict, self).__setitem__(key, res)
        return res  # super(DefaultDict, self).__getitem__(key)

__all__ = ['binary_search', 'UnsortedListException']

import unittest


class UnsortedListException(Exception):
    """ Exception thrown when the list being searched against is presumed unsorted."""


def binary_search(inp_list: list, seeking: str or float or int) -> int:
    """
    Implementation of the Binary Search Algorithm.
    Implies that the input is a sorted list and will return the index of the found item in the list.
    """
    first_index = 0
    last_index = len(inp_list) - 1
    mid_index = last_index // 2
    indices = (first_index, mid_index, last_index)
    while first_index < len(inp_list) and last_index >= 0:
        cur_item = inp_list[mid_index]
        if cur_item == seeking:
            break
        if cur_item > seeking:
            last_index = mid_index - 1
        else:
            first_index = mid_index + 1
        mid_index = (first_index + last_index) // 2
        if first_index > mid_index and indices == (first_index, mid_index, last_index):
            # If these conditions are met though the item may exist the list is not sorted.
            # The only way the first_index value could exceed the mid_index is if the item sought is both > and < than
            # the current element which is impossible.
            # The indices check is in place to allow the initial exit condition check
            raise UnsortedListException("The input list was not a sorted list.")
        indices = (first_index, mid_index, last_index)
    else:
        # Did not find the item in the list. Raise and leave the caller handle the exception.
        raise IndexError(f"The item '{seeking}' was not found in the inp_list given.")
    return mid_index


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        self.sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.unsorted_list = [6, 9, 3, 16, 8, 10, 18, 14, 15, 11, 17, 12, 19, 13, 0, 5, 1, 4, 2, 7]
        self.invalid_elements = [20, -1, -5, 100]

    def test_search_for_valid_element(self):
        for index in self.sorted_list:
            with self.subTest(msg=f"Seeking valid element {index}"):
                actual = binary_search(inp_list=self.sorted_list.copy(), seeking=index)
                self.assertEqual(actual, index, msg=f"Assertion Failed {actual} != {index}")

    def test_search_for_invalid_element(self):
        for seeking in self.invalid_elements:
            with self.subTest(msg=f"Seeking invalid element {seeking}"):
                self.assertRaises(IndexError, binary_search,
                                  inp_list=self.sorted_list.copy(), seeking=seeking)

    def test_search_for_valid_element_in_unsorted_list(self):
        possible_exceptions = tuple([UnsortedListException, IndexError])
        for seeking in self.sorted_list:
            with self.subTest(msg=f"Seeking {seeking} in unsorted_list"):
                try:
                    found_index = binary_search(inp_list=self.unsorted_list.copy(), seeking=seeking)
                    # The element could still be found even in an unsorted list so ensure that its the sought value.
                    actual = self.unsorted_list[found_index]
                    self.assertEqual(actual, seeking)
                except possible_exceptions as exc:
                    # Due to the list being unsorted it could falsely raise with IndexError due to the sort not
                    # testing all elements.
                    with self.assertRaises(possible_exceptions):
                        raise exc


if __name__ == '__main__':
    unittest.main()

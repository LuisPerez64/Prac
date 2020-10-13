def invert_bits(n: int):
    """
    Give 0101 invert the 1/0 bits in the value to yield '1010'
    """
    rev = 2 ** 32 - 1
    mask = 1
    # This operation will actually just invert the value...
    for idx in range(33):
        rev &= ~(n & mask << idx)


def missing_number(nums: list) -> int:
    """
    X ^ X == X
    The index at which i ^ num != num is the idx at which num lapses
    We keep a tally based on the len of nums array initially and
    keep applying that property until we've exhausted the list of numbers.
    """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

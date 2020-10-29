"""
Collection of bitwise operations that have come up in interviews, or leetcode questions.

Bit Wise Operations:
    x << y: Returns x with the bits shifted to the left by y places
        (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

    x >> y: Returns x with the bits shifted to the right by y places.
        This is the same as //'ing x by 2**y.

    x & y: Does a "bitwise and".
        Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

    x | y: Does a "bitwise or".
        Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

    ~ x: Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1.
        This is the same as -x - 1.

    x ^ y: Does a "bitwise exclusive or".
        Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
        and it's the complement of the bit in x if that bit in y is 1.
"""


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


def count_one_bits(num) -> int:
    """
    Pulled implementation from Leetcode for an optimization to break out of
    the loop sooner.
    While the current num isn't 0 increment the possible number of 1 bits.
    & the number with itself -1 (n &= (n - 1))
    Note:
    The key idea here is to realize that for any number n,
    doing a bit-wise AND of n and n - 1 flips the least-significant 1-bit in n to 0.
    For n = 11 the sequence produces
    n      n -1   n & (n - 1)
    0b1011 0b1010 0b1010
    0b1010 0b1001 0b1000
    0b1000 0b111  0b0
    """
    count = 0
    while num:
        count += 1
        num &= num - 1
    return count


def is_power_of_2(num) -> int:
    """
    A number is a power of 2 iff it has only 1 1 bit in it, excluding 0.
    Grabbing that state comes down to the bitwise operation "Num & (Num - 1) == 0"
    .i.e.
    0010 == 2; 0001 == 2 -1;   2 & 1 == 0000
    0011 == 3; 0010 == 3-1;    3 & 2 == 0010 (not a power)
    """
    return num & (num - 1) == 0


def add_two_integers(a, b):
    """
    TODO: Anotate this in full.
    """
    x, y = abs(a), abs(b)
    # ensure that abs(a) >= abs(b)
    if x < y:
        # Flip the values, and recall this function, instead of handling each of the edge cases for it.
        return add_two_integers(b, a)

    # abs(a) >= abs(b) -->
    # a determines the sign
    sign = 1 if a > 0 else -1
    # The carry_func determines if we're going to be borrowing from or carrying the excess bit in the next calculation.
    if a * b >= 0:
        # sum of two positive integers
        def carry_func(p, q):
            return (p & q) << 1
    else:
        # difference of two integers x - y where x > y
        def carry_func(p, q):
            return ((~p) & q) << 1

    while y:
        answer = x ^ y
        add_op = carry_func(x, y)
        x, y = answer, add_op

    return x * sign


def reverse_bits(num):
    """
    Get the least significant bit and place it in the reverse location in the 32 bit
    range. We get this through raising the value to a given mask. Starting at 31
    and decreasing with each iteration.
    Steps: res = 0, mask = 31
        1) get least sig bit => least_sig_bit = n & 1
        2) increase accum => res = res + least_sig_bit ** mask => res += lsb << mask
        3) right shift n by 1 => n = n // 2 => n >>= 1
        4) set the mask to point to the next power location.
        5) repeat until n 0
    Return the new digit.
    """

    def print_locals():
        tmp = locals().copy()
        for k in ['self', 'tmp', 'print_locals', 'k']:
            tmp.pop(k, None)
        for k, v in [('n_bin', bin(num)), ('ret_bin', bin(ret)), ('mask_bin', bin(2 << mask if mask >= 0 else 0))]:
            tmp[k] = v

        print(tmp, '\n')

    ret = 0
    mask = 31
    while num:
        print_locals()
        # And with 1 to get the lsb
        least_sig_bit = num & 1
        # Increase result by that bit raised to the mask's power
        ret += least_sig_bit << mask
        # Right shift n to get its next bit. Same as n // 2
        num >>= 1
        # decrease the mask to get the next value in place
        mask -= 1
    print_locals()
    return ret

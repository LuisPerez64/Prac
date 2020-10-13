"""
Write a function that takes an unsigned integer and returns the number of '1' bits it
has (also known as the Hamming weight).

Follow up: If this function is called many times, how would you optimize it?

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


Constraints:

The input must be a binary string of length 32
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.first_implementation(n)

    def first_implementation(self, n: int) -> int:
        """
        Integer is guaranteed to fit in a 32 bit register so capture up til 32 bits
        in the mask.
        Initialize it to 1 => 0001 and check if anding that value with the int
        yields anything but 0 and if it does then value must have a 0 at that stage.
        mask = 0001 input is 0011
        0001 & 0011 => 0001 != 0 count += 1
        mask <<= 1 => 0010
        0010 & 0011 => 0010 != 0 count += 1
        ... continue until mask <<= 32
        """
        count = 0
        for idx in range(33):
            if n & 1 << idx != 0:
                count += 1
        return count

    def pulled_implementation(self, n: int) -> int:
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
        while n:
            count += 1
            n &= n - 1
        return count

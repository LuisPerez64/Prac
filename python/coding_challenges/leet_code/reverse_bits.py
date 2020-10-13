"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output
 will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary
  representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above,
the input represents the signed integer -3 and the output represents the signed integer -1073741825.
Follow up:

If this function is called many times, how would you optimize it?

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
 so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
so return 3221225471 which its binary representation is 10111111111111111111111111111111.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        return self.first_implementation(n)

    def first_implementation(self, n: int) -> int:
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
        ret = 0
        mask = 31
        while n:
            # And with 1 to get the lsb
            least_sig_bit = n & 1
            # Increase result by that bit raised to the mask's power
            ret += least_sig_bit << mask
            # Right shift n to get its next bit. Same as n // 2
            n >>= 1
            # decrease the mask to get the next value in place
            mask -= 1
        return ret

    def pulled_implementation(self, n: int) -> int:
        """
        We can implement the algorithm in the following steps:
        1). First, we break the original 32-bit into 2 blocks of 16 bits, and switch them.
        2). We then break the 16-bits block into 2 blocks of 8 bits.
            Similarly, we switch the position of the 8-bits blocks
        3). We then continue to break the blocks into smaller blocks,
            until we reach the level with the block of 1 bit.
        4). At each of the above steps, we merge the intermediate results into a
            single integer which serves as the input for the next step.
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

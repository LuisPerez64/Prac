"""
REVISIT: The algorithm P(x) = P(x & (x - 1)) + 1 may come up as some bit algebra.
Question: https://leetcode.com/problems/counting-bits/

Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in
their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # return self.first_implementation(num)
        return self.second_implementation(num)

    def first_implementation(self, num: int) -> List[int]:
        """
        No use of the bin function to get the number of bits.
        Brute force finding the number of bits in each iteration.
        TC: O(n log n)
            O(n): for every element in the range given
            O(log n): Shift operation takes place and we've got ~ half of the problem at each iteration.
        SC: O(1)
        """
        num_bits = []
        t = 0
        for n in range(num + 1):
            count = 0
            t += 1
            while n:
                t += 1
                count += n & 1

                n = n >> 1
            num_bits.append(count)
        return num_bits

    def second_implementation(self, num: int) -> List[int]:
        """
        Using the last set bit equation.
        P(x) = P(x & (x - 1)) + 1
        num_bits[x] = num_bits[(x & (x - 1))] + 1
        Sequence: n = 5
        Num: 1, Pre: 0, Pre Bits: 0
        Num: 2, Pre: 0, Pre Bits: 0
        Num: 3, Pre: 2, Pre Bits: 1
        Num: 4, Pre: 0, Pre Bits: 0
        Num: 5, Pre: 4, Pre Bits: 1
        TC: O(n)
        SC: O(1)
        """
        num_bits = [0]
        for n in range(1, num + 1):
            # print(f"Num: {n}, Pre: {n & (n - 1)}, Pre Bits: {num_bits[n & (n - 1)]}")
            num_bits.append(num_bits[n & (n - 1)] + 1)
        return num_bits
       
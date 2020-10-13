"""
REVISIT: Bitwise operations are in need of a definite refresh.  Do the operations on pen and paper.
Question: https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return self.pulled_implementation(a, b)

    def pulled_implementation(self, a: int, b: int) -> int:
        """
        Pulled from: https://leetcode.com/problems/sum-of-two-integers/solution/
        Algorithm 1: Bit manipulation
        I would not even be able to begin getting this problem solved at this moment.
        REVISIT: Marking it inside of this context as this needs to be followed through
            and instated through some code analysis and paper run through.

        Bit Wise Operations.
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
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.pulled_implementation(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                print({'action': 'add', 'x': x, 'y': y, 'bin(x)': bin(x), 'bin(y)': bin(y), 'answer = x^y': x ^ y,
                       'carry = (x & y) << 1': (x & y) << 1})
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                print({'action': 'sub', 'x': x, 'y': y, 'bin(x)': bin(x), 'bin(y)': bin(y), 'answer = x^y': x ^ y,
                       '(~x)': (~x),
                       'borrow = ((~x) & y) << 1': ((~x) & y) << 1})

                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign

# Solution().getSum(10,-20)
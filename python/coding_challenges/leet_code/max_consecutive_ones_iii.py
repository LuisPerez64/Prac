"""
REVISIT: Frequency calculation within a sliding window. Base format and can be extended if need be to a varied elt.
Question: https://leetcode.com/problems/max-consecutive-ones-iii/

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.


Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1

Example Run:

input:
    A = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
Window from 0 - 1 is in bound [1]
Window from 0 - 2 is in bound [1, 1]
Window from 0 - 3 is in bound [1, 1, 1]
Window from 0 - 4 is in bound [1, 1, 1, 0]
Window from 0 - 5 is in bound [1, 1, 1, 0, 0]
Window from 0 - 6 out of bound [1, 1, 1, 0, 0, 0]
Window from 1 - 7 out of bound [1, 1, 0, 0, 0, 1]
Window from 2 - 8 out of bound [1, 0, 0, 0, 1, 1]
Window from 3 - 9 out of bound [0, 0, 0, 1, 1, 1]
Window from 4 - 10 is in bound [0, 0, 1, 1, 1, 1]
Window from 4 - 11 out of bound [0, 0, 1, 1, 1, 1, 0]
"""


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        return self.first_implementation(A, K)

    def first_implementation(self, A: List[int], K: int) -> int:
        """
        Use the frequency calculation to grab if the value would benefit from a swap at
        the current position.
        Use a sliding window in relation to it. If the frequency of 1's in the window
        can be supplemented by K if need be to create a long concurrent sequence
        then we check if that length is our new maximum.
        If there are too many 0's to create a full sequence of 1's then
        we increment the left side of the window after removing an instance of the value that
        it had from the frequency listing.
        """
        frequency = defaultdict(lambda: 0)
        left = 0
        max_len = 0
        for right in range(len(A)):
            frequency[A[right]] += 1
            window = right - left + 1

            if window - frequency[1] <= K:
                # print(f"Window from {left} - {right+1} is in bound", A[left:right+1])
                # We've got enough Ks to swap if needed to create a longer sequence.
                max_len = max(max_len, window)
            else:
                # print(f"Window from {left} - {right+1} out of bound", A[left:right+1])
                # increment the left pointer after removing an instance of its number
                frequency[A[left]] -= 1
                left += 1
        return max_len

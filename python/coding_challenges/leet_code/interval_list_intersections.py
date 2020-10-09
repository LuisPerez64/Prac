"""
REVISIT: The main point being the discrete math topics outlined in it with Set Algebra.
Question: https://leetcode.com/problems/interval-list-intersections/submissions/

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return self.first_implementation(A, B)
        # return self.second_implementation(A, B)

    def first_implementation(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Iterate over the two lists with two pointers. If the startpoint of one of the intervals is
        within the end of another then they intersect. On each operation grab the smallest interval
        start point to use as the basis for comparison.
        Time Complexity: O(m + n)
            where m/n are the sizes of the two arrays. since each element is visited at most once.
        Space Complexity: O(1) -- O(n) if taking the output into account
        """
        intervals = []
        idx_a = idx_b = 0

        # 1. Find if the intervals intersect by seeing if the interval with the smallest start points end point overlaps with the later one
        def intervals_intersect(interval_a, interval_b):
            # test: [0,2], [1,5] => [1, 2]
            min_inter, max_inter = (interval_a, interval_b) if interval_a[0] < interval_b[0] else (
            interval_b, interval_a)
            if min_inter[1] >= max_inter[0]:
                # intervals.append()
                return [max_inter[0], min(max_inter[1], min_inter[1])]
            return None

        # 2. iterate over the two interval lists until one of them is exhausted
        while idx_a < len(A) and idx_b < len(B):
            intersection = intervals_intersect(A[idx_a], B[idx_b])
            if intersection:
                intervals.append(intersection)
            # Need to review this discrete math concept.
            # Since all of the intervals are disjoint the smallest end point cannot be joined with another
            # Test: A ([0,2], [5,10]) -- B ([1,5], [8,12]) produce first intersection [1,2].
            # Given that they're disjoint the next possible interval has to start after the end of the previous.
            # since A[n][1] < B[m][1] the only next interval could be from A[n+1][0], B[m][0] since B can still encompass other from A's set.
            if A[idx_a][1] < B[idx_b][1]:
                idx_a += 1
            else:
                idx_b += 1

        return intervals

    def second_implementation(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Recursive solution offloading the work to a helper function with a bound that returns at the first missed interval
        Time Complexity: O(m+n)
            Each element in the arrays will be visited at most once
        Space Complexity: O(1)
            O(m+n) if taking into account the call stack
        """

        # 1. Find if the intervals intersect by seeing if the interval with the smallest start points end point overlaps with the later one
        def intervals_intersect(interval_a, interval_b):
            # test: [0,2], [1,5] => [1, 2]
            min_inter, max_inter = (interval_a, interval_b) if interval_a[0] < interval_b[0] else (
            interval_b, interval_a)
            if min_inter[1] >= max_inter[0]:
                return [max_inter[0], min(max_inter[1], min_inter[1])]
            return None

        def find_intersections(idx_a, idx_b):
            if idx_a == len(A) or idx_b == len(B):
                return []
            intervals = []
            interval_a = A[idx_a]
            interval_b = B[idx_b]
            intersection = intervals_intersect(interval_a, interval_b)
            if intersection:
                intervals.append(intersection)
            if interval_a[1] < interval_b[1]:
                idx_a += 1
            else:
                idx_b += 1
            return intervals + find_intersections(idx_a, idx_b)

        return find_intersections(0, 0)

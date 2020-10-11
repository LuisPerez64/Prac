""" REVISIT: Reviewing the difference in the first/second approach.
Question: https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2


Constraints:

2 <= height.length <= 3 * 104
0 <= height[i] <= 3 * 104

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.second_implementation(height)

    def first_implementation(self, height: List[int]) -> int:
        """
        Brute force attempt.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """

        def get_area(inp_arr: List[int]) -> int:
            """
            Helper function to calculate the total area of water between two points.
            """
            height = min(inp_arr[0], inp_arr[-1])
            return height * (len(inp_arr) - 1)

        final_max = 0
        for start in range(len(height)):
            max_vol = 0
            for end in range(start, len(height)):
                max_vol = max(max_vol, get_area(height[start:end + 1]))
            final_max = max(max_vol, final_max)
        return final_max

    def second_implementation(self, height: List[int]) -> int:
        """
        Using a sliding window approach the start/end pointer only needs to get moved based on which is smaller
        to try and get the bigger area.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        start = 0
        end = len(height) - 1
        final = 0
        while start < end:
            final = max(final, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return final


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

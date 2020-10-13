"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""
from collections import defaultdict
from heapq import heappush, heappushpop, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.first_implementation(nums, k)

    def first_implementation(self, nums: List[int], k: int) -> List[int]:
        """
        Use a hash map
        store the numbers into the hashmap and iterate over the nums list.
        Iterate a second time over the hashmap and get values inserted into a heap
        based on their values. heap insertion is O(log n)
        TM: O(n log k)
            The heap size will never pass K. And insertion is log k
        SC: O(n)
        """
        occs = defaultdict(int)
        rs = []
        for num in nums:
            occs[num] += 1

        for num, oc in occs.items():
            # Convert the min heap to a max heap (simulated) which stores its values as a tuple (-occ, num)
            if len(rs) == k:
                heappushpop(rs, (oc, num))
            else:
                heappush(rs, (oc, num))

        return [heappop(rs)[1] for _ in range(k)]

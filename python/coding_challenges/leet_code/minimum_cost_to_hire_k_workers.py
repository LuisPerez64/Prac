"""
REVISIT: The process for handling the heap is needed. Anotate the solution in full.
Question: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.
When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared
to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.



Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.


Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        """
        Determine the quality to cost ratio for the workers.
        Maintain a max heap of quality. (We're using a minheap, with negative values.)
        We'll also maintain sumq, the sum of this heap.
        For each worker in order of ratio, we know all currently considered workers have lower ratio.
        This worker will be the 'captain'.
        We calculate the candidate answer as this ratio times the sum of the smallest K workers in quality.
        """
        # Sort the workers based on the best bang for buck for the wage / quality

        rqw = sorted([(w / float(q), q, w) for q, w in zip(quality, wage)])

        answer = float('inf')
        pool = []
        sumq = 0
        for r, q, w in rqw:
            # insert the quality into the minheap to pull them out in maxheap order.
            heappush(pool, -q)
            sumq += q
            if len(pool) > K:
                # try and get the min value we can pay out of the scope.
                sumq += heappop(pool)

            if len(pool) == K:
                answer = min(answer, r * sumq)
        return answer

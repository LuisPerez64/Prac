"""
REVISIT: The distributed sorting for the workers distance is an odd optimization and
    worth looking into time complexity wise.
Question: https://leetcode.com/problems/campus-bikes/
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M.
Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers,
we choose the (worker, bike) pair with the shortest Manhattan distance between each other,
and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the
same shortest Manhattan distance, we choose the pair with the smallest worker index;
if there are multiple ways to do that, we choose the pair with the smallest bike index).
We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

Example 1:
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation:
Worker 1 grabs Bike 0 as they are closest (without ties),
and Worker 0 is assigned Bike 1. So the output is [1, 0].
Example 2:



Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation:
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2,
thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].


Note:

0 <= workers[i][j], bikes[i][j] < 1000
All worker and bike locations are distinct.
1 <= workers.length <= bikes.length <= 1000
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # return self.pulled_implementation(workers, bikes)
        return self.first_implementation(workers, bikes)

    def first_implementation(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """
        REDO!
        Calculate the manhattan distances for each of the workers to each of the bikes.
        Implementation works, but needs more separation of the workload. Maybe using a generator
        instead of the whole dist list being read in.
        TC: O(N * N log N) +  O(N log N) => O(N^2 log N)
            O(N^2 log N): Iteration over the two list and the heappush operation on the sort for the individual workers.
            O(N log N)  : Iteration over the workers when assigning them each a bike.
        """
        dist = []
        assigned = [-1] * len(workers)
        best = []

        # TC: O(N^2 log N )
        for idx in range(len(workers)):
            # Create a list per worker to reduce the amount of work to be done when getting the best
            # bike for the given worker.
            dist.append([])
            for b_idx in range(len(bikes)):
                tmp = (abs(workers[idx][0] - bikes[b_idx][0]) + abs(workers[idx][1] - bikes[b_idx][1]), b_idx, idx)
                heappush(dist[-1], tmp)
            # Get the best possible bike for the current worker and place it into the min heap.
            # This segmentation of work reduces the strain on the sort algo to 1K instances from 1M instances
            heappush(best, heappop(dist[-1]))

        invalid = set()
        # TC: O(N log N)
        # Iterate over a minimum N workers and log N for the heappush
        while best and len(invalid) < len(workers):
            _, bike, worker = heappop(best)
            if bike not in invalid and assigned[worker] == -1:
                assigned[worker] = bike
                invalid.add(bike)
            else:
                # We won't be able to assign this bike to the current worker.
                # Select the next closest from their independent pool.
                heappush(best, heappop(dist[worker]))
        return assigned

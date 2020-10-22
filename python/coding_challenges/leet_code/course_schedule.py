"""
REVISIT: First directed graph question, though it fits in the same algo as the undirected
Question: https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.first_implementation(numCourses, prerequisites)

    def first_implementation(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        """
        This is testing if in a directed graph the node does not visit
        its child which visits itself.
        If there is any instance of a cycle then we've found an invalid course link.

        Cycle formats:
            Top level : [[0,1], [1,0]] 1 <-> 0,
            Deep cycle: [[1,0], [2,1], [0, 2]],
                course 2 would need to be taken before course 0 which is a pre req for 1 and 1 is a pre-req for 2
        """
        adjacent = defaultdict(set)
        is_cycle = False

        for course, prereq in prerequisites:
            adjacent[prereq].add(course)
            if course in adjacent and course in adjacent[prereq]:
                # check if there's a cycle in the list at its first level.
                return False
        visited = set()
        seen_path = set()

        def dfs(node):
            """
            Visit each of the nodes.
            """
            if node in visited:
                # Don't redo the work if the cycle was not found before it won't be found now.
                return False
            if node in seen_path:
                # There's been a cycle found in the traversal.
                return True

            # Mark the path as visitedin the current iteration.
            seen_path.add(node)
            is_cycle = False
            for reqs in adjacent[node]:

                is_cycle = dfs(reqs)
                if is_cycle:
                    break
            # If there was no cycle then we remove the node from the seen paths
            # to not muddy up the next instance.
            visited.add(node)
            seen_path.remove(node)
            return is_cycle

        for course in range(num_courses):
            if dfs(course):
                # Found a course that's not represented, or a loop in the graph
                return False
        return True

from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return self.first_implementation(n, edges)

    def pulled_implementation(self, n: int, edges: List[List[int]]) -> int:
        """
        Don't submit this.
        """
        ## RC ##
        ## APPROACH : GRAPH / DFS ##

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        count = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                count += 1
        return count

    def first_implementation(self, n: int, edges: List[List[int]]) -> int:
        """
        Use a map to gather nodes in buckets based on their connections.
        Structure =>
            {nd: set(connected)}
        For every node if there's a connection between node A, B then all connections
        in node B are connected to Node A.
        Iterate over the connections and for every "root" check to see if its been seen
        before. If it's new then increment the count
        add all elements into fin_set.
        Nodes that are not represented are treated as independent?
        Time Complexity: O(3n) => O(n)
        Space Complexity: O(n)
        """
        count = 0
        connections = defaultdict(set)
        fin_set = set()

        for x in range(n):
            # If nodes that are not seen in the list are increasing the paths,
            # this will satisfy that.
            connections[x] = set()

        for a_node, b_node in edges:
            # Get the connected edges in the graph bidrectional
            connections[a_node].add(b_node)
            connections[b_node].add(a_node)

        # print(connections)
        toggle = False
        # Sort the nodes in order of descending order based on the size of their pool.
        # This ensures that stranglers with 1 connection don't jump in too soon into the list.
        for nde, conns in sorted(connections.items(), key=lambda k: -len(k[1])):
            # If the main node is not in fin_set that means nothings stated that a connection existed.
            # If for example it wasn't seen but one of it's connections was then they're all related.
            # Check to see if the child elements intersect with the final set as well.
            if nde not in fin_set and not fin_set.intersection(conns):
                toggle = True
                count += 1
            fin_set.add(nde)
            fin_set.update(conns)
            if toggle:
                print(nde, conns)

            toggle = False
        return count

    def second_implementation(self, n: int, edges: List[List[int]]) -> int:
        """
        FAILED IMPLMENTATION. Cases such as the one listed fail out.
        5
        [[0,1],[1,2],[0,2],[3,4]]
        Find the connected edges based on the first node in their pairing.
        Sort the list of edges to facilitate the comparisons.
        """
        edges.sort(key=lambda k: k[0])
        basis = [edges[0]]
        for edge in edges[1:]:
            if basis[-1][1] == edge[0]:
                basis[-1][1] = max(edge[1], basis[-1][1])
            else:
                basis.append(edge)

        return len(basis)


"""
Test Cases:

5
[[0,1],[1,2],[0,2],[3,4]]
6
[[2,3],[1,2],[1,3]]
5
[[0, 1], [1, 2], [2, 3], [3, 4]]
3
[[2,0], [2,1]]
6
[]
10
[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
100
[[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],[18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],[18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],[2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],[50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],[35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],[13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],[24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],[46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23],[52,55],[43,59],[49,26],[25,90],[52,0],[55,8],[7,23],[97,41],[0,40],[69,47],[73,68],[10,6],[47,9],[64,24],[95,93],[79,66],[77,21],[80,69],[85,5],[24,48],[74,31],[80,76],[81,27],[71,94],[47,82],[3,24],[66,61],[52,13],[18,38],[1,35],[32,78],[7,58],[26,58],[64,47],[60,6],[62,5],[5,22],[60,54],[49,40],[11,56],[19,85],[65,58],[88,44],[86,58]]
"""

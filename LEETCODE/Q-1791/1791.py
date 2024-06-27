## Q:
"""
There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi.
 Return the center of the given star graph.
"""

## Intuition & approach
"""
The code set(edges[0]) & set(edges[1]) converts the first two edges (sub-lists) into sets and finds the intersection of these two sets.
The intersection of two sets contains only the elements that are present in both sets and converts the resulting intersection set back into a list and retrieves the first (and only) element.


For example, consider a star graph with edges [[1,2], [2,3], [2,4]].

edges[0] is [1, 2]
edges[1] is [2, 3]
The sets would be:

set(edges[0]) is {1, 2}
set(edges[1]) is {2, 3}
The intersection of these two sets is {2}, so the center node is 2.
"""

##CODE:
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(set(edges[0]) & set(edges[1]))[0]
## Q:
"""
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.
"""

## APPROACH:
"""
Approach
These are the steps I followed in solving this problem:

Graph Representation and Indegree Calculation:

first, I represent the graph using an adjacency list to efficiently traverse it.
I then calculate the indegree for each node to know how many edges are coming into it.
Nodes with an indegree of 0 can be processed first since they have no dependencies.

Sorting:

I initialize a queue with nodes that have an indegree of 0, as they can be processed first.
During the topological sort, I process each node by:
Adding the current node to its child node's set of ancestors.
Adding all the ancestors of the current node to the child node's set, because if a node is an ancestor of the current node, it is also an ancestor of all its descendants.
Decreasing the indegree of the child node and adding it to the queue if its indegree becomes 0.

Maintaining Ancestors:

I use a set for each node to store its ancestors, ensuring each ancestor is stored only once.
When processing a node, I update the child node's ancestor set with both the current node and all ancestors of the current node to maintain the correct list of ancestors.
"""


## CODE:
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegrees = [0] * n    
        adj_list = collections.defaultdict(list)
        
        for u, v in edges:
            adj_list[u].append(v)
            indegrees[v] += 1
            
        q = collections.deque()

        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
                
        ans = [set() for _ in range(n)]

        while len(q) > 0:
            now = q.popleft()

            for child in adj_list[now]:
                ans[child].add(now)
                ans[child].update(ans[now])  # Union the sets of ancestors
                indegrees[child] -= 1

                if indegrees[child] == 0:
                    q.append(child)

        for i in range(n):
            ans[i] = list(sorted(ans[i]))
        return ans




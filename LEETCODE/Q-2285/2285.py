## Q:
"""
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.

"""
## INTUITION:
"""
Cities with more roads should get higher importance values to maximize their contribution to the total importance
"""
## APPROACH:
"""
Create an array degrees of size N to store the number of roads connected to each city.

For each road [u, v] in the roads list, increment the degree of both cities u and v by 1.

Sort the degrees array in descending order.
Initialize total to 0.

For each city, multiply its degree by its assigned importance value: highest degree gets N, next highest gets N-1, etc.

Sum these products to get the total importance.

Return the total importance value.

"""

## CODE:
class Solution:
    def maximumImportance(self, N: int, roads: List[List[int]]) -> int:
        degrees = [0] * N

        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1

        degrees.sort()
        degrees.reverse()

        total = 0
        for i, x in enumerate(degrees):
            total += (N - i) * x
        return total

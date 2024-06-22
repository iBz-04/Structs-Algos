## Q:
"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

"""

## INTUITION:
"""
The positions are sorted to allow binary search on the possible distances.
The binary search is used to efficiently find the maximum minimum distance by checking if it is possible to place m balls with at least a given distance using the helper function good.
By adjusting the search range based on the result of good, the algorithm narrows down to the optimal distance.

"""

## code:
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        head = 0
        tail = position[-1]

        def good(x):
            start = -1e100

            count = 0
            for p in position:
                if p - start >= x:
                    start = p
                    count += 1
            return count >= m

        while head < tail:
            mid = (head + tail) // 2

            if good(mid + 1):
                head = mid + 1
            else:
                tail = mid
        return head
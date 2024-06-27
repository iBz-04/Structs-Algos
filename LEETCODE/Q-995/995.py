##Q:
"""
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

"""

## INTUITION:
"""
I use a greedy approach to find the minimum number of K-bit flips needed to make all elements in the array nums equal to 1.
 The flip array keeps track of positions where flips end, while the current variable maintains the state of the current bit after flips. As I iterate through nums, if the current bit (considering previous flips) is 0, I flip the next K bits starting at the current index. If I can't complete a K-bit flip because it would exceed the array bounds, I return -1. 
Otherwise, I continue, marking the end of each flip in the flip array, and return the total number of flips.
"""

## CODE:
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        flips = 0

        flip = [False] * N
        current = 0
        for i, x in enumerate(nums):
            if flip[i]:
                current ^= 1
            if (x ^ current) == 0:
                flips += 1
                current ^= 1
                if i + k > N:
                    return -1
                if i + k < N:
                    flip[i + k] = True
        return flips
## Q:
"""
"""

## intuition:
"""
The algorithm uses a sliding window approach with two pointers (left and right) to efficiently find subarrays with exactly k odd numbers.
The deque q helps in keeping track of the indices of the odd numbers,
 allowing the algorithm to quickly adjust the window size and calculate the number of valid subarrays.
By maintaining the window with exactly k odd numbers, the code ensures all counted subarrays meet the requirement.
"""

## CODE:
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)

        total = 0
        q = collections.deque()

        left = 0
        for right in range(N):
            if nums[right] % 2 == 1:
                q.append(right)
            while len(q) > k:
                left = q.popleft() + 1
            if len(q) == k:
                degree = q[0] - left + 1
                total += degree
        return total
        
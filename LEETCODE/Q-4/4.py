""" Q: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
"""

## Intuition:
""" To find the median of two sorted arrays, we need to consider the combined sorted order of both arrays. 
The median will be at the center of this combined array. 
Instead of merging both arrays, which is inefficient,
 we can use a binary search approach to find the correct partition of the arrays such that 
 the left half and the right half are properly balanced."""

## CODE:

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # Ensure A is the smaller array to minimize the binary search range
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Mid index for A
            j = half - i - 2  # index for B

            # Elements on the left and right side of the partition in A
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            # Elements on the left and right side of the partition in B
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Checking if partitions are correct
            if Aleft <= Bright and Bleft <= Aright:
                # If the total number of elements is odd, return the middle element
                if total % 2:
                    return min(Aright, Bright)
                # If the total number of elements is even, return the average of the two middle elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # If Aleft is greater than Bright, move the partition in A to the left
            elif Aleft > Bright:
                r = i - 1
            # If Bleft is greater than Aright, move the partition in A to the right
            else:
                l = i + 1

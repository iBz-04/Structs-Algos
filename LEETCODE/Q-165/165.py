## Q:
"""Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0. """

##INTUITION:
## To compare two version strings, I splitted them by periods and compared each part individually.

##APPROACH:
"""I converted the strings into lists of integers, ensuring equal length by appending zeros,
 then iterating through corresponding elements to compare them. from the comparison, 
i return -1 for the first version being less, 1 for it being greater, and 0 for equality."""

## CODE:
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def get_list(version):
            return list(map(int, version.split(".")))
        
        v1 = get_list(version1)
        v2 = get_list(version2)
        
        while len(v1) < len(v2):
            v1.append(0)
        while len(v2) < len(v1):
            v2.append(0)
        for s1, s2 in zip(v1, v2):
            if s1 < s2:
                return -1
            if s1 > s2:
                return 1
        return 0
        
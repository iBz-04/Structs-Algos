#Q:
"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array.
 Otherwise, return false.
"""



##INTUITION:
"""
looping through the array and updating a streak counter when consecutive odd numbers are found
"""

## CODE:
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
       #we initiate a counter that will store the odd numbers found in sort of a streak form

       count_streak = 0

       # we loop through the array to find odd numbers with modulo
       for i in arr:
          if i % 2 == 1:
       #increase streak if odd number is found
            count_streak += 1
          else:
       # else do not increase
            count_streak = 0
       # if streak count reaches three, return true
          if count_streak >= 3:
              return True
       return False

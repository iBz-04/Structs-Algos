## Q:
"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

## INTUITION:
"""
First, I defined the 32-bit integer limits: MIN and MAX. I initialized a result variable, res, to zero.
 Using a loop, I extracted the last digit of x with the modulus operation and update x by performing integer division by 10.
And to prevent overflow, I checked if multiplying res by 10 and adding the digit would exceed MIN or MAX. If it would, I return zero. 
Otherwise, I update res by shifting its digits left and adding the new digit.
"""

## CODE:
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > MAX // 10 or 
                (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or 
                (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit

        return res
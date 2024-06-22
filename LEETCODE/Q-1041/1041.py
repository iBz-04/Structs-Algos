## Q:
"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

"""
## INTUITION:
"""
Approach
The robot's position and direction are tracked. After executing all instructions, the code checks if the robot returns to the initial position or if it faces a different direction than the initial one.

Complexity
Time complexity:
O(n), where n is the length of the instructions string

Space complexity:
O(1)
"""

## CODE:
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directionX, directionY = 0, 1
        x, y = 0, 0
        for d in instructions:
            if d == "G":
                x, y = x + directionX, y + directionY
            elif d == "L":
                directionX, directionY = -1 * directionY, directionX
            else:
                directionX, directionY = directionY, -1 * directionX
        return (x, y) == (0, 0) or (directionX, directionY) != (0, 1)

        
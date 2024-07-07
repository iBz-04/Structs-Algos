# Q:
"""
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
"""

## APPROACH:
"""
Assume numBottles = 9 and numExchange = 3:

-Initially, you have 9 full bottles.
-You drink 9 bottles, resulting in 9 empty bottles.
-You can exchange 9 empty bottles for 3 full bottles (9 // 3 = 3).
-Drink those 3 bottles, get 3 empty bottles.
-Exchange those 3 empty bottles for 1 full bottle (3 // 3 = 1).
-Drink that 1 bottle, get 1 empty bottle.
-Now you can’t exchange anymore as you need at least 3 empty bottles to get a full one.
-Total bottles drank = 9 (initial) + 3 (first exchange) + 1 (second exchange) = 13.
"""
## COMPLEXITIES:
"""
Time complexity:
-O(1), because the operation runs once and doesn't change with input - this means the complexity is constant

Space complexity:
-O(1)
"""

## CODE:
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + math.floor((numBottles-1)/(numExchange-1))

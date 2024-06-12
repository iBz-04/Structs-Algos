## Q:
'''You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.'''

##INTUITION:
'''If it's a "+", the score is the sum of the last two valid rounds.
If it's "D", the score is double the last valid round.
If it's "C", the last valid round is removed.
Otherwise, if it's a number, it's a valid round and is added to the score'''

## APPROACH:
#  the total score is calculated by summing up all the elements in the stack.

## CODE:
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for o in operations:
            if o == "+":
                stack.append(stack[-1]+stack[-2])
            elif o == "D":
                stack.append(stack[-1]*2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        return sum(stack)
        
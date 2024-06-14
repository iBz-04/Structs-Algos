## Q:
"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution."""

## INTUITION:
"""
I used backtracking
This algorithm tries to solve the problem by making a series of choices, and if it finds a choice that leads to a solution, it continues. If it encounters a dead end, it backtracks and tries another choice. This is done recursively until a solution is found or all possibilities are exhausted.
Before placing a number in a cell, the code checks if the number can be placed there(no repeated numbers in the same row, column, or 3x3 subgrid).
"""
##NOTE: THIS IS A HARD QUESTION

##CODE:
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
           """
        
        def is_valid(num, row, col):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                     return False
            return True
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(num, i, j):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True
        solve()
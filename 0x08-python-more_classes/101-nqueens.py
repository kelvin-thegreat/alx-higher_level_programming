#!/usr/bin/python3
"""Python module for calculation"""

import sys

def nqueens(N):
    # check if N is an integer
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # initialize empty board
    board = [-1] * N

    # define function to check if a queen can be placed in a given row and column
    def can_place(row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    # define function to place queens on the board
    def place_queens(row):
        if row == N:
            # all queens have been placed, print solution
            print(" ".join(str(x + 1) for x in board))
        else:
            for col in range(N):
                if can_place(row, col):
                    board[row] = col
                    place_queens(row + 1)

    # start placing queens
    place_queens(0)

# check if program was called with correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# solve N queens puzzle
nqueens(sys.argv[1])


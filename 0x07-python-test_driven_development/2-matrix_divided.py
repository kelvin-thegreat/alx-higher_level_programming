#!/usr/bin/python3
"""
Function module tha divides the number of a matrix

"""

def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by a given number.

    Arguments:
    matrix -- a list of lists of integers or floats.
    div -- a number (integer or float).

    Returns:
    a new matrix, with all elements of the input matrix divided by div,
    rounded to 2 decimal places.

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
         zeroDivisionError: if the division is zero          
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return (new_matrix)

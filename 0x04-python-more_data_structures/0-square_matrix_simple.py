#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Returns a new matrix with the same size as the input matrix,
    where each value is the square of the corresponding value in the input.
    The input matrix is not modified.
    """
    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in row] for row in matrix]

    # Compute the square value of each integer in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    return result


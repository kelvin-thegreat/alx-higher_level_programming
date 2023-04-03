#!/usr/bin/python3
"""

Module composed by a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


    """

    # Validate input matrices
    for matrix in [m_a, m_b]:
        # Check that matrix is a list
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        # Check that matrix is a list of lists
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
        # Check that matrix is not empty
        if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
            raise ValueError("m_a can't be empty or m_b can't be empty")
        # Check that matrix contains only integers or floats
        if not all(isinstance(val, (int, float)) for row in matrix for val in row):
            raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    # Check that matrices are rectangular
    row_sizes = set(len(row) for row in m_a + m_b)
    if len(row_sizes) != 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check that matrices can be multiplied
    a_rows, a_cols = len(m_a), len(m_a[0])
    b_rows, b_cols = len(m_b), len(m_b[0])
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result

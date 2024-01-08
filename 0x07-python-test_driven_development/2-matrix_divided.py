#!/usr/bin/python3
"""

Module divides an element by a number indicated

"""


def matrix_divided(matrix, div):
    """
    Matrix Divider Method
    """
    if isinstance(div, int) == 0 and isinstance(div, float) == 0:
        raise TypeError("div must be a number")
    new_matrix = []
    i = 0
    for row in matrix:
        temp = []
        for element in row:
            if isinstance(element, int) or isinstance(element, float):
                temp.append(round((element / div), 2))
            else:
                line1 = "matrix must be a matrix (list of lists)"
                line2 = " of integers/floats"
                raise TypeError(line1 + line2)
        if i != 0:
            if i != len(row):
                line1 = "Each row of the matrix"
                line2 = " must have the same size"
                raise TypeError(line1 + line2)
        i = len(row)
        new_matrix.append(temp)
    return new_matrix

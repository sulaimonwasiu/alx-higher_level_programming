#!/usr/bin/python3
"""Multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if (type(element) is not int) and (type(element) is not float):
                raise TypeError("m_a should contain only integers or float")
    for row in m_b:
        for element in row:
            if (type(element) is not int) and (type(element) is not float):
                raise TypeError("m_b should contain only integers or float")

    i = 0
    for row in m_a:
        for element in row:
            if i != 0:
                if i != len(row):
                    raise TypeError("each row of m_a must be of the same size")
            i = len(row)
    j = 0
    for row in m_a:
        for element in row:
            if j != 0:
                if j != len(row):
                    raise TypeError("each row of m_b must be of the same size")
            j = len(row)
    # Perform matrix multiplication
    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

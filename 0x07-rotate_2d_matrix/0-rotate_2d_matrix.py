#!/usr/bin/python3
"""
A module that implements a 2d matrix rotation
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a m * n 2D matrix in place
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    column = len(matrix[0])
    if not all(map(lambda x: len(x) == column, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(column * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
            matrix[-1].append(mtrix[r][c])
            if c == column - 1 and r >= -1:
                matrix.pop(r)
            r -= 1

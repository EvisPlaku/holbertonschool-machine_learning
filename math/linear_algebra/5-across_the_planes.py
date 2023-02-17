#!/usr/bin/env python3
"""Add two matrices elementwise"""

"""
def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    return [[ele1 + ele2 for ele1, ele2 in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]
"""
def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    result = [[0 for j in range(len(mat1[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

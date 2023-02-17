#!/usr/bin/env python3
""" defines function that transposes a 2D matrix """

#def matrix_transpose(matrix):
#    """returns the transposed matrix"""
#    return [[row[idx] for row in matrix] for idx in range(len(matrix[0]))]

def matrix_transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transpose = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    return transpose

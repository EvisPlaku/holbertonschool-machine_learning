#!/usr/bin/env python3
""" defines function that transposes a 2D matrix """

def matrix_transpose(matrix):
    """returns the transposed matrix"""
    return [[row[idx] for row in matrix] for idx in range(len(matrix[0]))]

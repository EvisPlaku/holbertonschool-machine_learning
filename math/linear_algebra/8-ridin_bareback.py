#!/usr/bin/env python3
"""Multiply two matrices"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication between two matrices mat1 and mat2."""
    # Check if the two matrices can be multiplied
    if len(mat1[0]) != len(mat2):
        return None
    # Create an empty result matrix with the appropriate dimensions
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    # Perform the multiplication and store the result in the new matrix
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

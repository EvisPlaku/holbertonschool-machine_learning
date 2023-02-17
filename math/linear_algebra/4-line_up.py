#!/usr/bin/env python3
"""Add two arrays elementwise"""

"""
def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
"""

def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result

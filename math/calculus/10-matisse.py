#!/usr/bin/env python3
""" defines a function that calculates the derivative of a polynomial """


def poly_derivative(poly):
    if type(poly) != list or len(poly) == 0:
        return None
    if len(poly) == 1 or poly == [0]:
        return [0]
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])
    return derivative

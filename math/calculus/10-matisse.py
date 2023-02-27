#!/usr/bin/env python3
""" defines a function that calculates the derivative of a polynomial """


def poly_derivative(poly):
    """
    calculates the derivative of the given polynomial
    Parameters:
        poly (list): list of coefficients representing a polynomial
            the index of the list represents the power of x
            the coefficient belongs to
    Returns:
        a new list of coefficients representing the derivative
        [0], if the derivate is 0
        None, if poly is not valid
    """
    # check if the polynomial is constant or zero
    if len(poly) == 1 or poly == [0]:
        return [0]

    # compute the derivative of the polynomial
    derivative = []
    for i in range(1, len(poly)):
        coefficient = i * poly[i]
        derivative.append(coefficient)
    if len(derivative) == 0:
        derivative.append(0)
    return derivative

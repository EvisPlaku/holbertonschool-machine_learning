#!/usr/bin/env python3
""" defines a function that calculates the integral of a polynomial """


def poly_integral(poly, C=0):
    if not isinstance(C, int) or not isinstance(poly, list) or len(poly) == 0:
        return None
    integral = [C]
    for i, coef in enumerate(poly):
        if not isinstance(coef, int):
            return None
        power = i + 1
        if coef % power != 0:
            return None
        integral.append(coef // power)
    return integral

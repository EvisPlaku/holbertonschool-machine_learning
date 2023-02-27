#!/usr/bin/env python3
""" defines a function that calculates the integral of a polynomial """


def poly_integral(poly, C=0):
    if type(poly) != list or len(poly) == 0:
        return None

    integral = [C]

    for i in range(len(poly)):
        coef = poly[i] / (i + 1)

        if coef.is_integer():
            coef = int(coef)

        integral.append(coef)

    while integral[-1] == 0 and len(integral) > 1:
        integral.pop()

    return integral

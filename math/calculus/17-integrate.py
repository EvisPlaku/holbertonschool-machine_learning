#!/usr/bin/env python3
""" defines a function that calculates the integral of a polynomial """

def poly_integral(poly, C=0):
    # Check if poly is valid
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None

    # Check if C is valid
    if not isinstance(C, int):
        return None

    # Integrate the polynomial and append the integration constant
    integral_coeffs = [C]
    for i in range(len(poly)):
        coeff = poly[i] / (i+1)
        if coeff.is_integer():
            coeff = int(coeff)
        integral_coeffs.append(coeff)

    # Remove trailing zeros
    while len(integral_coeffs) > 1 and integral_coeffs[-1] == 0:
        integral_coeffs.pop()

    return integral_coeffs

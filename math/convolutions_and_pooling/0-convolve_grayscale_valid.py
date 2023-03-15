#!/usr/bin/env python3
"""
Defines a function that performs valid convolution
on a grayscale image
"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images
    """
    m, height, width =  images.shape
    kernel_height, kernel_width  = kernel.shape
    out_height = height - kernel_height + 1
    out_width  = width - kernel_width + 1
    convoluted = np.zeros((m, out_height, out_width))
    for h in range(out_height):
        for w in range(out_width):
            output = np.sum(images[:, height: height + kernel_height, width: width + kernel_width] * kernel, axis=1).sum(axis=1)
            convoluted[:, height, width] = output
    return convoluted

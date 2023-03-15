import numpy as np

def convolve_grayscale_valid(images, kernel):
    m, h, w = images.shape
    kh, kw = kernel.shape
    # Compute output size
    oh, ow = h - kh + 1, w - kw + 1
    output = np.zeros((m, oh, ow))
    # Perform convolution for each image
    for i in range(m):
        for j in range(oh):
            for k in range(ow):
                output[i, j, k] = np.sum(images[i, j:j+kh, k:k+kw] * kernel)
    return output

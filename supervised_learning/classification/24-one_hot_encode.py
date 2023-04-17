#!/usr/bin/env python3

import numpy as np

def one_hot_encode(Y, classes):
    """
    Converts a numeric label vector into a one-hot matrix.
    
    Arguments:
    Y -- numpy.ndarray with shape (m,) containing numeric class labels
    classes -- maximum number of classes found in Y
    
    Returns:
    one-hot encoding of Y with shape (classes, m), or None on failure
    """
    if not isinstance(Y, np.ndarray) or Y.ndim != 1:
        return None
    
    try:
        onehot = np.zeros((classes, Y.shape[0]))
        onehot[Y, np.arange(Y.shape[0])] = 1
        return onehot
    except:
        return None

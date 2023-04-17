#!/usr/bin/env python3

import numpy as np

def one_hot_decode(one_hot):
    """
    Converts a one-hot matrix into a vector of labels.
    
    Args:
    one_hot (numpy.ndarray): One-hot encoded matrix with shape (classes, m)
    
    Returns:
    numpy.ndarray: Numeric labels for each example with shape (m, ), or None on failure
    """
    try:
        # Get the number of classes and examples
        classes, m = one_hot.shape
        
        # Find the indices of the maximum values along the first axis (classes)
        indices = np.argmax(one_hot, axis=0)
        
        # Return the indices as labels
        return indices
    
    except:
        return None

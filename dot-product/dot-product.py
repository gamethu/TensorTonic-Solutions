import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.asarray(x)
    y = np.asarray(y)

    res = x*y*np.cos(0)
    return sum(res)
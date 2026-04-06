import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x)

    res = 1/(1+np.exp(-x))
    return res
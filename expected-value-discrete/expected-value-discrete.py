import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if sum(p) != 1: 
        raise ValueError()
    
    x = np.asarray(x)
    p = np.asarray(p)

    res = x*p
    return sum(res)
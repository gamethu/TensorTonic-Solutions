import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows = len(A)
    cols = len(A[0])
    
    res = list()
    for j in range(cols):
        res.append([None] * rows)
        for i in range(rows):
            res[j][i] = A[i][j]
    return np.asarray(res)
            

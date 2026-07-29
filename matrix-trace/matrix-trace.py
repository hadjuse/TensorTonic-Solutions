import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.array(A)
    n, m = A.shape

    trace = 0
    for i in range(n):
        for j in range(m):
            if i == j:
                trace += A[i][j]
    
    return trace

import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    A = np.asarray(A, dtype=np.float64)
    result = 0
    for i in range(A.shape[0]):
        result += A[i,i]
    return float(result)
        
    
    
    
    
    
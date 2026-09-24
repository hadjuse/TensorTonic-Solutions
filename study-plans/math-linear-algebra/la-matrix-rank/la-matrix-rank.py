import numpy as np

def matrix_rank(A: list) -> int:
    """
    Returns the numerical rank as a Python integer.
    """
    A = np.asarray(A, dtype=np.float64)
    
    return int(np.linalg.matrix_rank(A))
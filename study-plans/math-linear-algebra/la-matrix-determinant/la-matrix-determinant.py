import numpy as np

def matrix_determinant(A: list) -> float:
    """
    Returns the determinant as a Python float.
    """
    A = np.asarray(A, dtype=np.float64)
    
    return float(np.linalg.det(A))
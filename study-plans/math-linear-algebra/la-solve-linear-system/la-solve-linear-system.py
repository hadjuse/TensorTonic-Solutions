import numpy as np

def solve_linear_system(A: list, b: list) -> np.ndarray:
    """
    Returns the float64 solution vector.
    """
    A = np.asarray(A, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    
    return np.linalg.solve(A, b) 
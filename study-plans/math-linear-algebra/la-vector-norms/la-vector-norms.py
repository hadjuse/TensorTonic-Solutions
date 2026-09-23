import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    v = np.asarray(v, dtype=np.float64)
    l1_norm = np.sum(np.abs(v))
    l2_norm = np.sqrt(np.sum(v ** 2))
    l_infinite_norm = np.max(np.abs(v))
    return np.array([l1_norm, l2_norm, l_infinite_norm])
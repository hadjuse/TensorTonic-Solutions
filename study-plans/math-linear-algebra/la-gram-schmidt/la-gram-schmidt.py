import numpy as np

def gram_schmidt(vectors: list) -> np.ndarray:
    """
    Returns a float64 array whose rows form the ordered orthonormal basis.
    """
    source = np.asarray(vectors, dtype=np.float64)
    basis = np.zeros_like(source, dtype=np.float64)
    for i in range(source.shape[0]):
        residual = source[i].copy()
        for j in range(i):
            residual -= np.dot(residual, basis[j]) * basis[j]
        basis[i] = residual / np.linalg.norm(residual)
    return basis

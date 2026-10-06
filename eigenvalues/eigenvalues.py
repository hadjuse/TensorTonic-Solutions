import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix = np.asarray(matrix)
    eigenvalues = np.linalg.eigvals(matrix).real
    print(eigenvalues)
    return np.sort(eigenvalues)
import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    matrix=np.zeros((len(v), len(v)), dtype=float)
    print(matrix)
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            if i==j:
                matrix[i][j]=v[i]

    return matrix

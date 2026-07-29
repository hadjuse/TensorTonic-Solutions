import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    shape_of_A = A.shape
    shape_of_A_T = A.shape[::-1]
    A_T = np.zeros(shape_of_A_T)
    for i in range(shape_of_A[0]):
        for j in range(shape_of_A[1]):
            A_T[j][i] = A[i][j]
    return A_T

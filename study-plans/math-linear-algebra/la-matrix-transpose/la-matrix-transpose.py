import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transpose as a float64 array.
    """
    A = np.array(A, dtype=np.float64)
    A_T_Shape = (A.shape[1], A.shape[0])
    print(A_T_Shape)
    A_T = np.zeros(A_T_Shape) 
    print(A_T)
    for i in range(A_T_Shape[0]):
        for j in range(A_T_Shape[1]):
            A_T[i][j] = A[j][i]
            
    return np.asarray(A_T, dtype=np.float64)
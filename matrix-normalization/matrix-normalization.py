import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrix = np.asarray(matrix)
    # Write code here
    if norm_type == "l1":
        row_sum = np.sum(matrix, axis=axis, keepdims=True)
        print("row sum l1", row_sum)
        l1_row_norm = matrix/row_sum
        print(l1_row_norm)
        return l1_row_norm
    elif norm_type == "l2":
        row_sum_squared = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
        print(row_sum_squared)
        l2_row_norm = matrix / row_sum_squared
        l2_row_norm[np.isnan(l2_row_norm)] = 0
        return l2_row_norm 
    else:
        row_max = np.max(matrix, axis=axis, keepdims=True)
        return matrix / row_max
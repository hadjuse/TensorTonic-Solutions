import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    data = np.asarray(data, dtype=np.float64)
    
    element_mask = (data > threshold).astype(float)
    any_row_threshold = data * np.any(data > threshold, axis = 1, keepdims=True)
    all_row_threshold = data * np.all(data > threshold, axis = 1, keepdims=True)
    
    print(element_mask, any_row_threshold, all_row_threshold)
    
    output = np.stack([element_mask, any_row_threshold, all_row_threshold])
    return output

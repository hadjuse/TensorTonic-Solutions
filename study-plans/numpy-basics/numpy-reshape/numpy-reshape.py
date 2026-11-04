import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data = np.asarray(data, dtype=np.float64)
    if operation == "flatten":
        data = data.flatten()
    elif operation == "transpose":
        data = data.T
    elif operation == "add_batch":
        data = np.expand_dims(data, axis=0)

    return data

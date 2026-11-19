import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.asarray(y)
    encoded = np.zeros((y.size, max(y) + 1))
    if num_classes is not None:
        encoded = np.zeros((y.size, num_classes))

        encoded[np.arange(y.size), y] = 1.0
    else:
        encoded[np.arange(y.size), y] = 1.0
    print(encoded)
    return encoded
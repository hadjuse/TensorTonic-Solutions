import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    product = np.dot(x,y)
    z = float(product)
    print(z)
    return z
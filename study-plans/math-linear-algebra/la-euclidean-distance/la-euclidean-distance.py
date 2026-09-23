import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    substraction = sum((x - y) **2)

    distance = float(np.sqrt(substraction))
    print(distance)
    return distance
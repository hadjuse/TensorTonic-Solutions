import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    # Write code here
    v = np.asarray(v, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    cosine = np.dot(v,w) / (np.sqrt(np.sum(v**2)) * np.sqrt(np.sum(w**2)))
    print(cosine)
    cosine = np.clip(cosine, -1.0, 1.0)
    angle = np.arccos(cosine)
    return angle
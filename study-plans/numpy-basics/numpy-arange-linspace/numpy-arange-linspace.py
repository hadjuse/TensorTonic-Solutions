import numpy as np

def create_sequence(start: float, stop: float, param: float, kind: str) -> np.ndarray:
    """
    Returns a 1D float64 array containing the requested sequence.
    """

    a = np.arange(start, stop, param)
    b = np.linspace(start, stop, int(param))
    return np.asarray(a, dtype=np.float64) if kind == "arange" else np.asarray(b, dtype=np.float64)

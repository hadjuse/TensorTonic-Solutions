import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x)
    n = len(x)
    x_mean = np.mean(x)
    var = np.sum((x-x_mean)**2) / (n - 1)
    standar_deviation = np.sqrt(var)
    return {"variance": float(var), "standard_deviation": float(standar_deviation)}
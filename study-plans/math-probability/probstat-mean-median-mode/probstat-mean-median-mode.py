import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    results={}
    x_np = np.array(x)
    mean = np.mean(x_np)
    median = np.median(x_np)
    mode = max(Counter(x_np), key = x.count)
    print(mean, median, mode)
    results["mean"] = mean
    results["median"] = median
    results["mode"] = mode
    return results
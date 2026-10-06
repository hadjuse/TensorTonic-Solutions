import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.asarray(x)
    x_mean = x.mean(axis=0)
    x_centered = x-x_mean
    sample_standard_deviation = np.sqrt(np.sum(x_centered**2)/(x.shape[0]-1))
    t = (x_mean - mu0) / (sample_standard_deviation/np.sqrt(x.shape[0]))
    return float(t)
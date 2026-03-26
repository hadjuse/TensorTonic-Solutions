import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here4
    x = np.array(x, dtype=float)
    erf = np.vectorize(math.erf)
    geluf = (1/2) * x * (1 + erf(x/math.sqrt(2)))
    print(geluf)
    return geluf       
    # print(math.erf(x/math.sqrt(2)))
    # print(np.vectorize(math.erf(x/math.sqrt(2))))
    # geluf = (1/2) * x * (1 + np.vectorize(math.erf(x/math.sqrt(2))))
    # print(geluf)
    # return geluf

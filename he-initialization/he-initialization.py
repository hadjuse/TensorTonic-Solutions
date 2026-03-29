import numpy as np
import math
def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    W = np.array(W, dtype=float)
    limit = math.sqrt(6/fan_in)
    W_Initialized = W*2*limit-limit
    print(W_Initialized)
    return W_Initialized
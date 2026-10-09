import math

def xavier_initialization(W: list, fan_in: int, fan_out: int) -> list:
    """
    Returns the weights mapped to the Xavier uniform range.
    """
    # Write code here
    L = math.sqrt(6 / (fan_in + fan_out))
    W_init=W
    for i in range(len(W)):
        for j in range(len(W[i])):
            W_init[i][j] = W_init[i][j] * 2*L - L
    return W_init
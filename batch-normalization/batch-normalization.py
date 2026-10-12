import numpy as np

def batch_norm_forward(x: list, gamma: list, beta: list, eps: float = 1e-5) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    gamma = np.asarray(gamma, dtype=float)
    beta = np.asarray(beta, dtype=float)

    if x.ndim == 4:
        axes = (0, 2, 3)
        gamma = gamma.reshape(1, -1, 1, 1)
        beta = beta.reshape(1, -1, 1, 1)
    else:
        axes = 0

    mean = x.mean(axis=axes, keepdims=True)
    var = x.var(axis=axes, keepdims=True)

    x_hat = (x - mean) / np.sqrt(var + eps)
    return gamma * x_hat + beta
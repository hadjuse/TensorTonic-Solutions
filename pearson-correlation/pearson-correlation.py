import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    print(X.shape)
    X_mean_axis_0 = X.mean(axis=0, keepdims=True)

    print("Axis 0 of X: ", X_mean_axis_0)

    Center_X_axis_0 = X - X_mean_axis_0
      

    print("Center X_0: ", Center_X_axis_0)

    
    covariance = Center_X_axis_0.T @ Center_X_axis_0 / (X.shape[0] - 1)
    
    print("Matmult: ", Center_X_axis_0.T @ Center_X_axis_0)
    print("Covariance: ", covariance)
    
    std_dev_X_0 = np.sqrt(np.sum(Center_X_axis_0 ** 2, axis=0) / (X.shape[0] - 1))

    print("Std dev axis 0: ", std_dev_X_0)
    
    denom = np.outer(std_dev_X_0, std_dev_X_0)
    
    correlation = covariance / denom

    print("Correlation: ", correlation)
    return correlation
import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    X_mean_column = np.mean(X, axis=0)
    N = len(X)
    
    Center_data = X - X_mean_column
    
    cov = Center_data.T @ Center_data / (N - 1) 
    
    print(cov)
    return cov
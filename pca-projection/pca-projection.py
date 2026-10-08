import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X)
    X_Centered = X - X.mean(axis=0)
    n = X.shape[0]
    covarience = X_Centered.T @ X_Centered / (n - 1)
    eigenvalues, eigenvectors = np.linalg.eigh(covarience)
    print("eigen vector:", eigenvectors)
    # np.argsort get the indices for the eigenvalues to sort eigenvectores with these indices
    sorted_indices = np.argsort(eigenvalues)[::-1]
    W = eigenvectors[:, sorted_indices[:k]]
    X_proj=X_Centered @ W
    print(X_proj)
    return X_proj
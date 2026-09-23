import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)

    if not np.count_nonzero(a) or not np.count_nonzero(b):
        return float(0)
    
    dot_product = np.dot(a, b)
    
    magnitude_vector_a = np.sqrt(sum(a ** 2))
    magnitude_vector_b = np.sqrt(sum(b ** 2))

    cosine = float(dot_product / (magnitude_vector_a * magnitude_vector_b))
    
    return cosine
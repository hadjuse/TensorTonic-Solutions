import numpy as np

def filter_and_extract(data: list, row_start: int, row_stop: int, threshold: float) -> np.ndarray:
    """
    Returns matching values in row-major order as a 1D float64 array.
    """
    data = np.asarray(data, dtype = np.float64)
    data_filtered = data[row_start:row_stop]
    mask = data_filtered > threshold
    print(data_filtered)
    output = data_filtered[mask]
    # print(output)
    return output

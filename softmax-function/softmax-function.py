import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x, dtype="float64")
    print(len(x.shape))
    if len(x.shape) == 1:
        softmax = np.exp(x-np.max(x))/np.sum(np.exp(x-np.max(x)))
        print(softmax)
    else:
        exp=np.exp(x-np.max(x, axis=1, keepdims=True))
        softmax = exp/np.sum(exp, axis=1, keepdims=True)
        
    return softmax
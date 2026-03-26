import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.array(x, dtype="float")
    print(len(x.shape))    
    is_shape_eq_or_gt_two = True if len(x.shape) > 1 else False

    numerator = np.exp(x) - np.exp(-x)
    denominator = np.exp(x) + np.exp(-x)

    tanhyp=numerator/(denominator)
    if is_shape_eq_or_gt_two:
        print("shapes")
        return tanhyp
            
        
    return tanhyp
    pass
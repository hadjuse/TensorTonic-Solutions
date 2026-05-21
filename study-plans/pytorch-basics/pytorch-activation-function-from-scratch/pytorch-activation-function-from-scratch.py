import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype = torch.float32)
    method_is_relu = method == "relu"
    method_is_sigmoid = method == "sigmoid"
    method_is_tanh= method == "tanh"
    method_is_leaky_relu = method == "leaky_relu"
    print("here")
    if method_is_relu:
        return torch.clamp(x, min=0).tolist()
    elif method_is_sigmoid:
        return (1 / (1 + torch.exp(-x))).tolist()
    elif method_is_tanh:
        numerator = torch.exp(x) - torch.exp(-x)
        denominator = torch.exp(x) + torch.exp(-x)
        
        return (numerator / denominator).tolist()
    elif method_is_leaky_relu:
        return torch.where(x > 0, x, 0.01 *x ).tolist()
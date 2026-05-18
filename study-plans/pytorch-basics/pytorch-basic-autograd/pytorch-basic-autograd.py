import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    
    x = torch.tensor(values, dtype = torch.float32, requires_grad=True)
    x_pow_3 = torch.pow(x, 3)
    two_x = 2 * x
    y = sum(x_pow_3 + two_x)
    y_backward = y.backward()
    x_grad = x.grad.tolist()
    return x_grad
    

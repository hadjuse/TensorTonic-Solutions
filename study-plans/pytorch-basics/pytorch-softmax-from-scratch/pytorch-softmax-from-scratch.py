import torch

def softmax(logits):
    """
    Returns: tensor of same shape with softmax probabilities (each row sums to 1)
    """
    z = torch.tensor(logits, dtype=torch.float32)
    softmax_calc=torch.exp(z - torch.max(z, dim=1, keepdim=True).values)/torch.sum(torch.exp(z-torch.max(z, dim=1 , keepdim=True).values), dim=1, keepdim=True)
    return softmax_calc

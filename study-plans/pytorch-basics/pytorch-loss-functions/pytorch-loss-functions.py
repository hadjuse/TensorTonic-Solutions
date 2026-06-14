import torch

def compute_loss(pred, target, method, delta=1.0):
    """
    Returns: float, the mean loss value
    """
    loss = 0
    pred = torch.tensor(pred, dtype = torch.float32)
    target = torch.tensor(target, dtype=torch.float32)
    if method == "mse":
        loss = ((pred - target) ** 2).mean()
    elif method == "cross_entropy":
        print(len(pred[0]))
        print(target[0])
        print(pred.shape[0], pred.shape[1])
        total  = 0
        for i in range(pred.shape[0]):
            total += torch.nn.functional.log_softmax(pred[i])[target[i].to(torch.int64)]
        loss = -1 * (total / pred.shape[0])
    elif method == "huber":
        a = pred - target
        loss = torch.where(torch.abs(a) <= delta, 0.5*(a**2), delta*(torch.abs(a)-0.5*delta)).mean()
    return loss

import torch
import torch.nn as nn

class CustomLinear(nn.Module):
    """
    Returns: y = x W^T + b without using nn.Linear
    """

    def __init__(self, in_features, out_features):
        super().__init__()
        # self.param=nn.Parameter(torch.empty((out_features, in_features)))
        self.weight = nn.Parameter(nn.init.kaiming_uniform(torch.empty((out_features, in_features))))
        self.bias = nn.Parameter(torch.empty(out_features))

    def forward(self, x):
        print("1")
        x= torch.tensor(x, dtype = torch.float32, requires_grad=True)
        print("2")
        y = x @ self.weight.t() + self.bias
        print("3")
        # y_backward = y.backward()
        print("4")
        return y

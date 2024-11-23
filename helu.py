import torch
from torch import autograd


class HeLUFunction(autograd.Function):
    @staticmethod
    def forward(ctx, z, alpha=0.05):
        ctx.save_for_backward(z)
        ctx.alpha = alpha
        return torch.where(z > 0, z, 0)

    @staticmethod
    def backward(ctx, grad_output):
        z, = ctx.saved_tensors
        alpha = ctx.alpha
        return torch.where(z > -alpha, grad_output, 0), None


class HeLU(torch.nn.Module):
    def __init__(self, alpha=0.05):
        super(HeLU, self).__init__()
        self.alpha = alpha

    def forward(self, input):
        return HeLUFunction.apply(input, self.alpha)

    def __repr__(self):
        return self.__class__.__name__ + ' (' \
            + 'alpha=' + str(self.alpha) + ')'

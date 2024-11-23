# HeLU
Hysteresis Rectified Linear Unit

### Abstract:
The widely used ReLU is favored for its hardware efficiencyas the implementation at inference is a one bit sign case, yet suffers from
issues such as the “dying ReLU” problem, where during training, neurons fail
to activate and constantly remain at zero, as highlighted by Lu et al. [ 16]. Traditional approaches to mitigate this issue often introduce more complex and less
hardware-friendly activation functions. In this work, we propose a Hysteresis
Rectified Linear Unit (HeLU), an efficient activation function designed to address
the “dying ReLU” problem with minimal complexity. Unlike traditional activation
functions with fixed thresholds for training and inference, HeLU employs a variable
threshold that refines the backpropagation. This refined mechanism allows simpler
activation functions to achieve competitive performance comparable to their more
complex counterparts without introducing unnecessary complexity or requiring
inductive biases. Empirical evaluations demonstrate that HeLU enhances model
generalization across diverse datasets, offering a promising solution for efficient
and effective inference suitable for a wide range of neural network architectures.

# HeLU
Hysteresis Rectified Linear Unit

### Abstract:
The widely used ReLU is favored for its hardware efficiency yet suffers from
2 issues such as the “dying ReLU” problem, where during training, neurons fail
3 to activate and constantly remain at zero, as highlighted by Lu et al. [16]. Tra4 ditional approaches to mitigate this issue often introduce more complex and less
5 hardware-friendly activation functions. In this work, we propose a Hysteresis
6 Rectified Linear Unit (HeLU), an efficient activation function designed to address
7 the “dying ReLU” problem with minimal complexity. Unlike traditional activation
8 functions with fixed thresholds for training and inference, HeLU employs a variable
9 threshold that refines the backpropagation. This refined mechanism allows simpler
10 activation functions to achieve competitive performance comparable to their more
11 complex counterparts without introducing unnecessary complexity or requiring
12 inductive biases. Empirical evaluations demonstrate that HeLU enhances model
13 generalization across diverse datasets, offering a promising solution for efficient
14 and effective inference suitable for a wide range of neural network architectures.


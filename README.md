# Hysteresis Rectified Linear Unit (HeLU)
Accepted to 4th NeurIPS Efficient Natural Language and Speech Processing Workshop ([ENLSP-IV 2024](https://neurips2024-enlsp.github.io/))

[Poster](https://neurips.cc/virtual/2024/106479)

[Paper](https://proceedings.mlr.press/v262/kimhi24a.html)

### Abstract:
The widely used ReLU is favored for its hardware efficiencyas the implementation at inference is a one bit sign case, yet suffers from
issues such as the “dying ReLU” problem, where during training, neurons fail
to activate and constantly remain at zero, as highlighted by Lu et al. [16]. Traditional approaches to mitigate this issue often introduce more complex and less
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

### Cite

Bibtex:
```
@InProceedings{pmlr-v262-kimhi24a,
  title = 	 {Hysteresis Activation Function for Efficient Inference},
  author =       {Kimhi, Moshe and Kashani, Idan and Baskin, Chaim and Mendelson, Avi},
  booktitle = 	 {Proceedings of The 4th NeurIPS Efficient Natural Language and Speech Processing Workshop},
  pages = 	 {414--422},
  year = 	 {2024},
  editor = 	 {Rezagholizadeh, Mehdi and Passban, Peyman and Samiee, Soheila and Partovi Nia, Vahid and Cheng, Yu and Deng, Yue and Liu, Qun and Chen, Boxing},
  volume = 	 {262},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {14 Dec},
  publisher =    {PMLR},
  pdf = 	 {https://raw.githubusercontent.com/mlresearch/v262/main/assets/kimhi24a/kimhi24a.pdf},
  url = 	 {https://proceedings.mlr.press/v262/kimhi24a.html},
  abstract = 	 {The widely used ReLU is favored for its hardware efficiency yet suffers from issues such as the “dying ReLU” problem, where during training, neurons fail to activate and constantly remain at zero, as highlighted by Lu et al.&nbsp;\citep{lu2018collapse}. Traditional approaches to mitigate this issue often introduce more complex and less hardware-friendly activation functions. In this work, we propose a Hysteresis Rectified Linear Unit (HeLU), an efficient activation function designed to address the “dying ReLU” problem with minimal complexity. Unlike traditional activation functions with fixed thresholds for training and inference, HeLU employs a variable threshold that refines the backpropagation. This refined mechanism allows simpler activation functions to achieve competitive performance comparable to their more complex counterparts without introducing unnecessary complexity or requiring inductive biases. Empirical evaluations demonstrate that HeLU enhances model generalization across diverse datasets, offering a promising solution for efficient and effective inference suitable for a wide range of neural network architectures.}
}
```

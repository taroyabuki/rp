from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train.shape
#> (60000, 28, 28)

import numpy as np
np.set_printoptions(linewidth=170)
x_train[4, :, :]

import matplotlib.pyplot as plt
plt.matshow(x_train[4, :, :])

[x_train.min(), x_train.max()]
#> [0, 255]

x_train = x_train / 255
x_test  = x_test  / 255

y_train
#> array([5, 0, 4, ..., 5, 6, 8], dtype=uint8)

import random
my_index = random.sample(range(60000), 6000)
x_train = x_train[my_index, :, :]
y_train = y_train[my_index]


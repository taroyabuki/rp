from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt
plt.matshow(x_train[4, :, :])
plt.savefig('12-p-mnist-id5.pdf')

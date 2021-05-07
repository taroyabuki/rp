from keras import datasets
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

import matplotlib.pyplot as plt
plt.matshow(x_train[4, :, :])
plt.savefig('11-p-mnist-id5.pdf')

import numpy
numpy.random.seed(0)

from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.utils import shuffle
X, y = shuffle(X, y)

from keras.models import Sequential
from keras.layers import Dense

my_model = Sequential()
my_model.add(Dense(units=3, activation='relu', input_dim=4))
my_model.add(Dense(units=3,               # 出力層のニューロン数
                   activation='softmax')) # 活性化関数

from sklearn.preprocessing import StandardScaler
my_scaler = StandardScaler()
X = my_scaler.fit_transform(X) # 標準化
# yはそのまま使う．

my_model.compile(loss = 'sparse_categorical_crossentropy',
                 optimizer = 'rmsprop',
                 metrics = ['accuracy'])

my_history = my_model.fit(x=X, y=y, validation_split=0.25,
                          batch_size=1, epochs=50)

import matplotlib.pyplot as plt
def my_plot_loss_acc(history):
    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(history.history['val_loss'], label='validation')
    ax1.plot(history.history['loss'], label='training')
    ax1.set_ylabel('loss')
    ax1.legend()
    ax2.plot(history.history['val_accuracy'])
    ax2.plot(history.history['accuracy'])
    ax2.set_xlabel('epoch')
    ax2.set_ylabel('accuracy')

my_plot_loss_acc(my_history)
plt.savefig('11-p-b-iris-1.pdf')

for k, v in my_history.history.items():
    print(f'{k}: {v[-1]}')

print(my_model.evaluate(x=X, y=y))

my_prob = my_model.predict(X)
print(my_prob[0:5])

import numpy as np
from math import log
print(np.mean([-log(my_prob[i, y[i]]) for i in range(len(y))]))

my_pred = my_model.predict_classes(X)
print(my_pred[0:5])

my_pred = np.argmax(my_model.predict(X), axis=-1)
print(my_pred[0:5])

print((my_pred == y).mean())
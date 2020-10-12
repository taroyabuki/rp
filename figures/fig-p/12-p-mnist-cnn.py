from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255
x_test  = x_test  / 255

import random
my_index = random.sample(range(60000), 6000)
x_train = x_train[my_index, :, :]
y_train = y_train[my_index]

x_train2d = x_train.reshape(-1, 28, 28, 1)
x_test2d = x_test.reshape(-1, 28, 28, 1)

from keras.models import Sequential
from keras.layers import *

my_model = Sequential()
my_model.add(Conv2D(filters=32, kernel_size=3,
                    activation='relu', input_shape=(28, 28, 1)))
my_model.add(MaxPooling2D(pool_size=2))
my_model.add(Flatten())
my_model.add(Dense(128, activation='relu'))
my_model.add(Dense(10, activation='softmax'))

my_model.compile(loss = 'sparse_categorical_crossentropy',
                 optimizer = 'rmsprop',
                 metrics = ['accuracy'])

from keras.callbacks import EarlyStopping
my_cb = [EarlyStopping(patience=5,                   # 訓練停止条件
                       restore_best_weights = True)] # 最善を保持

my_history = my_model.fit(
    x=x_train2d,          # 入力変数
    y=y_train,            # 出力変数
    validation_split=0.2, # 検証データの割合
    batch_size=128,       # バッチサイズ
    epochs=20,            # エポック数の上限
    callbacks=my_cb)      # エポックごとに行う処理

import matplotlib.pyplot as plt
import pandas as pd
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
tmp = my_history.history
pd.DataFrame({'validation':tmp['val_loss'],
              'training':tmp['loss']}
            ).plot(ax=ax1, ylabel='loss', style='o-')
pd.DataFrame({'valitation':tmp['val_accuracy'],
              'training':tmp['accuracy']}
            ).plot(ax=ax2, xlabel='epoch', ylabel='accuracy', legend=False, style='o-')
plt.savefig('12-p-mnist-cnn.pdf')

print(my_model.evaluate(x=x_test2d, y=y_test))

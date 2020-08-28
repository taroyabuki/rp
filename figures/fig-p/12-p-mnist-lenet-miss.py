from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255
x_test  = x_test  / 255

x_train2d = x_train.reshape(-1, 28, 28, 1)
x_test2d = x_test.reshape(-1, 28, 28, 1)

from keras.models import Sequential
from keras.layers import *

my_model = Sequential()
my_model.add(Conv2D(filters=20, kernel_size=5, activation='relu',
                    input_shape=(28, 28, 1)))
my_model.add(MaxPooling2D(pool_size=2, strides=2))
my_model.add(Conv2D(filters=20, kernel_size=5, activation='relu'))
my_model.add(MaxPooling2D(pool_size=2, strides=2))
my_model.add(Dropout(rate=0.25))
my_model.add(Flatten())
my_model.add(Dense(500, activation='relu'))
my_model.add(Dropout(rate=0.5))
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
    epochs=500,            # エポック数の上限
    callbacks=my_cb)      # エポックごとに行う処理

my_model.evaluate(x=x_test2d, y=y_test)

import numpy as np
import pandas as pd

my_prob = my_model.predict(x_test2d)                 # カテゴリに属する確率

tmp = pd.DataFrame({
    'prob': np.max(my_prob, axis=1),                 # 確率の最大値
    'pred': np.argmax(my_prob, axis=1),              # 予測カテゴリ
    'answer': y_test,                                # 正解
    'id': range(len(y_test))})                       # 番号

tmp = tmp[tmp.pred != tmp.answer]                    # 予測がはずれたものを残す
my_result = tmp.sort_values('prob', ascending=False) # 確率の大きい順に並び替える
my_result.head()

import matplotlib.pyplot as plt
for i in range(5):
    plt.subplot(1, 5, i + 1)
    id = my_result['id'].iloc[i]
    plt.imshow(x_test[id])
    plt.axis('off')

plt.savefig('12-p-mnist-lenet-miss.pdf')

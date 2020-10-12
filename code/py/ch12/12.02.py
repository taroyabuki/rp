from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train / 255
x_test  = x_test  / 255

import random
my_index = random.sample(range(60000), 6000)
x_train = x_train[my_index, :, :]
y_train = y_train[my_index]

x_train1d = x_train.reshape(len(x_train), 784)
x_test1d = x_test.reshape(len(x_test), 784)

from keras.models import Sequential
from keras.layers import Dense

my_model = Sequential()
my_model.add(Dense(units = 256, activation = "relu", input_dim = 784))
my_model.add(Dense(units = 10, activation = "softmax"))

my_model.compile(loss = 'sparse_categorical_crossentropy',
                 optimizer = 'rmsprop',
                 metrics = ['accuracy'])

from keras.callbacks import EarlyStopping
my_cb = [EarlyStopping(patience=5,                   # 訓練停止条件
                       restore_best_weights = True)] # 最善を保持

my_history = my_model.fit(
    x=x_train1d,          # 入力変数
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

my_prob = my_model.predict(x_test1d)
my_pred = np.argmax(my_prob, axis=-1)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, my_pred)
#> array([[ 961,    0,    1,    3,    0,    3,    9,    1,    1,    1],
#>        [   0, 1115,    3,    1,    1,    2,    5,    0,    8,    0],
#>        [  11,    2,  952,   17,    5,    3,    9,    9,   22,    2],
#>        [   2,    0,    6,  943,    1,   27,    1,    6,   16,    8],
#>        [   2,    1,    4,    1,  918,    0,   14,    1,    3,   38],
#>        [   5,    2,    0,   15,    2,  843,   11,    1,    7,    6],
#>        [  11,    3,    2,    1,    7,   13,  920,    0,    1,    0],
#>        [   2,   11,   19,   11,    1,    3,    0,  955,    2,   24],
#>        [   9,    2,    5,   22,    6,   18,   11,    7,  886,    8],
#>        [   9,    7,    3,   11,   19,    7,    1,    7,    7,  938]])

(y_test == my_pred).mean()
#> 0.9431

my_model.evaluate(x=x_test1d, y=y_test)
#> [0.19800357520580292,
#>  0.9430999755859375]


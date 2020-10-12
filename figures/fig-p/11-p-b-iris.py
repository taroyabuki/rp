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

from keras.callbacks import EarlyStopping
my_cb = [EarlyStopping(patience=20,                  # 訓練停止条件
                       restore_best_weights = True)] # 最善を保持

my_history = my_model.fit(
    x=X,                   # 入力変数
    y=y,                   # 出力変数
    validation_split=0.25, # 検証データの割合
    batch_size=20,         # バッチサイズ
    epochs=500,            # エポック数の上限
    callbacks=my_cb)       # エポックごとに行う処理

import matplotlib.pyplot as plt
import pandas as pd
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
tmp = my_history.history
pd.DataFrame({'validation':tmp['val_loss'],
              'training':tmp['loss']}
            ).plot(ax=ax1, ylabel='loss')
pd.DataFrame({'valitation':tmp['val_accuracy'],
              'training':tmp['accuracy']}
            ).plot(ax=ax2, xlabel='epoch', ylabel='accuracy', legend=False)
plt.savefig('11-p-b-iris.pdf')

{k: v[-1] for k, v in my_history.history.items()}

my_model.evaluate(x=X, y=y)

my_prob = my_model.predict(X)
my_prob[0:5]

import numpy as np
from math import log
np.mean([-log(my_prob[i, y[i]]) for i in range(len(y))])

my_pred = my_model.predict_classes(X)
my_pred[0:5]

my_pred = np.argmax(my_model.predict(X), axis=-1)
my_pred[0:5]

(my_pred == y).mean()
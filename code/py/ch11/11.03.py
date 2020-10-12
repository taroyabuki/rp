y = [2, 1, 0, 1] # 正解

import numpy as np

# 予測例A
p_A = np.array([[0.1, 0.1, 0.8],
                [0.1, 0.7, 0.2],
                [0.3, 0.4, 0.3],
                [0.1, 0.8, 0.1]])

# 予測例B
p_B = np.array([[0.1, 0.2, 0.7],
                [0.2, 0.6, 0.2],
                [0.2, 0.5, 0.3],
                [0.2, 0.7, 0.1]])

# 予測カテゴリA
y_A = np.argmax(p_A, axis=1)
y_A
#> array([2, 1, 1, 1])

# 予測カテゴリB
y_B = np.argmax(p_B, axis=1)
y_B
#> array([2, 1, 1, 1])

(y_A == y).mean() # 正解率A
#> 0.75

(y_B == y).mean() # 正解率B
#> 0.75

import pandas as pd
p = pd.get_dummies(y)
p
#>    0  1  2
#> 0  0  0  1
#> 1  0  1  0
#> 2  1  0  0
#> 3  0  1  0

p_A * p
#>      0    1    2
#> 0  0.0  0.0  0.8
#> 1  0.0  0.7  0.0
#> 2  0.3  0.0  0.0
#> 3  0.0  0.8  0.0

# 予測例Aの交差エントロピー
-np.mean(np.log(
    (p_A * p).apply(np.sum, axis=1)))
#> 0.5017337127232719

# 予測例Bの交差エントロピー
-np.mean(np.log(
    (p_B * p).apply(np.sum, axis=1)))
#> 0.708403356019389

from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.utils import shuffle
X, y = shuffle(X, y) # シャッフル

from sklearn.preprocessing import StandardScaler
my_scaler = StandardScaler()
X = my_scaler.fit_transform(X) # 標準化
# yはそのまま使う．

from keras.models import Sequential
from keras.layers import Dense

my_model = Sequential()
my_model.add(Dense(units=3, activation='relu', input_dim=4))
my_model.add(Dense(units=3, activation='softmax'))

my_model.compile(loss = 'sparse_categorical_crossentropy',
                 optimizer = 'rmsprop',
                 metrics = ['accuracy']) # 正解率を記録する．

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

{k: v[-1] for k, v in my_history.history.items()}
#> {'loss': 0.06126071885228157,
#>  'accuracy': 0.9910714030265808,
#>  'val_loss': 0.09569854289293289,
#>  'val_accuracy': 0.9210526347160339}

my_model.evaluate(x=X, y=y)
#> [0.0721130445599556,
#>  0.9733333587646484]

p_A = my_model.predict(X)
p_A[0:5]
#> array([[5.9782765e-12, 8.6652004e-04, 9.9913353e-01],
#>        [1.2191916e-02, 9.6308953e-01, 2.4718598e-02],
#>        [1.0000000e+00, 7.4585138e-10, 9.9767018e-12],
#>        [6.3189853e-10, 6.3192551e-03, 9.9368072e-01],
#>        [9.9999988e-01, 1.7056873e-07, 2.6229992e-09]], dtype=float32)

import numpy as np
# 予測カテゴリ
y_A = np.argmax(p_A, axis=1)

# 正解率（訓練）
(y_A == y).mean()
#> 0.9733333587646484

import pandas as pd
p = pd.get_dummies(y)

# 交差エントロピー（訓練）
-np.mean(np.log(
    (p_A * p).apply(np.sum, axis=1)))
#> 0.0721130445599556

from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
from sklearn.utils import shuffle
X, y = shuffle(X, y)

import pandas as pd
from sklearn.preprocessing import StandardScaler
my_scaler = StandardScaler()
X = my_scaler.fit_transform(X) # 標準化
p = pd.get_dummies(y)          # ワンホットエンコーディング
p.head()
#>    0  1  2
#> 0  0  1  0
#> 1  1  0  0
#> 2  0  1  0
#> 3  1  0  0
#> 4  1  0  0

from keras.models import Sequential
from keras.layers import Dense

my_model = Sequential()
my_model.add(Dense(units=3, activation='relu', input_dim=4))
my_model.add(Dense(units=3, activation='softmax'))

my_model.compile(loss = 'categorical_crossentropy', # 変更箇所
                 optimizer = 'rmsprop',
                 metrics = ['accuracy'])

from keras.callbacks import EarlyStopping
my_cb = [EarlyStopping(patience=20,                  # 訓練停止条件
                       restore_best_weights = True)] # 最善を保持

my_history = my_model.fit(
    x=X,                   # 入力変数
    y=p,                   # 出力変数
    validation_split=0.25, # 検証データの割合
    batch_size=20,         # バッチサイズ
    epochs=500,            # エポック数の上限
    callbacks=my_cb)       # エポックごとに行う処理

my_model.evaluate(x=X, y=p)
#> [0.10981836915016174,
#>  0.9599999785423279]

# 正解カテゴリ
import numpy as np
y = np.argmax(np.array(p), axis=1)

# 予測確率
p_A = my_model.predict(X)

# 予測カテゴリ
y_A = np.argmax(p_A, axis=1)

# 正解率（訓練）
(y_A == y).mean()
#> 0.96

# 交差エントロピー（訓練）
-np.mean(np.log(
    (p_A * p).apply(np.sum, axis=1)))
#> 0.10981837166945979


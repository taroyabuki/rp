import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/wine.csv'
tmp = pd.read_csv(my_url)
tmp.head()
#>    LPRICE2  WRAIN  DEGREES  HRAIN  TIME_SV
#> 0 -0.99868    600  17.1167    160       31
#> 1 -0.45440    690  16.7333     80       30
#> 2 -0.80796    502  17.1500    130       28
#> 3 -1.50926    420  16.1333    110       26
#> 4 -1.71655    582  16.4167    187       25

from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
my_data = scaler.fit_transform(shuffle(tmp)) # シャッフルと標準化
X = my_data[:, 1:5] # 入力変数
y = my_data[:, 0]   # 出力変数

from sklearn.linear_model import LinearRegression
my_model = LinearRegression() # 線形回帰分析

# 5分割交差検証（10回）
from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10)

# 交差検証の実行
my_scores = cross_val_score(my_model, X, y,
                            cv=my_cv,
                            n_jobs=-1,
                            scoring='neg_mean_squared_error') # -MSEを使う．
-my_scores.mean() # MSE（検証）
#> 0.2958079750627453

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping

my_model = Sequential()               # 層状のネットワーク
my_model.add(Dense(units=3,           # 隠れ層のニューロン数
                   activation='relu', # 活性化関数
                   input_dim=4))      # 入力層のニューロン数
my_model.add(Dense(units=1))          # 出力層のニューロン数

my_model.compile(loss='mean_squared_error',
                 optimizer='rmsprop')

my_cb = [EarlyStopping(patience=20,                  # 訓練停止条件
                       restore_best_weights = True)] # 最善を保持

my_history = my_model.fit(
    x=X,                   # 入力変数
    y=y,                   # 出力変数
    validation_split=0.25, # 検証データの割合
    batch_size=10,         # バッチサイズ
    epochs=500,            # エポック数の上限
    callbacks=my_cb)       # エポックごとに行う処理

import matplotlib.pyplot as plt
tmp = my_history.history
plt.plot(tmp['val_loss'], label='validation')
plt.plot(tmp['loss'], label='training')
plt.ylabel('loss')
plt.legend()

{k: v[-1] for k, v in my_history.history.items()}
#> {'loss': 0.1775408387184143, 'val_loss': 0.134183868765831}


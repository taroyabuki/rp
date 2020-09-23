import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/titanic.csv'
tmp = pd.read_csv(my_url)
tmp2 = pd.get_dummies(tmp, drop_first=True)
tmp2.head()
#>    Class_2nd  Class_3rd  Class_Crew  Sex_Male  Age_Child  Survived_Yes
#> 0          0          0           0         1          1             1
#> 1          0          0           0         1          1             1
#> 2          0          0           0         1          1             1
#> 3          0          0           0         1          1             1
#> 4          0          0           0         1          1             1

from sklearn.utils import shuffle
my_data = shuffle(tmp2) # シャッフル
X = my_data.iloc[:, 0:5] # 入力変数
y = my_data.iloc[:, 5]   # 出力変数

from keras.models import Sequential
from keras.layers import Dense

my_model = Sequential()
my_model.add(Dense(units=5, activation='relu', input_dim=5))
my_model.add(Dense(units=1, activation='sigmoid')) # 変更箇所1

my_model.compile(loss = 'binary_crossentropy', # 変更箇所2
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

my_model.evaluate(x=X, y=y)
#> [0.4836958348751068,
#>  0.7891867160797119]

# 予測確率
p_A = my_model.predict(X)[:, 0]

# 予測カテゴリ
y_A = p_A > 0.5

# 正解率（訓練）
(y_A == y).mean()
#> 0.7891867333030441

# 交差エントロピー（訓練）
import numpy as np
-np.mean(np.log(
    p_A * y + (1 - p_A) * (y != 1)))
#> 0.4836979806423187


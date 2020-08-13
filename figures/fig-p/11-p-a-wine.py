import numpy
numpy.random.seed(0)

import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/wine.csv'
tmp = pd.read_csv(my_url)

from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
my_data = scaler.fit_transform(shuffle(tmp)) # シャッフルと標準化

X = my_data[:, 1:5] # 入力変数
y = my_data[:, 0]   # 出力変数

from keras.models import Sequential
from keras.layers import Dense

my_model = Sequential()
my_model.add(Dense(units=3,
                   activation='relu',
                   input_dim=4))
my_model.add(Dense(units=1))

my_model.compile(loss='mean_squared_error',
                 optimizer='rmsprop')

my_history = my_model.fit(
  x=X,                   # 入力変数
  y=y,                   # 出力変数
  validation_split=0.25, # 検証データの割合
  batch_size=1,          # バッチサイズ
  epochs=50)             # エポック数の上限

import matplotlib.pyplot as plt
plt.plot(my_history.history['val_loss'], label='validation')
plt.plot(my_history.history['loss'], label='training')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.savefig('11-p-a-wine.pdf')

for k, v in my_history.history.items():
    print(f'{k}: {v[-1]}')
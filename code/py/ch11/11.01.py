## 11.1 Kerasによる回帰

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from keras import activations, callbacks, layers, models
from sklearn.preprocessing import StandardScaler

my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
tmp = pd.read_csv(my_url)

## 11.1 Kerasによる回帰

my_data = sklearn.utils.shuffle(tmp)

## 11.1 Kerasによる回帰

my_scaler = StandardScaler()
X = my_scaler.fit_transform(
    my_data.drop(columns=['LPRICE2']))
y = my_data['LPRICE2']

## 11.1 Kerasによる回帰

x = np.linspace(-3, 3, 100)
plt.plot(x, activations.relu(x))
plt.xlabel('x')
plt.ylabel('ReLU(x)')

## 11.1 Kerasによる回帰

my_model = models.Sequential()
my_model.add(layers.Dense(units=3, activation='relu', input_shape=[4]))
my_model.add(layers.Dense(units=1))

my_model.summary() # ネットワークの概要
#> Model: "sequential"
#> _________________________________________________________________
#> Layer (type)                 Output Shape              Param #   
#> =================================================================
#> dense (Dense)                (None, 3)                 15        
#> _________________________________________________________________
#> dense_1 (Dense)              (None, 1)                 4         
#> =================================================================
#> Total params: 19
#> Trainable params: 19
#> Non-trainable params: 0

## 11.1 Kerasによる回帰

my_model.compile(
    loss='mse',
    optimizer='rmsprop')

## 11.1 Kerasによる回帰

my_cb = callbacks.EarlyStopping(
    patience=20,
    restore_best_weights = True)

## 11.1 Kerasによる回帰

my_history = my_model.fit(
    x=X,
    y=y,
    validation_split=0.25,
    batch_size=10,
    epochs=500,
    callbacks=[my_cb],
    verbose=0)

## 11.1 Kerasによる回帰

tmp = pd.DataFrame(my_history.history)
tmp.plot(xlabel='epoch')

## 11.1 Kerasによる回帰

tmp.iloc[-1, ]
#> loss        0.058252
#> val_loss    0.085878
#> Name: 499, dtype: float64


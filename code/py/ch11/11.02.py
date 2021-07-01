## 11.2 Kerasによる分類

import numpy as np
import pandas as pd
import sklearn
import statsmodels.api as sm
from keras import callbacks, layers, losses, models
from sklearn.preprocessing import StandardScaler, LabelEncoder

tmp = sm.datasets.get_rdataset('iris', 'datasets').data
my_data = sklearn.utils.shuffle(tmp)

## 11.2 Kerasによる分類

my_scaler = StandardScaler()
X = my_scaler.fit_transform(
    my_data.drop(columns=['Species']))
my_enc = LabelEncoder()
y = my_enc.fit_transform(
    my_data['Species'])

## 11.2 Kerasによる分類

my_model = models.Sequential()
my_model.add(layers.Dense(units=3, activation='relu', input_shape=[4]))
my_model.add(layers.Dense(units=3, activation='softmax'))

## 11.2 Kerasによる分類

my_model.compile(loss='sparse_categorical_crossentropy',
                 optimizer='rmsprop',
                 metrics=['accuracy'])

## 11.2 Kerasによる分類

my_cb = callbacks.EarlyStopping(
    patience=20,
    restore_best_weights = True)

my_history = my_model.fit(
    x=X,
    y=y,
    validation_split=0.25,
    batch_size=10,
    epochs=500,
    callbacks=[my_cb],
    verbose = 0)

tmp = pd.DataFrame(my_history.history)
tmp.plot(xlabel='epoch')

## 11.2 Kerasによる分類

tmp.iloc[-1, ]
#> loss            0.057278
#> accuracy        0.991071
#> val_loss        0.100445
#> val_accuracy    0.947368

### 11.2.1 交差エントロピー

-np.log([0.8, 0.7, 0.3, 0.8]).mean()
#> 0.5017337127232719

-np.log([0.7, 0.6, 0.2, 0.7]).mean()
#> 0.708403356019389

### 11.2.1 交差エントロピー

y = [2, 1, 0, 1]
y_1 = [[0.1, 0.1, 0.8],
       [0.1, 0.7, 0.2],
       [0.3, 0.4, 0.3],
       [0.1, 0.8, 0.1]]
y_2 = [[0.1, 0.2, 0.7],
       [0.2, 0.6, 0.2],
       [0.2, 0.5, 0.3],
       [0.2, 0.7, 0.1]]

### 11.2.1 交差エントロピー

[losses.sparse_categorical_crossentropy(y_true=y, y_pred=y_1).numpy().mean(),
 losses.sparse_categorical_crossentropy(y_true=y, y_pred=y_2).numpy().mean()]
#> [0.5017337, 0.70840335]


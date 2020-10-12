import pandas as pd
my_data = pd.read_csv('an_wld_en.csv')
my_data.index = pd.to_datetime(my_data['year'], format='%Y')

my_train = my_data[:109] # 訓練データ
my_test  = my_data[-20:] # 検証データ

import matplotlib.pyplot as plt
plt.plot(my_train[['world']], label='train')
plt.plot(my_test[['world']], label='test')
plt.legend()

from sklearn.linear_model import LinearRegression
X_train, y_train = my_train[['year']], my_train['world']
my_lm_model = LinearRegression().fit(X_train, y_train)

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
y_ = my_lm_model.predict(X_train)
[np.sqrt(mean_squared_error(y_train, y_)), # RMSE
 r2_score(y_true=y_train, y_pred=y_),      # 決定係数（その1）
 my_lm_model.score(X_train, y_train)]      # 決定係数（その2）
#> [0.11727053954998497, 0.73458474420936, 0.73458474420936]

X_test, y_test = my_test[['year']], my_test['world']
y_ = my_lm_model.predict(X_test)
[np.sqrt(mean_squared_error(y_test, y_)), # RMSE
 r2_score(y_true=y_test, y_pred=y_),      # 決定係数（その1）
 my_lm_model.score(X_test, y_test)]       # 決定係数（その2）
#> [0.22055093276762147, -2.054535483738701, -2.054535483738701]

from pmdarima import auto_arima
my_arima_model = auto_arima(y_train)    # モデルの作成
#my_arima_model.summary()               # モデルの確認と診断1（割愛）
#my_arima_model.plot_diagnostics()      # モデルの確認と診断2（割愛）

y_ = my_arima_model.predict(20)         # 20年分の予測
np.sqrt(mean_squared_error(y, y_))      # RMSEの計算
#> 0.16406012856510532

my_model = auto_arima(my_data['world']) # すべてのデータを使う．
y_, my_ci = my_model.predict(30,                   # 30年分の予測
                             return_conf_int=True) # 信頼区間を求める．

from datetime import datetime
my_df = pd.DataFrame({'world': y_,
                      'Lo': my_ci[:, 0],
                      'Hi': my_ci[:, 1]})
my_df.index=pd.date_range('2020-01-01', '2049-01-01', freq='AS')
my_df.head()
#>                world        Lo        Hi
#> 2020-01-01  0.411209  0.223448  0.598969
#> 2021-01-01  0.383494  0.157460  0.609529
#> 2022-01-01  0.380250  0.145498  0.615002
#> 2023-01-01  0.398964  0.159492  0.638436
#> 2024-01-01  0.397272  0.149843  0.644700

import matplotlib.pyplot as plt
plt.plot(my_data['world'])
plt.plot(my_df['world'])
plt.fill_between(my_df.index,
                 my_df.Lo,
                 my_df.Hi,
                 color='k',
                 alpha=0.25)

import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/tokyo-max-temp-2015--2019.csv'
my_data = pd.read_csv(my_url,
                      encoding='sjis',
                      skiprows=5,
                      names=['month', 'tokyo', 'quality', 'no'])
my_data.head()
#>     month  tokyo  quality  no
#> 0  2015/1   10.4        8   1
#> 1  2015/2   10.4        8   1
#> 2  2015/3   15.5        8   1
#> 3  2015/4   19.3        8   1
#> 4  2015/5   26.4        8   1

my_data.index = pd.to_datetime(my_data['month'], format='%Y/%m')
my_data.head()
#>              month  tokyo  quality  no
#> month
#> 2015-01-01  2015/1   10.4        8   1
#> 2015-02-01  2015/2   10.4        8   1
#> 2015-03-01  2015/3   15.5        8   1
#> 2015-04-01  2015/4   19.3        8   1
#> 2015-05-01  2015/5   26.4        8   1

from pmdarima import auto_arima
my_model = auto_arima(my_data['tokyo'])

my_pred, my_ci = my_model.predict(24,
                                  return_conf_int=True)
my_df = pd.DataFrame({'tokyo': my_pred,
                      'Lo': my_ci[:, 0],
                      'Hi': my_ci[:, 1]})
my_df.index=pd.date_range('2020-01-01', '2021-12-01', freq='MS')
my_df.head()
#>                 tokyo         Lo         Hi
#> 2020-01-01  10.100906   7.170399  13.031412
#> 2020-02-01  10.287664   7.266074  13.309253
#> 2020-03-01  13.242980  10.216923  16.269037
#> 2020-04-01  18.169809  14.977157  21.362461
#> 2020-05-01  23.755596  20.185964  27.325228

import matplotlib.pyplot as plt
plt.plot(my_data['tokyo'])
plt.plot(my_df['tokyo'])
plt.fill_between(my_df.index,
                 my_df.Lo,
                 my_df.Hi,
                 color='k',
                 alpha=0.25)


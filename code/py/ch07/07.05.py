### 7.5.2 Pythonの場合

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

from sklearn.linear_model import LinearRegression
my_model = LinearRegression()
my_model.fit(X, y)

my_test = pd.DataFrame({'speed':[21.5]})
my_model.predict(my_test)
#> array([66.96769343])

y_ = my_model.predict(X) # 訓練データに対する予測
my_data.assign(model=y_).plot(x='speed', style=['o', '-'])

import pandas as pd
import numpy as np
# モデル可視化用のデータフレームを作る．
my_min, my_max = my_data['speed'].min(), my_data['speed'].max()
tmp = pd.DataFrame({'speed':np.linspace(my_min, my_max, num=100)})
y_ = my_model.predict(tmp)  # 予測し，
tmp2 = tmp.assign(model=y_) # 結果をデータフレームに加える．

tmp3 = pd.concat([my_data, tmp2])      # 訓練データとモデル可視化用データフレームを連結し，
tmp3.plot(x='speed', style=['o', '-']) # 可視化する．
# （先と同じ結果のため割愛）


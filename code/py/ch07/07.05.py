### 7.5.2 Pythonの場合

from sklearn.linear_model import LinearRegression
my_model = LinearRegression()

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']
my_model.fit(X, y)

import pandas as pd
my_test = pd.DataFrame({'speed':[21.5]})

my_model.predict(my_test)
#> array([66.96769343])

import numpy as np
my_min, my_max = my_data['speed'].min(), my_data['speed'].max()
tmp = pd.DataFrame({'speed':np.linspace(my_min, my_max, num=100)})

tmp['model'] = my_model.predict(tmp)                        # 予測
pd.concat([my_data, tmp]).plot(x='speed', style=['o', '-']) # 描画

y_ = my_model.predict(X) # 訓練データに対する予測
my_data.assign(model=y_).plot(x='speed', style=['o', '-']) # 結果は割愛


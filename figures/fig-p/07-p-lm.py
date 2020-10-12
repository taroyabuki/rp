from sklearn.linear_model import LinearRegression
my_model = LinearRegression()

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']
my_model.fit(X, y)

import pandas as pd
import numpy as np
# モデル可視化用のデータフレームを作る．
my_min, my_max = my_data['speed'].min(), my_data['speed'].max()
tmp = pd.DataFrame({'speed':np.linspace(my_min, my_max, num=100)})

tmp['model'] = my_model.predict(tmp)                        # 予測
pd.concat([my_data, tmp]).plot(x='speed', style=['o', '-']) # 描画

import matplotlib.pyplot as plt
plt.savefig('07-p-lm.pdf')
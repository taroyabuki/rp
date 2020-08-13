import matplotlib.pyplot as plt

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
#　speedがリストになっている点，解説が必要そう．
my_result = lr.fit(my_data[['speed']], my_data['dist'])

import numpy as np # 矢吹が補いました．
import matplotlib.pyplot as plt

# 訓練に使ったデータと訓練で得られたモデルを一緒に可視化します．
tmp = np.linspace(my_data['speed'].min(), my_data['speed'].max(), num=100)
# 1次元なので，配列の配列にするために変換
y_ = my_result.predict(tmp[:, np.newaxis])
# 以下でも良いが，https://scipy-lectures.org/　を見ると，newaxisの方が自然か？確信はないです．
# y_ = my_result.predict(tmp.reshape((-1, 1))) # reshape(-1, 1)でもOK

plt.scatter(my_data['speed'], my_data['dist'], c='c', label='my_data')
plt.plot(tmp, y_, c='k', label='model')
plt.xlabel('speed')
plt.ylabel('dist')
plt.legend()
plt.savefig('07-p-lm.pdf')
import matplotlib.pyplot as plt

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data

from sklearn.neighbors import KNeighborsRegressor
my_knr = KNeighborsRegressor() #n_neighbors=5)
my_knr.fit(my_data[['speed']] , my_data['dist'])

import numpy as np # 矢吹が補いました．
# pltとfig,axのスタイルの違いを，最初にmatplotlibを紹介するところで書きましょう．ここは，pltで．
# fig, ax = plt.subplots()
tmp = np.linspace(my_data['speed'].min(), my_data['speed'].max(), num=100)
y_ = my_knr.predict(tmp[:, np.newaxis])

plt.scatter(my_data['speed'], my_data['dist'], c='c', label='training')
plt.plot(tmp, y_, c='k', label='prediction')
plt.xlabel('speed')
plt.ylabel('dist')
plt.legend()
plt.savefig('07-p-knn.pdf')
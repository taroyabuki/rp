import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

from sklearn.neighbors import KNeighborsRegressor
my_model = KNeighborsRegressor() # (n_neighbors=5)
my_model.fit(X, y)

import pandas as pd
import numpy as np
# モデル可視化用のデータフレームを作る．
my_min, my_max = my_data['speed'].min(), my_data['speed'].max()
tmp = pd.DataFrame({'speed':np.linspace(my_min, my_max, num=100)})
tmp['model'] = my_model.predict(tmp) # 予測結果の列を加える．

pd.concat([my_data, tmp]).plot(x='speed', style=['o', '-']) # まとめて描画する．
import matplotlib.pyplot as plt
plt.savefig('07-p-knn.pdf')
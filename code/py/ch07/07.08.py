### 7.8.2 Pythonの場合

from sklearn.neighbors import KNeighborsRegressor
my_model = KNeighborsRegressor()

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']
my_model.fit(X, y)

y_ = my_model.predict(X)
((y_ - y) ** 2).mean() ** 0.5
#> 13.087184571174962

import pandas as pd
import numpy as np
my_min, my_max = my_data['speed'].min(), my_data['speed'].max()
tmp = pd.DataFrame({'speed':np.linspace(my_min, my_max, num=100)})
tmp['model'] = my_model.predict(tmp)
pd.concat([my_data, tmp]).plot(x='speed', style=['o', '-'])


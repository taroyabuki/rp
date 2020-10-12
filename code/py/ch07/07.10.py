import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2, 2, 0.1)
y = 1.0 / (1 + np.exp(-x))
plt.plot(x, y)

### 7.10.2 Pythonの場合

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
my_model = Pipeline([('sc', StandardScaler()), ('mlp', MLPRegressor())])
my_model.set_params(mlp__max_iter=1000)

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']
my_model.fit(X, y)

import pandas as pd
import numpy as np
my_min, my_max = my_data['speed'].min(), my_data['speed'].max()
tmp = pd.DataFrame({'speed':np.linspace(my_min, my_max, num=100)})
tmp['model'] = my_model.predict(tmp)
pd.concat([my_data, tmp]).plot(x='speed', style=['o', '-'])


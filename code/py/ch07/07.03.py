import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

# モデルの指定
from sklearn.linear_model import LinearRegression
my_model = LinearRegression()

# モデルをデータにフィットさせる．
my_model.fit(X, y)

# まとめて実行してもよい．
# my_model = LinearRegression().fit(X, y)

[my_model.intercept_, my_model.coef_]
#> -17.579094890510973 [3.93240876]

import pandas as pd
tmp = [[21.5]]
my_model.predict(tmp)
#> array([66.96769343])

import numpy as np
tmp = pd.DataFrame({'speed':np.linspace(min(my_data.speed),
                                        max(my_data.speed),
                                        100)})
tmp['model'] = my_model.predict(tmp)

pd.concat([my_data, tmp]).plot(
  x='speed', style=['o', '-'])


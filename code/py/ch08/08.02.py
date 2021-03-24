import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, LeaveOneOut

my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)
X, y = my_data.drop(columns=['LPRICE2']), my_data['LPRICE2']

my_model = LinearRegression().fit(X, y)

[my_model.intercept_, my_model.coef_]
#> [-12.145333576510417,  # (Intercept)
#>  array([ 0.00116678,   # WRAIN
#>          0.61639244,   # DEGREES
#>         -0.00386055,   # HRAIN
#>          0.02384741])] # TIME_SV

my_test = [[500, 17, 120, 2]]
my_model.predict(my_test)
#> array([-1.49884253])

y_ = my_model.predict(X)

mean_squared_error(y_, y)**0.5
#> 0.2586166620130621 # RMSE（訓練）

my_model.score(X, y)
#> 0.8275277990052154 # 決定係数1

import numpy as np
np.corrcoef(y, y_)[0, 1]**2
#> 0.8275277990052158 # 決定係数6

my_scores = cross_val_score(my_model, X, y,
                            cv=LeaveOneOut(),
                            scoring='neg_mean_squared_error')
(-my_scores.mean())**0.5
#> 0.32300426518411957 # RMSE（検証）

import numpy as np
M = np.matrix(X.assign(b0=1))
np.linalg.solve(M.T @ M, M.T @ y)
#> array([ 1.16678230e-03,  # WRAIN
#>         6.16392441e-01,  # DEGREES
#>        -3.86055357e-03,  # HRAIN
#>         2.38474129e-02,  # TIME_SV
#>        -1.21453336e+01]) # b0


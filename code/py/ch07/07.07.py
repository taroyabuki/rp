import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.neighbors import KNeighborsRegressor

my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

my_params = {'n_neighbors':range(1, 16)} # 探索範囲（1以上15以下の整数）

my_search = GridSearchCV(estimator=KNeighborsRegressor(),
                         param_grid=my_params,
                         cv=LeaveOneOut(),
                         scoring='neg_mean_squared_error')
my_search.fit(X, y)

tmp = my_search.cv_results_
my_df = pd.DataFrame(
    {'n_neighbors':
     my_params['n_neighbors'],
     'validation':
     (-tmp['mean_test_score'])**0.5})
my_df.plot(x='n_neighbors',
           style='o-',
           ylabel='RMSE')

my_search.best_params_
#> {'n_neighbors': 5}

(-my_search.best_score_)**0.5
#> 16.07308308943869

my_model = my_search.best_estimator_
y_ = my_model.predict(X)
mean_squared_error(y_, y)**0.5
#> 13.087184571174962

import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.neighbors import KNeighborsRegressor

my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

my_params = {'n_neighbors':range(1, 16)} # 探索範囲（1以上15以下の整数）

my_search = GridSearchCV(estimator=KNeighborsRegressor(),
                         param_grid=my_params,
                         cv=LeaveOneOut(),
                         scoring='neg_mean_squared_error',
                         return_train_score=True)
my_search.fit(X, y)

tmp = my_search.cv_results_
my_df = pd.DataFrame(
    {'n_neighbors':
     my_params['n_neighbors'],
     'validation':
     (-tmp['mean_test_score'])**0.5,
     'training':
     (-tmp['mean_train_score'])**0.5})
my_df.plot(x='n_neighbors',
           style='o-',
           ylabel='RMSE')


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data[['dist']]

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10) # 5分割交差検証（10回）

def f(x):
    my_model = LinearRegression()
    X_poly = PolynomialFeatures(x).fit_transform(X)
    my_scores =  cross_validate(my_model, X_poly, y, cv=my_cv, n_jobs=-1,
                                return_train_score=True) # 決定係数（訓練）も返す．
    my_train = my_scores['train_score']
    my_test = my_scores['test_score']
    s = np.sqrt(len(my_train))
    return pd.Series([x,
                      my_train.mean(), my_train.std() / s,
                      my_test.mean(),  my_test.std()  / s],
                     index=['degree',
                            'mean_train_score', 'std_error_train',
                            'mean_test_score',  'std_error_test'])

my_x = range(1, 7)
my_results = pd.Series(my_x).apply(f)
my_results
#>    degree  mean_train_score  std_error_train  mean_test_score  std_error_test
#> 0     1.0          0.650336         0.005173         0.486990        0.048597
#> 1     2.0          0.668367         0.005871         0.508901        0.034347
#> 2     3.0          0.675553         0.005857         0.498946        0.037529
#> 3     4.0          0.687773         0.005565         0.443572        0.088367
#> 4     5.0          0.692880         0.005051         0.473242        0.043312
#> 5     6.0          0.697218         0.005812        -0.500109        0.644328

my_df = pd.DataFrame({
    'x':my_x,
    'train':my_results['mean_train_score'],
    'validation':my_results['mean_test_score']})

my_errors = pd.DataFrame({
    'x':my_x,
    'train':my_results['std_error_train'],
    'validation':my_results['std_error_test']}).set_index('x')

import matplotlib.pyplot as plt
my_df.plot(x='x', yerr=my_errors)
plt.ylabel('R^2')
plt.xlabel('degree')


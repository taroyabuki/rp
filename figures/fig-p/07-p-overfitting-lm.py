import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data[['dist']]

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10) # K分割交差検証（10回）

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def f(x):
    my_model = LinearRegression()
    X_poly = PolynomialFeatures(x).fit_transform(X)
    my_scores =  cross_validate(my_model, X_poly, y, cv=my_cv, return_train_score=True, n_jobs=-1)
    my_train = my_scores['train_score']
    my_test = my_scores['test_score']
    s = np.sqrt(len(my_train))
    return pd.Series([x, my_train.mean(), my_train.std() / s, my_test.mean(), my_test.std() / s],
                     index=['degree', 'mean_train_score', 'std_error_train', 'mean_test_score', 'std_error_test'])

my_x = range(1, 7)
my_results = pd.Series(my_x).apply(f)
print(my_results)

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

plt.savefig('07-p-overfitting-lm.pdf')
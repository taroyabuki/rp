import matplotlib.pyplot as plt

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import RepeatedKFold

my_knr = KNeighborsRegressor()
params = {'n_neighbors': list(range(1,16))}
rkf = RepeatedKFold(n_splits=5, n_repeats=20)
clf = GridSearchCV(my_knr, params, cv=rkf, scoring='neg_mean_squared_error', return_train_score=True)

clf.fit(my_data[['speed']], my_data['dist'])

import numpy as np
rmse = np.sqrt(-clf.cv_results_['mean_test_score'])
plt.plot(range(1, 16), rmse)
plt.xlabel('k')
plt.ylabel('rmse')
plt.savefig('07-p-tuning.pdf')
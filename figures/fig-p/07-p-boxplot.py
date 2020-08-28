import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data[['dist']]

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=5) # K分割交差検証（5回）

# 線形単回帰分析
from sklearn.linear_model import LinearRegression
my_lm_model = LinearRegression()
my_lm_scores = cross_val_score(my_lm_model, X, y, cv=my_cv)
print(my_lm_scores.mean())

# K最近傍法
from sklearn.neighbors import KNeighborsRegressor
my_knn_model = KNeighborsRegressor()
my_knn_scores = cross_val_score(my_knn_model, X, y, cv=my_cv)
print(my_knn_scores.mean())

import pandas as pd
my_df = pd.DataFrame({'lm': my_lm_scores, 'knn': my_knn_scores})
print(my_df.head())

my_df.boxplot()
import matplotlib.pyplot as plt
plt.savefig('07-p-boxplot.pdf')

from scipy import stats
print(stats.mannwhitneyu(my_lm_scores, my_knn_scores, alternative='two-sided'))
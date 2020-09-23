### 7.11.2 Pythonの場合

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate

# from sklearn.metrics import mean_squared_error

lr = LinearRegression()
scores = cross_validate(lr, my_data[['speed']], my_data['dist'], cv=5,
                        scoring = 'neg_mean_squared_error',
                        return_train_score=True)

scores
#> {'fit_time': array([0.00793219, 0.00227952, 0.00231218, 0.00296402, 0.00247073]),
#>  'score_time': array([0.0033319 , 0.00127578, 0.00138569, 0.00131702, 0.00129986]),
#>  'test_score': array([-110.30459822, -82.56632671, -379.09442919, -337.67126901, -419.62462927]),
#>  'train_score': array([-264.33903892, -264.72197576, -189.41831029, -200.41976329, -201.86693026])}

np.mean(np.sqrt(-scores['test_score']))
#> 15.58402474583013

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data[['dist']]

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=5) # K分割交差検証（5回）

# 線形単回帰分析
from sklearn.linear_model import LinearRegression
my_lm_model = LinearRegression()
my_lm_scores = cross_val_score(my_lm_model, X, y, cv=my_cv)
my_lm_scores.mean()
#> 0.5873534834160824

# K最近傍法
from sklearn.neighbors import KNeighborsRegressor
my_knn_model = KNeighborsRegressor()
my_knn_scores = cross_val_score(my_knn_model, X, y, cv=my_cv)
my_knn_scores.mean()
#> 0.4999752343319323

my_df = pd.DataFrame({'lm': my_lm_scores, 'knn': my_knn_scores})
my_df.head()
#>          lm       knn
#> 0  0.809073  0.581115
#> 1  0.803353  0.583306
#> 2  0.652358  0.478726
#> 3  0.317201  0.676515
#> 4  0.540462  0.564383

my_df.boxplot()

from scipy import stats
stats.mannwhitneyu(my_lm_scores, my_knn_scores, alternative='two-sided')
#> MannwhitneyuResult(statistic=327.0, pvalue=0.7858989168050492)


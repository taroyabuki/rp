### 7.11.2 Pythonの場合

from sklearn.model_selection import *
my_cv = KFold(5) # 5分割交差検証

from sklearn.linear_model import LinearRegression
my_model = LinearRegression()

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

my_score = cross_validate(my_model, X, y,
                          cv=my_cv,
                          return_train_score=True)

my_score
#> {'fit_time': array([0.00233173, 0.0016377 , 0.01008534, 0.00153947, 0.0017395 ]),
#>  'score_time': array([0.00134301, 0.00132465, 0.0011909 , 0.00202823, 0.00120544]),
#>  'test_score': array([-0.25789256, -0.21421069, -0.30902773, -0.27346232,  0.02312918]),
#>  'train_score': array([0.52996992, 0.63554457, 0.74429689, 0.71795674, 0.47109477])}

my_score['test_score'].mean()
#> -0.20629282165364665

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data[['dist']]

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=5) # 5分割交差検証（5回）

# 線形単回帰分析
from sklearn.linear_model import LinearRegression
my_lm_model = LinearRegression()
my_lm_score = cross_val_score(my_lm_model, X, y, cv=my_cv)
my_lm_score.mean()
#> 0.5873534834160824

# K最近傍法
from sklearn.neighbors import KNeighborsRegressor
my_knn_model = KNeighborsRegressor()
my_knn_score = cross_val_score(my_knn_model, X, y, cv=my_cv)
my_knn_score.mean()
#> 0.4999752343319323

my_df = pd.DataFrame({'lm': my_lm_score, 'knn': my_knn_score})
my_df.head()
#>          lm       knn
#> 0  0.809073  0.581115
#> 1  0.803353  0.583306
#> 2  0.652358  0.478726
#> 3  0.317201  0.676515
#> 4  0.540462  0.564383

my_df.boxplot()

from scipy import stats
stats.mannwhitneyu(my_lm_score, my_knn_score, alternative='two-sided')
#> MannwhitneyuResult(statistic=327.0, pvalue=0.7858989168050492)


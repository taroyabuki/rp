import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

for c in range(4):
    X.iloc[:, c] = [np.nan if np.random.random() < 0.1 else x for x in X.iloc[:, c]]

X.describe()
#>        Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
#> count    134.000000   144.000000    136.000000   128.000000
#> 以下略

import xgboost
my_model = xgboost.XGBClassifier()

# 5分割交差検証（10回）
from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10)

my_scores = cross_val_score(my_model, X, y, cv=my_cv)
my_scores.mean() # 正解率（検証）
#> 0.9513333333333334


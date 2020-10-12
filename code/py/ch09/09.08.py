### 9.8.2 Pythonの場合

from sklearn.ensemble import RandomForestClassifier
my_model = RandomForestClassifier()

# データの読み込み
import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

# 5分割交差検証（10回）
from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10)

# 交差検証の実行
my_scores = cross_val_score(my_model, X, y, cv=my_cv)
my_scores.mean() # 正解率（検証）
#> 0.9560000000000001

import xgboost
my_model = xgboost.XGBClassifier()

# 割愛（データの読み込み，交差検証の設定と実行）
my_scores.mean() # 正解率（検証）
#> 0.9486666666666665


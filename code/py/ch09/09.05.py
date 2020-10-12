### 9.5.2 Pythonの場合

from sklearn.neighbors import KNeighborsClassifier
my_model = KNeighborsClassifier()

# チューニングの設定（1以上21未満のKを調べる．）
params = {'n_neighbors': list(range(1,21))}

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

# 5分割交差検証（10回）
from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10)

# パラメータチューニングの設定
my_search = GridSearchCV(my_model,
                         params,
                         cv=my_cv,
                         return_train_score=True) # 正解率（訓練）の保存

# 訓練（チューニング）
my_search.fit(X, y)

my_search.best_params_ # 最良パラメータ
#> {'n_neighbors': 9}

my_search.best_score_ # 正解率（検証）
#> 0.968

import pandas as pd
my_result = my_search.cv_results_
my_df = pd.DataFrame({'k':range(1,21),
                      'train':my_result['mean_train_score'],
                      'test':my_result['mean_test_score']})
my_df.plot(x='k', ylabel='Accuracy', style='o-')


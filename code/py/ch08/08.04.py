#### 8.4.2.2 Pythonの場合

from sklearn.linear_model import ElasticNet
my_model = ElasticNet()

# チューニングの設定
import numpy as np
params = {'l1_ratio': np.arange(0, 0.001, 0.0001),
          'alpha': np.arange(0.01, 0.2, 0.01)}

import pandas as pd
tmp = pd.read_csv('wine.csv')
X, y = tmp.iloc[:, 1:5], tmp.LPRICE2

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=25) # 5分割交差検証（10回）

import os
my_model = GridSearchCV(my_model,
                        params,
                        cv=my_cv,
                        return_train_score=True, # 訓練正解率の保存
                        n_jobs=os.cpu_count())   # 並列処理
my_model.fit(X, y) # 訓練

my_model.best_params_ # 最良パラメータ
#> {'alpha': 0.02, 'l1_ratio': 0.0}

my_model.best_score_ # 決定係数（検証）
#> 0.5672976659881529

my_model.best_estimator_.coef_ # 係数
#> array([ 0.00110609,  0.5817578 , -0.00390292,  0.02462978])

my_model.best_estimator_.intercept_ # 定数
#> -11.544234226243098


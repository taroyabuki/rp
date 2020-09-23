### 8.2.2 Pythonの場合

from sklearn.linear_model import LinearRegression
my_model = LinearRegression()

import pandas as pd
tmp = pd.read_csv('wine.csv') # 8.1節で作成したwine.csvを使う．
#my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/wine.csv'
#tmp = pd.read_csv(my_url)
X, y = tmp.iloc[:, 1:5], tmp.LPRICE2
my_model.fit(X, y) # 訓練

my_model.coef_ # 係数
#> array([ 0.00116678,  0.61639244, -0.00386055,  0.02384741])

my_model.intercept_ # 定数
#> -12.145333576510417

my_test = pd.DataFrame([[500, 17, 120, 2]],
                       columns=['WRAIN', 'DEGREES', 'HRAIN', 'TIME_SV'])
my_model.predict(my_test)
#> array([-1.49884253])

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10) # 5分割交差検証（10回）

import os
my_scores = cross_val_score(my_model, X, y, cv=my_cv, n_jobs=os.cpu_count())
my_scores.mean() # 決定係数（検証）
#> 0.5178759794549234

import pandas as pd
tmp = pd.read_csv('wine.csv') # 8.1節で作成したwine.csvを使う．
#my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/wine.csv'
#tmp = pd.read_csv(my_url)

import numpy as np
tmp['b'] = [1] * len(tmp)       # すべて1の列を追加して，
A = np.matrix(tmp.iloc[:, 1:6]) # 1から5列目を行列にする．
y = tmp['LPRICE2']
np.linalg.solve(A.T @ A, A.T @ y) # AT A = AT yを解く（ATはAの転置行列）
#> array([ 1.16678230e-03,  6.16392441e-01, -3.86055357e-03,  2.38474129e-02,
#>        -1.21453336e+01])


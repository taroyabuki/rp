# データの準備
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, RepeatedKFold
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

# モデルの指定
my_model = LinearRegression()

# 検証（5分割交差検証）
my_scores = cross_val_score(my_model, X, y)

# 5個の決定係数1を得る．
my_scores
#> array([-0.25789256, -0.21421069, -0.30902773, -0.27346232,  0.02312918])

# 平均を決定係数1（検証）とする．
my_scores.mean()
#> -0.20629282165364665

-cross_val_score(my_model, X, y, scoring='neg_root_mean_squared_error').mean()
#> 15.58402474583013 # RMSE（検証）

import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import make_scorer, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, RepeatedKFold

my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']
my_model = LinearRegression().fit(X, y)
y_ = my_model.predict(X)

# RMSE（訓練）
mean_squared_error(y, y_)**0.5
# あるいは
((y_ - y)**2).mean()**0.5
#> 15.068855995791381

# 決定係数1（訓練）
my_model.score(X, y)
# あるいは
r2_score(y_true=y, y_pred=y_)
#> 0.6510793807582509

# 決定係数6（訓練）
np.corrcoef(y, y_)[0, 1]**2
#> 0.6510793807582511

my_scores = cross_val_score(
    my_model, X, y, cv=RepeatedKFold(),
    scoring='neg_root_mean_squared_error')
my_scores.mean()
#> 15.301860331378464 # RMSE（検証）

my_scores = cross_val_score(my_model, X, y, cv=RepeatedKFold())
my_scores.mean()
#> 0.49061365458235245 # 決定係数1（検証）

my_scores = cross_val_score(my_model, X, y, cv=RepeatedKFold(),
                            scoring=make_scorer(my_r2_6))
my_scores.mean()
#> 0.6417227070606119 # 決定係数6（検証）

# 決定係数6（検証）を求める関数
def my_r2_6(y_true, y_pred):
    return ((np.corrcoef(y_true, y_pred)[0, 1]**2)).mean()

cross_val_score(my_model, X, y, cv=RepeatedKFold(),
                scoring=make_scorer(my_r2_6)).mean()
#> 0.6417227070606119

# 方法1
my_scores = cross_val_score(my_model, X, y, cv=len(y),
                            scoring='neg_mean_squared_error')
(-my_scores.mean())**0.5
#> 15.697306009399101 # RMSE（検証）

# 方法2
my_scores = cross_val_score(my_model, X, y, cv=len(y),
                            scoring='neg_root_mean_squared_error')
(my_scores**2).mean()**0.5 # my_scores.mean()ではない
#> 15.697306009399101 # RMSE（検証）

def f(id): # 指定した番号のデータを検証データとし，その予測値を求める．
    my_train = my_data.drop([id])
    my_valid = my_data.take([id])
    X, y = my_train[['speed']], my_train['dist']
    return  LinearRegression().fit(X, y).predict(my_valid[['speed']])[0]

y  = my_data['dist']
y_ = [f(id) for id in my_data.index] # LOOCVでの予測値

mean_squared_error(y, y_)**0.5       # RMSE（検証）
#> 15.697306009399101                # （前と同じ結果）

r2_score(y_true=y, y_pred=y_)        # 決定係数1（検証）
#> 0.6213688690415049

np.corrcoef(y, y_)[0, 1]**2          # 決定係数6（検証）
#> 0.6217139186808114


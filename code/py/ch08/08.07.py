import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-6, 6, 100)
y = 1 / (1 + np.exp(-x))
plt.plot(x, y)

import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, GridSearchCV, LeaveOneOut
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)
X, y = my_data.drop(columns=['LPRICE2']), my_data['LPRICE2']

my_pipeline = Pipeline([('sc', StandardScaler()),        # 標準化
                        ('mlp', MLPRegressor())])        # ニューラルネットワーク
my_pipeline.fit(X, y)                                    # 訓練

my_scores = cross_val_score(my_pipeline, X, y,
                            scoring='neg_root_mean_squared_error')

y_ = my_pipeline.predict(X)
mean_squared_error(y_, y)**0.5
#> 0.23277167397113335 # RMSE（訓練）

-my_scores.mean()
#> 0.46383292352312744 # RMSE（検証）

my_pipeline = Pipeline([
    ('sc', StandardScaler()),
    ('mlp', MLPRegressor(tol=1e-5,         # 改善したと見なす基準
                         max_iter=5000))]) # 改善しなくなるまでの反復数
my_layers = (1, 3, 5,                                         # 隠れ層1層の場合
             (1, 1), (3, 1), (5, 1), (1, 2), (3, 2), (5, 2))  # 隠れ層2層の場合
my_params = {'mlp__activation': ('logistic', 'tanh', 'relu'), # 活性化関数
             'mlp__hidden_layer_sizes': my_layers}            # 隠れ層の構造
my_search = GridSearchCV(estimator=my_pipeline,
                         param_grid=my_params,
                         cv=LeaveOneOut(),
                         scoring='neg_mean_squared_error',
                         n_jobs=-1).fit(X, y)
my_model = my_search.best_estimator_ # 最良モデル

my_search.best_params_               # チューニング結果
#> {'mlp__activation': 'tanh', 'mlp__hidden_layer_sizes': 3}

y_ = my_model.predict(X)
mean_squared_error(y_, y)**0.5
#> 0.21660824459726416 # RMSE（訓練）

(-my_search.best_score_)**0.5
#> 0.2832501479521093  # RMSE（検証）


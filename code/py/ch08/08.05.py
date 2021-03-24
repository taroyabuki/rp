import numpy as np
import pandas as pd
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.pipeline import Pipeline

my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)

n = len(my_data)
my_data2 = my_data.assign(rand1=np.random.random(n), rand2=np.random.random(n))
X, y = my_data2.drop(columns=['LPRICE2']), my_data2['LPRICE2']

my_sfs = SequentialFeatureSelector(
    estimator=LinearRegression(),
    direction='forward',              # 変数増加法
    cv=LeaveOneOut(),
    scoring='neg_mean_squared_error')

my_pipeline = Pipeline([       # 変数選択の後で再訓練を行うようにする．
  ('sfs', my_sfs),             # 変数選択
  ('lm', LinearRegression())]) # 回帰分析

my_params = {'sfs__n_features_to_select':range(1, 6)} # 選択する変数の上限
my_search = GridSearchCV(estimator=my_pipeline,
                         param_grid=my_params,
                         cv=LeaveOneOut(),
                         scoring='neg_mean_squared_error',
                         n_jobs=-1).fit(X, y)
my_model = my_search.best_estimator_ # 最良のパラメータで再訓練したモデル
my_search.best_estimator_.named_steps.sfs.get_support()
#> array([ True,  True,  True,  True, False, False])


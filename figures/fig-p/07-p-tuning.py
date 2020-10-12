import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist']

from sklearn.neighbors import KNeighborsRegressor
my_model = KNeighborsRegressor()
my_params = {'n_neighbors': list(range(1,16))} # K=1から15を調べる．

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=20) # 交差検証（5分割，20回）
my_search = GridSearchCV(my_model,
                         my_params,
                         cv=my_cv,
                         n_jobs=-1,               # 並列計算
                         return_train_score=True) # 訓練データでのスコアも計算する．
my_search.fit(X, y) # チューニングの実行

import pandas as pd
my_result = my_search.cv_results_
my_df = pd.DataFrame({'k':range(1, 16),
                      'train': my_result['mean_train_score'],
                      'test': my_result['mean_test_score']})
my_df.plot(x='k', ylabel='R^2', style='o-')

import matplotlib.pyplot as plt
plt.savefig('07-p-tuning.pdf')
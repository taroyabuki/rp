import numpy
numpy.random.seed(0)

from sklearn.neighbors import KNeighborsClassifier
my_model = KNeighborsClassifier()

# チューニングの設定（1以上21未満のKを調べる．）
params = {'n_neighbors': list(range(1,21))}

# データの読み込み
import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10) # 5分割交差検証（10回）

my_search = GridSearchCV(my_model,
                         params,
                         cv=my_cv,
                         return_train_score=True, # 正解率（訓練）の保存
                         n_jobs=-1)               # 並列処理
my_search.fit(X, y) # 訓練

import pandas as pd
my_plt = pd.DataFrame({
    'n_neighbors':range(1,21),
    'train':my_search.cv_results_['mean_train_score'],
    'test':my_search.cv_results_['mean_test_score']}).plot('n_neighbors')
my_plt.set_ylabel('Accuracy')
import matplotlib.pyplot as plt
plt.savefig('09-p-knn.pdf')
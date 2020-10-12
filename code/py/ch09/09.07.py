### 9.7.2 Pythonの場合

from sklearn import tree
my_model = tree.DecisionTreeClassifier()

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

from sklearn.model_selection import *
my_cv = KFold(n_splits=5) # 5分割交差検証
my_score = cross_validate(my_model, X, y,
                          cv=my_cv,
                          return_train_score=True)
my_score['test_score'].mean() # 正解率（検証）
#> 0.9133333333333333

my_model.fit(X, y)
tree.plot_tree(my_model, filled=True)


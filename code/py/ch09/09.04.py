import numpy as np
# 正解
y = np.array(['serosa', 'setosa'])

# 予測
y_A = np.array(['serosa', 'versicolor'])

# 比較
y_A == y
#> array([ True, False])

# 正解率
(y_A == y).mean()
#> 0.5

### 9.4.2 Pythonの場合

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

from sklearn.neighbors import KNeighborsClassifier
my_model = KNeighborsClassifier()
my_model.fit(X, y)
y_ = my_model.predict(X)

from sklearn.metrics import confusion_matrix
confusion_matrix(y, y_) # Rの仕様に合わせる．
#> array([[50,  0,  0],
#>        [ 0, 47,  2],
#>        [ 0,  3, 48]])

my_model.score(X, y)
# あるいは
y_ = my_model.predict(X)
(y_ == y).mean()
#> 0.9666666666666667


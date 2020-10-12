### 9.3.2 Pythonの場合

from sklearn.neighbors import KNeighborsClassifier
my_model = KNeighborsClassifier()

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species
my_model.fit(X, y)

import pandas as pd
my_test = pd.DataFrame([[5.0, 3.5, 1.5, 0.5], [6.5, 3.0, 5.0, 2.0]])
my_model.predict(my_test)
#> array(['setosa', 'virginica'], dtype=object)

my_model.predict_proba(my_test)
#> array([[1. , 0. , 0. ],
#>        [0. , 0.2, 0.8]])


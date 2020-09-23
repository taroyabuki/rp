import numpy as np
x = np.arange(-6, 6, 0.1)
y = 1 / (1 + np.exp(-x))
import matplotlib.pyplot as plt
plt.plot(x, y)

### 10.5.2 Pythonの場合

import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/titanic.csv'
my_data = pd.read_csv(my_url)
X, y = pd.get_dummies(my_data.iloc[:,0:3], drop_first=True), my_data.Survived

from sklearn.linear_model import LogisticRegression
my_model = LogisticRegression()

# 5分割交差検証（10回）
from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10)

my_scores = cross_val_score(my_model, X, y, cv=my_cv, n_jobs=-1)
my_scores.mean() # 正解率（検証）

my_model.fit(X, y)

my_model.coef_
#> array([[-0.92869887, -1.68151296, -0.80815719, -2.36602057,  0.9831511 ]])

my_model.intercept_
#> array([1.94694608])

my_model.score(X, y) # 正解率（訓練）
#> 0.7782825988187188


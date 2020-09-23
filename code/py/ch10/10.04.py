### 10.4.2 Pythonの場合

import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/titanic.csv'
my_data = pd.read_csv(my_url)
my_data.head()
#>   Class   Sex    Age Survived
#> 0   1st  Male  Child      Yes
#> 1   1st  Male  Child      Yes
#> 2   1st  Male  Child      Yes
#> 3   1st  Male  Child      Yes
#> 4   1st  Male  Child      Yes

#### 10.4.3.2 Pythonの場合

import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/titanic.csv'
my_data = pd.read_csv(my_url)

X, y = pd.get_dummies(my_data.iloc[:,0:3], drop_first=True), my_data.Survived
X.head()
#>    Class_2nd  Class_3rd  Class_Crew  Sex_Male  Age_Child
#> 0          0          0           0         1          1
#> 1          0          0           0         1          1
#> 2          0          0           0         1          1
#> 3          0          0           0         1          1
#> 4          0          0           0         1          1

from sklearn import tree
my_model = tree.DecisionTreeClassifier(max_depth=3)

# 5分割交差検証（10回）
from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10)

my_scores = cross_val_score(my_model, X, y, cv=my_cv, n_jobs=-1)
my_scores.mean() # 正解率（検証）
#> 0.7892313955885385

my_model.fit(X, y)
tree.plot_tree(my_model, filled=True)


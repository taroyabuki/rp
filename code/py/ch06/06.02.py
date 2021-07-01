#### 6.2.2.2 Python

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
iris
#>    Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
#> 0           5.1          3.5           1.4          0.2  setosa
#> （以下省略）

import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()
#>    sepal_length  sepal_width  petal_length  petal_width species
#> 0           5.1          3.5           1.4          0.2  setosa
#> （以下省略）

import pandas as pd
from sklearn.datasets import load_iris
tmp = load_iris()
iris = pd.DataFrame(tmp.data, columns=tmp.feature_names)
iris['target'] = tmp.target_names[tmp.target]
iris.head()
#>    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
#> 0                5.1               3.5                1.4               0.2  setosa
#> （以下省略）

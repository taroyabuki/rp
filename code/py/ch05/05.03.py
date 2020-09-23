import numpy as np
x = [2, 3]
y = (x - np.mean(x)) / np.std(x)
y
#> array([-1.,  1.])

[np.mean(y), np.std(y)]
#> [0.0, 1.0]

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data

import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
tmp = pd.DataFrame(scaler.fit_transform(iris.iloc[:, 0:4])) # 標準化
tmp.head()
#>           0         1         2         3
#> 0 -0.900681  1.019004 -1.340227 -1.315444
#> 1 -1.143017 -0.131979 -1.340227 -1.315444
#> 2 -1.385353  0.328414 -1.397064 -1.315444
#> 3 -1.506521  0.098217 -1.283389 -1.315444
#> 4 -1.021849  1.249201 -1.340227 -1.315444

scaler.mean_ # 元のデータの平均
#> array([5.84333333, 3.05733333, 3.758     , 1.19933333])

scaler.scale_ # 元のデータの標準偏差
#> array([0.82530129, 0.43441097, 1.75940407, 0.75969263])

tmp.describe() # 基本統計量
#>                   0             1             2             3
#> count  1.500000e+02  1.500000e+02  1.500000e+02  1.500000e+02
#> mean  -2.775558e-16 -9.695948e-16 -8.652338e-16 -4.662937e-16
#> std    1.003350e+00  1.003350e+00  1.003350e+00  1.003350e+00
#> 以下略

tmp.std(ddof=0) # 不偏出ない分散の平方根
#> 0    1.0
#> 1    1.0
#> 2    1.0
#> 3    1.0
dtype: float64

import scipy.stats as sp
tmp = pd.DataFrame(sp.stats.zscore(iris.iloc[:, 0:4], ddof=1)) # 標準化

tmp.describe() # 基本統計量
#>                   0             1             2             3
#> count  1.500000e+02  1.500000e+02  1.500000e+02  1.500000e+02
#> mean  -1.068220e-15 -3.639681e-16 -2.967996e-16 -2.309264e-16
#> std    1.000000e+00  1.000000e+00  1.000000e+00  1.000000e+00
#> 以下略

import pandas as pd
my_df = pd.DataFrame({'id': [1, 2, 3],
                      'class': ['A', 'B', 'C']})
pd.get_dummies(my_df)
#>    id  class_A  class_B  class_C
#> 0   1        1        0        0
#> 1   2        0        1        0
#> 2   3        0        0        1

pd.get_dummies(my_df, drop_first=True)
#>    id  class_B  class_C
#> 0   1        0        0
#> 1   2        1        0
#> 2   3        0        1


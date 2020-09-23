x = [165, 170, 175, 180, 185]
import numpy as np
np.mean(x) # リストの場合（アレイ・シリーズも可）
#> 175.0

x = np.array([165, 170, 175, 180, 185])
x.mean() # アレイの場合
#> 175.0

import pandas as pd
x = pd.Series([165, 170, 175, 180, 185])
x.mean() # シリーズの場合
#> 175.0

np.sum(x) / len(x) # 平均（その2）
#> 

x - np.mean(x)
#> array([-10.,  -5.,   0.,   5.,  10.])

np.mean(x - np.mean(x))
#> 0.0

np.mean((x - np.mean(x)) ** 2)
#> 50.0

np.sqrt(np.mean((x - np.mean(x)) ** 2))
#> 7.0710678118654755

y = [173, 174, 175, 176, 177]

np.mean(y)
#> 175.0 # 平均

np.sqrt(np.mean((y - np.mean(y)) ** 2))
#> 1.4142135623730951 # 標準偏差

np.var(x) # 分散
#> 50.0

np.std(x) # 標準偏差
#> 7.0710678118654755

np.var(x, ddof=1) # 不偏分散
#> 62.5

np.std(x, ddof=1) # 平方根
#> 7.905694150420948

np.var(x) # 不偏でない分散
#> 50.0

np.std(x) # 平方根
#> 7.0710678118654755

import pandas as pd
s = pd.Series(x)
s.describe()
#> count      5.000000 （データ数）
#> mean     175.000000 （平均）
#> std        7.905694 （不偏分散の非負の平方根）
#> min      165.000000 （最小値）
#> 25%      170.000000 （第1四分位数）
#> 50%      175.000000 （中央値）
#> 75%      180.000000 （第2四分位数）
#> max      185.000000 （最大値）
#> dtype: float64

# s.describe()で計算済み

my_df = pd.DataFrame({
    'english': [60, 90, 70, 90],
    'math': [70, 80, 90, 100]})
my_df.describe()

#>        english        math
#> count      4.0    4.000000
#> mean      77.5   85.000000
#> std       15.0   12.909944
# 以下省略

import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])
iris['target'] = [data['target_names'][i] for i in data['target']]
iris.head()
#>    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
#> 0                5.1               3.5                1.4               0.2  setosa
#> 1                4.9               3.0                1.4               0.2  setosa
#> 2                4.7               3.2                1.3               0.2  setosa
#> 3                4.6               3.1                1.5               0.2  setosa
#> 4                5.0               3.6                1.4               0.2  setosa

iris.hist('sepal length (cm)')

import matplotlib.pyplot as plt

x = [1, 2, 3]
plt.hist(x, bins=2) # 階級数は2

iris.boxplot()

iris.describe()
#>        sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
#> count         150.000000        150.000000         150.000000        150.000000
#> mean            5.843333          3.057333           3.758000          1.199333
#> std             0.828066          0.435866           1.765298          0.762238
#> min             4.300000          2.000000           1.000000          0.100000
#> 25%             5.100000          2.800000           1.600000          0.300000
#> 50%             5.800000          3.000000           4.350000          1.300000
#> 75%             6.400000          3.300000           5.100000          1.800000
#> max             7.900000          4.400000           6.900000          2.500000

iris.boxplot('sepal length (cm)',
             by='target')

辻君へ：お願いします．

iris.plot('sepal length (cm)',
          'sepal width (cm)',
          kind='scatter')

import numpy as np
x = np.arange(-2, 2, 0.1)
y = x**3 - x
import matplotlib.pyplot as plt
plt.plot(x, y)


x = [165, 170, 175, 180, 185]
import numpy as np
np.mean(x) # リストの場合
#> 175.0

x = np.array([165, 170, 175, 180, 185])
x.mean() # アレイの場合（np.mean(x)も可）
#> 175.0

import pandas as pd
x = pd.Series([165, 170, 175, 180, 185])
x.mean() # シリーズの場合（np.mean(x)も可）
#> 175.0

n = len(x) # 標本の大きさ
sum(x) / n
#> 

y = [173, 174, 175, 176, 177]
np.mean(y)
#> 175.0

np.var(x) # xの分散
#> 50.0

np.var(y) # yの分散
#> 2.0

sum((x - np.mean(x))**2) / n # 分散
#> 50.0

np.std(x) # xの標準偏差
#> 7.0710678118654755

np.std(y) # yの標準偏差
#> 1.4142135623730951

np.var(x)**0.5 # xの標準偏差
#> 7.0710678118654755

import pandas as pd
s = pd.Series(x)
s.describe()
#> count      5.000000 （データ数）
#> mean     175.000000 （平均）
#> std        7.905694 （標準偏差）
#> min      165.000000 （最小値）
#> 25%      170.000000 （第1四分位数）
#> 50%      175.000000 （中央値）
#> 75%      180.000000 （第2四分位数）
#> max      185.000000 （最大値）
#> dtype: float64

# s.describe()で計算済み

my_df = pd.DataFrame({
    'english': [60, 90, 70,  90],
    'math':    [70, 80, 90, 100]})
my_df.describe()
#>        english        math
#> count      4.0    4.000000
#> mean      77.5   85.000000
#> std       15.0   12.909944
# 以下省略

import numpy as np
x = [165, 170, 175, 180, 185]
n = len(x)

np.var(x)
# あるいは
np.var(x, ddof=0)
#> 50.0

np.var(x, ddof=1)
# あるいは
np.var(x) * n / (n - 1)
#> 62.5

# 不偏分散の平方根
np.std(x, ddof=1)
# あるいは
np.sqrt(n / (n - 1)) * np.std(x)
#> 7.905694150420949

# 標準偏差'
np.std(x)
# あるいは
np.std(x, ddof=0)
#> 7.0710678118654755

np.std(x, ddof = 1) / len(x)**0.5
#> 3.5355339059327373

import pandas as pd

my_df = pd.DataFrame({
    'name':    ['A', 'B', 'C', 'D'],
    'english': [ 60,  90,  70,  90],
    'math':    [ 70,  80,  90, 100],
    'gender':  ['f', 'm', 'm', 'f']})

my_df['english'].var()
# あるいは
import numpy as np
np.var(my_df['english'], ddof=1)

#> 225.0

my_df.var()
# あるいは
my_df.agg('var')

#> english    225.000000
#> math       166.666667
#> dtype: float64

my_df.iloc[:, [1,2]].agg(
    lambda x: np.std(x, ddof=1) /
    len(x)**0.5)
#> english    7.500000
#> math       6.454972
#> dtype: float64

my_df.describe()
#>        english        math
#> count      4.0    4.000000
#> mean      77.5   85.000000
#> std       15.0   12.909944
#> min       60.0   70.000000
#> 25%       67.5   77.500000
#> 50%       80.0   85.000000
#> 75%       90.0   92.500000
#> max       90.0  100.000000





my_df.groupby('gender').count()
# あるいは
my_df.groupby('gender').agg(len)

#>         name  english  math
#> gender
#> f          2        2     2
#> m          2        2     2

my_df.groupby('gender').mean()
# あるいは
my_df.groupby('gender').agg('mean')

#>         english  math
#> gender
#> f          75.0  85.0
#> m          80.0  85.0

my_df.groupby('gender').agg(
    lambda x: x.std() /
    len(x)**0.5)
#>         english  math
#> gender
#> f            15    15
#> m            10     5


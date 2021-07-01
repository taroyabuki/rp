## 3.7 反復処理

import numpy as np
import pandas as pd

### 3.7.1 指定した回数→1次元データ

def f1(x):
    tmp = np.random.random(x)
    return np.mean(tmp)

f1(10)                # 動作確認
#> 0.5427033207230424 # 結果の例

### 3.7.1 指定した回数→1次元データ

[f1(10) for i in range(3)]
#> [0.4864425069985622,
#>  0.4290935578857099,
#>  0.535206509631883]

### 3.7.1 指定した回数→1次元データ

[f1(10)] * 3
#> [0.43725641184595576,
#>  0.43725641184595576,
#>  0.43725641184595576]

### 3.7.2 1次元データ→1次元データ

v = [5, 10, 100]
[f1(x) for x in v] # 方法1
#> [0.454, 0.419, 0.552]

# あるいは

v = pd.Series([5, 10, 100])
v.apply(f1) # 方法2
#> 0    0.394206
#> 1    0.503949
#> 2    0.532698
#> dtype: float64

### 3.7.2 1次元データ→1次元データ

pd.Series([10] * 3).apply(f1)
# 結果は割愛

### 3.7.3 1次元データ→データフレーム

def f2(n):
    tmp = np.random.random(n)
    return pd.Series([
        n,
        np.mean(tmp),
        np.std(tmp)],
        index=['x', 'p', 'q'])

f2(10) # 動作確認
#> x    10.000000
#> p     0.470242 （平均の例）
#> q     0.265091 （標準偏差の例）
#> dtype: float64

### 3.7.3 1次元データ→データフレーム

v = pd.Series([5, 10, 100])
v.apply(f2)
#>        x         p         q
#> 0    5.0  0.614590  0.237824
#> 1   10.0  0.575434  0.212021
#> 2  100.0  0.471762  0.282674

### 3.7.4 データフレーム→データフレーム

def f3(x, y):
    tmp = np.random.random(x) * y
    return pd.Series([x,
                      y,
                      np.mean(tmp),
                      np.std(tmp)],
                     index=['x', 'y', 'p', 'q'])

f3(10, 6) # 動作確認
#> x    10.000000
#> y     6.000000
#> p     2.711746 （平均の例）
#> q     1.370546 （標準偏差の例）
#> dtype: float64

### 3.7.4 データフレーム→データフレーム

my_df = pd.DataFrame({
    'x': [5, 10, 100, 5, 10, 100],
    'y': [6, 6, 6, 12, 12, 12]})

my_df.apply(
    lambda row:
    f3(row['x'], row['y']),
    axis=1)
# あるいは
my_df.apply(lambda row:
            f3(*row), axis=1)

#>        x     y     p     q
#> 0    5.0   6.0  3.18  1.50
#> 1   10.0   6.0  3.01  1.94
#> 2  100.0   6.0  2.92  1.62
#> 3    5.0  12.0  5.94  2.80
#> 4   10.0  12.0  7.66  3.75
#> 5  100.0  12.0  5.96  3.46

### 3.7.5 補足：反復処理の並列化

from pandarallel import pandarallel
pandarallel.initialize() # 準備

v = pd.Series([5, 10, 100])
v.parallel_apply(f1)
# 結果は割愛


import numpy as np

def my_f1(x):
    tmp = np.random.random(x)
    return np.mean(tmp)

my_f1(10) # 動作確認
#> 0.5427033207230424 （結果の例）

[my_f1(10) for i in range(3)]
#> [0.4864425069985622,
#>  0.4290935578857099,
#>  0.535206509631883]

[my_f1(10)] * 3
#> [0.43725641184595576,
#>  0.43725641184595576,
#>  0.43725641184595576]

my_v = [5, 10, 100]
[my_f1(x) for x in my_v] # 方法1
#> [0.454, 0.419, 0.552]

# あるいは

my_v = pd.Series([5, 10, 100])
my_v.apply(my_f1) # 方法2
#> 0    0.394206
#> 1    0.503949
#> 2    0.532698
#> dtype: float64

pd.Series([10] * 3).apply(my_f1)
# 結果は割愛

def my_f2(n):
    tmp = np.random.random(n)
    return pd.Series([
        n,
        np.mean(tmp),
        np.std(tmp)],
        index=['x', 'p', 'q'])

my_f2(10) # 動作確認
#> x    10.000000
#> p     0.470242 （平均の例）
#> q     0.265091 （標準偏差の例）
#> dtype: float64

my_v = pd.Series([5, 10, 100])
my_v.apply(my_f2)
#>        x         p         q
#> 0    5.0  0.614590  0.237824
#> 1   10.0  0.575434  0.212021
#> 2  100.0  0.471762  0.282674

def my_f3(x, y):
    tmp = np.random.random(x) * y
    return pd.Series([x,
                      y,
                      np.mean(tmp),
                      np.std(tmp)],
                     index=['x', 'y', 'p', 'q'])

my_f3(10, 6) # 動作確認
#> x    10.000000
#> y     6.000000
#> p     2.711746 （平均の例）
#> q     1.370546 （標準偏差の例）
#> dtype: float64

my_df = pd.DataFrame({
    'x': [5, 10, 100, 5, 10, 100],
    'y': [6, 6, 6, 12, 12, 12]})

my_df.apply(
    lambda row:
    my_f3(row['x'], row['y']),
    axis=1)
# あるいは
my_df.apply(lambda row:
            my_f3(*row), axis=1)

#>        x     y     p     q
#> 0    5.0   6.0  3.18  1.50
#> 1   10.0   6.0  3.01  1.94
#> 2  100.0   6.0  2.92  1.62
#> 3    5.0  12.0  5.94  2.80
#> 4   10.0  12.0  7.66  3.75
#> 5  100.0  12.0  5.96  3.46

from pandarallel import pandarallel
pandarallel.initialize() # 準備

my_v = pd.Series([5, 10, 100])
my_v.parallel_apply(my_f1)
# 結果は割愛


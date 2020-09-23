my_v = ['foo', 'bar', 'baz']

len(my_v)
#> 3

my_v[1]
#> 'bar'

my_v[-2]
#> 'bar'

my_v + ['qux']
#> ['foo', 'bar', 'baz', 'qux']

my_v.append('qux')
# あるいは
my_v = my_v + ['qux']
my_v
#> ['foo', 'bar', 'baz', 'qux']

my_v = list(range(5))
# my_v = [0, 1, 2, 3, 4]と同じ

list(range(1, 10, 2))
#> [1, 3, 5, 7, 9]

import numpy as np
import pandas as pd

my_v = np.array([2, 3, 5, 7])  # アレイ
# あるいは
mv_v = pd.Series([2, 3, 5, 7]) # シリーズ

my_v + 10 # 加算
#> array([12, 13, 15, 17])

my_v * 10 # 乗算
#> array([20, 30, 50, 70])

my_u = [2, 3]
import numpy as np
np.sin(my_u)
#> array([0.90929743, 0.14112001])

my_v = np.array([2,  3,   5,    7])
my_w = np.array([1, 10, 100, 1000])
my_v + my_w
#> array([   3,   13,  105, 1007])

my_v * my_w
#> array([   2,   30,  500, 7000])

np.dot(my_v, my_w)
#> 7532

import numpy as np
u = np.array([1, 2, 3])
v = np.array([1, 2, 3])
w = np.array([1, 2, 4])

# 全体の比較
all(u == v)
#> True

all(u == w)
#> False

# 要素ごとの比較
u == v
#> array([ True,  True,  True])
> u == w
#> array([ True,  True, False])

# 同じ要素の数
(u == w).sum()
#> 2

# 同じ要素の割合
(u == w).mean()
#> [1] 0.6666667

my_list = [1, "two"]

my_list[1]
#> 'two'

my_dic = {'apple'  : 'りんご',
          'orange' : 'みかん'}

my_dic['apple']
#> 'りんご'


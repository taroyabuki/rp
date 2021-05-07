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
# my_v = [0, 1, 2, 3, 4]と同等

list(range(0, 11, 2))
#> [0, 2, 4, 6, 8, 10]

np.arange(0, 1.1, 0.5)
#> array([0. , 0.5, 1. ])

np.linspace(0, 1, 5)
#> array([0.  , 0.25, 0.5 , 0.75, 1.  ])

[10] * 5
#> [10, 10, 10, 10, 10]

import numpy as np
my_v = np.array([2, 3, 5, 7])

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
# あるいは
my_v @ my_w

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
u == w
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

my_map = {'apple' :'りんご',
          'orange':'みかん'}

my_map['grape'] = 'ぶどう'

my_map['apple']
# あるいは
tmp = 'apple'
my_map[tmp]
#> 'りんご'


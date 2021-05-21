x = ['foo', 'bar', 'baz']

len(x)
#> 3

x[1]
#> 'bar'

x[1] = 'BAR'
x # 結果の確認
#> ['foo', 'BAR', 'baz']

x[1] = 'bar # 元に戻す．

x[-2]
#> 'bar'

x + ['qux']
#> ['foo', 'bar', 'baz', 'qux']

x = x + ['qux']
x # 結果の確認
#> ['foo', 'bar', 'baz', 'qux']

list(range(5))
#> [0, 1, 2, 3, 4]

list(range(0, 11, 2))
#> [0, 2, 4, 6, 8, 10]

np.arange(0, 1.1, 0.5)
#> array([0. , 0.5, 1. ])

np.linspace(0, 1, 5)
#> array([0.  , 0.25, 0.5 , 0.75, 1.  ])

[10] * 5
#> [10, 10, 10, 10, 10]

import numpy as np
x = np.array([2, 3, 5, 7])

x + 10 # 加算
#> array([12, 13, 15, 17])

x * 10 # 乗算
#> array([20, 30, 50, 70])

x = [2, 3]
np.sin(x)
#> array([0.90929743, 0.14112001])

x = np.array([2,  3,   5,    7])
y = np.array([1, 10, 100, 1000])
x + y
#> array([   3,   13,  105, 1007])

x * y
#> array([   2,   30,  500, 7000])

np.dot(x, y)
# あるいは
x @ y

#> 7532

import numpy as np
u = np.array([1, 2, 3])
v = np.array([1, 2, 3])
w = np.array([1, 2, 4])

all(u == v) # 全体の比較
#> True

all(u == w) # 全体の比較
#> False

u == v      # 要素ごとの比較
#> array([ True,  True,  True])

u == w      # 要素ごとの比較
#> array([ True,  True, False])

(u == w).sum()  # 同じ要素の数
#> 2

(u == w).mean() # 同じ要素の割合
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

x = ['foo', 'bar', 'baz']
y = x
y[1] = 'BAR'
y
#> ['foo', 'BAR', 'baz']

x
#> ['foo', 'BAR', 'baz']

x = ['foo', 'bar', 'baz']
y = x.copy()             # 「y = x」とせずに，コピーする．
x == y, x is y
#> (True, False)         # xとyは，等価（内容は同じ）だが同一ではない．

y[1] = 'BAR'             # yを更新しても，
x
#> ['foo', 'bar', 'baz'] # xは変化しない．


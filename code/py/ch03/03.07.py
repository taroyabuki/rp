import numpy as np
my_v = [1, np.nan, 3]
my_v
#> [1, nan, 3]

np.isnan(my_v[1])
#> True

my_v[1] == np.nan # 誤り
#> False

x = 123
type(x)
#> int

%whos
Variable   Type      Data/Info
------------------------------
my_v       list      n=3
np         module    <module 'numpy' from '/op<...>kages/numpy/__init__.py'>
x          int       123


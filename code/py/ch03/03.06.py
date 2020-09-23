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


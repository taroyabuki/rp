### 3.8.2 変数や関数についての調査

x = 123
type(x)
#> int

%whos
#> Variable   Type      Data/Info
#> ------------------------------
#> math       module    <module 'math' from '/opt<...>-38-x86_64-linux-gnu.so'>
#> x          int       123

import math
?math.log
# あるいは
help(math.log)

### 3.8.3 RのNA，Pythonのnan

import numpy as np
my_v = [1, np.nan, 3]
my_v
#> [1, nan, 3]

np.isnan(my_v[1])
#> True

my_v[1] == np.nan # 誤り
#> False


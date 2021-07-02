---
jupyter:
  kernelspec:
    display_name: "Python 3"
    name: python3
---
### 5.2.1 標準化

``` code
x1 = [1, 2, 3]

import numpy as np
z1 = (x1 - np.mean(x1)) / np.std(x1)
# あるいは
from scipy.stats import zscore
z1 = zscore(x1)

z1
#> array([-1.22474487,
#>         0.        ,
#>         1.22474487])
```

``` code
[z1.mean(), z1.std()]
#> [0.0, 0.9999999999999999]
```

``` code
z1 * np.std(x1) + np.mean(x1)
#> array([1., 2., 3.])
```

``` code
x2 = [1, 3, 5]
z2 = (x2 - np.mean(x1)) / np.std(x1)
[z2.mean(), z2.std()]
#> [1.2247448713915892,
#>  1.9999999999999998]
```

### 5.2.2 ワンホットエンコーディング

``` code
import pandas as pd
from sklearn.preprocessing import (
    OneHotEncoder)

my_df = pd.DataFrame({
    'id':    [ 1 ,  2 ,  3 ],
    'class': ['A', 'B', 'C']})

my_enc = OneHotEncoder()
tmp = my_enc.fit_transform(
    my_df[['class']]).toarray()
my_names = my_enc.get_feature_names()
pd.DataFrame(tmp, columns = my_names)
#>    x0_A  x0_B  x0_C
#> 0   1.0   0.0   0.0
#> 1   0.0   1.0   0.0
#> 2   0.0   0.0   1.0
```

``` code
my_df2 = pd.DataFrame({
    'id':    [ 4,   5,   6 ],
    'class': ['B', 'C', 'B']})
tmp = my_enc.transform(
    my_df2[['class']]).toarray()
pd.DataFrame(tmp, columns = my_names)
#>    x0_A  x0_B  x0_C
#> 0   0.0   1.0   0.0
#> 1   0.0   0.0   1.0
#> 2   0.0   1.0   0.0
```

#### 5.2.2.1 補足：冗長性の排除

``` code
my_enc = OneHotEncoder(drop='first')

tmp = my_enc.fit_transform(
    my_df[['class']]).toarray()
my_names = my_enc.get_feature_names()
pd.DataFrame(tmp, columns = my_names)
#>    x0_B  x0_C
#> 0   0.0   0.0
#> 1   1.0   0.0
#> 2   0.0   1.0

tmp = my_enc.transform(
    my_df2[['class']]).toarray()
pd.DataFrame(tmp, columns = my_names)
#>    x0_B  x0_C
#> 0   1.0   0.0
#> 1   0.0   1.0
#> 2   1.0   0.0
```


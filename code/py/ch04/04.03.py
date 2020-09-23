from scipy import stats
stats.binom_test(14, n=20, p=0.5)

#> 0.11531829833984371

from scipy.stats import binom
x = 5
s = binom.cdf(k=x, n=20, p=0.5)
s
#> 0.020694732666015625

binom.ppf(q=s, n=20, p=0.5)
#> 5.0

from scipy.stats import binom
alpha = 0.05
binom.ppf(q=[alpha / 2, 1 - alpha / 2], n=20, p=0.5)
#> array([ 6., 14.]) # 左側の境界は6，右側の境界は14

import numpy as np
X = np.array([0] * 6 + [1] * 14)            # 手順1
tmp = np.random.choice(X, 20, replace=True) # 手順2
tmp
#> array([1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1])

np.mean(tmp) # 手順3
#> 0.8

# 手順4
result = [np.mean(np.random.choice(X, 20, replace=True)) for _ in range(10**5)]
np.quantile(result, [0.025, 0.975]) # 手順5

#> array([0.5, 0.9])


## 4.3 乱数

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(
      1,     # 最小
      7,     # 最大+1
      10000) # 個数
# あるいは
x = np.random.choice(
      range(1, 7), # 1から6
      10000,       # 個数
      True)        # 重複あり
plt.hist(x, bins=6) # ヒストグラム

x = np.random.uniform(0, 1, 1000)
# あるいは
x = np.random.random(1000)
plt.hist(x)

tmp = np.random.uniform(1, 7, 1000)
x = np.array(tmp, dtype=int)
plt.hist(x, bins=6) # 結果は割愛

x = np.random.binomial(100, 0.5, 1000)
plt.hist(x)

x = np.random.normal(165, 10, 1000)
plt.hist(x)

n = 10000
x = [np.random.normal(
    size=5, scale=3).var()
    for i in range(n)]

np.mean(x)
#> 7.16166215199147

plt.hist(x, bins=14)

x = [np.random.normal(
    size=5, scale=3).std(ddof=1)
    for i in range(n)]

np.mean(x)
#> 2.797564339614321


import matplotlib.pyplot as plt
import numpy as np

x = np.random.choice(
      range(1, 7), # 1から6
      10000,       # 個数
      True)        # 重複あり
plt.hist(x, bins=6) # ヒストグラム
plt.savefig('04-p-random-sample.pdf')

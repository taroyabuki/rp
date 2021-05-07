import numpy as np
X = [32.1, 26.2, 27.5, 31.8, 32.1, 31.2, 30.1, 32.4, 32.3, 29.9, 29.6,
     26.6, 31.2, 30.9, 29.3]
Y = [35.4, 34.6, 31.1, 32.4, 33.3, 34.7, 35.3, 34.3, 32.1, 28.3, 33.3,
     30.5, 32.6, 33.3, 32.2]
Z = np.array(X) - np.array(Y) # 対標本として扱う．

n = 10**5
result = [np.random.choice(Z, len(Z), replace=True).mean() for _ in range(n)]

import matplotlib.pyplot as plt
plt.hist(result, bins='sturges')
plt.savefig('04-p-boot-ttest.pdf')

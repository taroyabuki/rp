import numpy as np
n = 10000
x = [np.random.normal(
    size=5, scale=3).var()
     for i in range(n)]

print(np.mean(x))

import matplotlib.pyplot as plt
plt.hist(x, bins=14)
plt.savefig('04-p-bias-var.pdf')
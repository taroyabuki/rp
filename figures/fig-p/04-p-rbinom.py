import matplotlib.pyplot as plt

import numpy as np
x = np.random.binomial(100, 0.5, 1000)
plt.hist(x)

plt.savefig('04-p-rbinom.pdf')

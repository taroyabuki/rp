import matplotlib.pyplot as plt

import numpy as np
x = np.random.normal(165, 10, 1000)
plt.hist(x)

plt.savefig('04-p-rnorm.pdf')

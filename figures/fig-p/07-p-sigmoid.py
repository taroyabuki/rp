import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-6, 6, 0.1)
y = 1.0 / (1 + np.exp(-x))
plt.plot(x, y)
plt.savefig('07-p-sigmoid.pdf')
import numpy as np
x = np.arange(-2, 2, 0.1)
y = x**3 - x
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.savefig('04-p-curve.pdf')
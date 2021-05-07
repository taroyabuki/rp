import numpy as np
import pandas as pd
from scipy.stats import binom

t = 4 / 10
n = 15
x = np.array(range(0, 16))
my_pr = binom.pmf(x, n, t)

my_data = pd.DataFrame({
    'x':x, 'y1':my_pr, 'y2':my_pr})
my_data.loc[x >  2, 'y1'] = np.nan # 当たった回数が2回超過
my_data.loc[x <= 2, 'y2'] = np.nan # 当たった回数が2回以下
ax = my_data.plot(x='x', style='o', ylabel='probability', legend=False)
ax.vlines(x=x, ymin=0, ymax=my_pr)

import matplotlib.pyplot as plt
plt.savefig('04-p-pvalue2.pdf')

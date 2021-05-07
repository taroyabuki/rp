import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data

iris.boxplot('Sepal.Length',
             by='Species')

import matplotlib.pyplot as plt
plt.savefig('04-p-boxplot2.pdf')

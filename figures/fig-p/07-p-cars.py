import seaborn as sns
import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
sns.regplot(x='speed', y='dist', data=my_data)

import matplotlib.pyplot as plt
plt.savefig('07-p-cars.pdf')
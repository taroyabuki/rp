import matplotlib.pyplot as plt

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
#　speedがリストになっている点，解説が必要そう．
my_result = lr.fit(my_data[['speed']], my_data['dist'])
my_data['prediction'] = my_result.predict(my_data[['speed']])
my_data['residual'] = my_data['dist'] - my_data['prediction']

import numpy as np # 矢吹が補いました．
import matplotlib.pyplot as plt

plt.scatter(my_data['speed'], my_data['dist'], c='c', label='train')
plt.plot(my_data['speed'], my_data['prediction'], c='k', label='prediction')
for i in my_data.index:
    v = my_data.loc[i]
    plt.vlines(v['speed'], v['dist'], v['prediction'], colors='g', linestyles='dashed')
plt.xlabel('speed')
plt.ylabel('dist')
plt.legend()
plt.savefig('07-p-residual.pdf')
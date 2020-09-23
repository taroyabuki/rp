### 7.6.2 Pythonの場合

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
my_result = lr.fit(my_data[['speed']], my_data['dist'])
my_data['prediction'] = my_result.predict(my_data[['speed']])

my_data['residual'] = my_data['dist'] - my_data['prediction']
my_data.head()
#>    speed  dist  prediction   residual
#> 0      4     2   -1.849460   3.849460
#> 1      4    10   -1.849460  11.849460
#> 2      7     4    9.947766  -5.947766
#> 3      7    22    9.947766  12.052234
#> 4      8    16   13.880175   2.119825

# 残差計算の前にやってもいいのではないか？と思いました．
import matplotlib.pyplot as plt
plt.scatter(my_data['speed'], my_data['dist'], c='c', label='train')
plt.plot(my_data['speed'], my_data['prediction'], c='k', label='prediction')
for i in my_data.index:
    v = my_data.loc[i]
    plt.vlines(v['speed'], v['dist'], v['prediction'], colors='g', linestyles='dashed')
plt.xlabel('speed')
plt.ylabel('dist')
plt.legend()

(my_data['residual'] ** 2).mean()
# あるいは
from sklearn.metrics import mean_squared_error
mean_squared_error(my_data['dist'], my_data['prediction'])

#> 227.07042102189783


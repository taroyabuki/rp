import pandas as pd
my_data = pd.read_csv('https://raw.githubusercontent.com/taroyabuki/rp/master/data/an_wld_en.csv')
my_data.index = pd.to_datetime(my_data['year'], format='%Y')

# 移動平均
my_data['mean5'] = my_data.rolling(window=5).mean()['world']

# 回帰分析結果
from sklearn.linear_model import LinearRegression
X, y = my_data[['year']], my_data['world']
my_data['lm'] = LinearRegression().fit(X, y).predict(X)

my_data[['lm', 'mean5', 'world']].plot(style=['-', '-', 'o-'])
import matplotlib.pyplot as plt
plt.savefig('13-p-an-wld-en.pdf')
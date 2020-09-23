import pandas as pd
my_data = pd.read_csv('https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/an_wld_en.csv')
my_data.index = pd.to_datetime(my_data['year'], format='%Y')

my_train = my_data[:109] # 訓練データ
my_test  = my_data[-20:] # 検証データ

import matplotlib.pyplot as plt
plt.plot(my_train[['world']], label='train')
plt.plot(my_test[['world']], label='test')
plt.legend()
plt.savefig('13-p-train-test.pdf')
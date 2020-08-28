import pandas as pd
my_data = pd.read_csv('https://raw.githubusercontent.com/taroyabuki/rp/master/data/an_wld_en.csv')
my_data.index = pd.to_datetime(my_data['year'], format='%Y')

from pmdarima import auto_arima
my_model = auto_arima(my_data['world'])
y_, my_ci = my_model.predict(30,                   # 30年分の予測
                             return_conf_int=True) # 信頼区間を求める．

from datetime import datetime
my_df = pd.DataFrame({'world': y_,
                      'Lo': my_ci[:, 0],
                      'Hi': my_ci[:, 1]})
my_df.index=[datetime(y, 1, 1) for y in range(2020, 2050)]
my_df.head()

import matplotlib.pyplot as plt
plt.plot(my_data['world'])
plt.plot(my_df['world'])
plt.fill_between(my_df.index, my_df.Lo, my_df.Hi, color='k', alpha=0.25)
plt.savefig('13-p-an-wld-en-arima.pdf')
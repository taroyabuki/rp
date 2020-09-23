import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/tokyo-max-temp-2015--2019.csv'
my_data = pd.read_csv(my_url, encoding='sjis', skiprows=5, names=['month', 'tokyo', 'quality', 'no']) 

my_data.index = pd.to_datetime(my_data['month'], format='%Y/%m')

from pmdarima import auto_arima
my_model = auto_arima(my_data['tokyo'])

my_pred, my_ci = my_model.predict(24, return_conf_int=True)
my_df = pd.DataFrame({'tokyo': my_pred,
                      'Lo': my_ci[:, 0],
                      'Hi': my_ci[:, 1]})
my_df.index=pd.date_range('2020-01-01', '2021-12-01', freq='MS')

import matplotlib.pyplot as plt
plt.plot(my_data['tokyo'])
plt.plot(my_df['tokyo'])
plt.fill_between(my_df.index,
                 my_df.Lo,
                 my_df.Hi,
                 color='k',
                 alpha=0.25)
plt.savefig('13-p-tokyo.pdf')
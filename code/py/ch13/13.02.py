# 年の列（Aは年，Sはその初めを表す．）
pd.date_range('2020-01-01', '2025-01-01', freq='AS')
#> DatetimeIndex(['2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01',
#>                '2024-01-01', '2025-01-01'],
#>               dtype='datetime64[ns]', freq='AS-JAN')

# 年月の列（Mは月，Sはその初めを表す．）
pd.date_range('2020-01-01', '2020-05-01', freq='MS')
#> DatetimeIndex(['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01',
#>                '2020-05-01'],
#>               dtype='datetime64[ns]', freq='MS')

# 年月日の列
pd.date_range('2020-01-01', '2020-01-05', freq='D')
#> DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
#>                '2020-01-05'],
#>               dtype='datetime64[ns]', freq='D')

# 時の列
pd.date_range('2020-01-01 12:00:00', '2020-01-01 14:00:00', freq='H')
#> DatetimeIndex(['2020-01-01 12:00:00', '2020-01-01 13:00:00',
#>                '2020-01-01 14:00:00'],
#>               dtype='datetime64[ns]', freq='H')

import pandas as pd
my_data = pd.read_csv('an_wld_en.csv')
my_data.index = pd.to_datetime(my_data['year'], format='%Y')

import pandas as pd
my_data = pd.read_csv('an_wld_en.csv')
my_data.index = pd.to_datetime(my_data['year'], format='%Y')

# 移動平均
my_data['mean5'] = my_data.rolling(window=5).mean()['world']

# 回帰分析結果
from sklearn.linear_model import LinearRegression
X, y = my_data[['year']], my_data['world']
my_data['lm'] = LinearRegression().fit(X, y).predict(X)
my_data.head()
#>             year  world  mean5        lm
#> year
#> 1891-01-01  1891  -0.63    NaN -0.774702
#> 1892-01-01  1892  -0.71    NaN -0.767262
#> 1893-01-01  1893  -0.75    NaN -0.759822
#> 1894-01-01  1894  -0.70    NaN -0.752382
#> 1895-01-01  1895  -0.68 -0.694 -0.744941

my_data[['lm', 'mean5', 'world']].plot(style=['-', '-', 'o-'])


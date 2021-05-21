import pandas as pd
pd.to_datetime('2020-01-01')
#> Timestamp('2020-01-01 00:00:00')

pd.date_range(start='2021-01-01',
              end='2023-01-01',
              freq='1AS')
#> DatetimeIndex(['2021-01-01', '2022-01-01', '2023-01-01'],
#>               dtype='datetime64[ns]', freq='AS-JAN')

pd.date_range(start='2021-01-01',
              end='2021-03-01',
              freq='2MS')
#> DatetimeIndex(['2021-01-01', '2021-03-01'],
#>               dtype='datetime64[ns]', freq='2MS')

pd.date_range(start='2021-01-01',
              end='2021-01-03',
              freq='1D')
#> DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03'],
#>               dtype='datetime64[ns]', freq='D')

pd.date_range(start='2021-01-01 00:00:00',
              end='2021-01-01 03:00:00',
              freq='2H')
#> DatetimeIndex(['2021-01-01 00:00:00', '2021-01-01 02:00:00'],
#>               dtype='datetime64[ns]', freq='2H')


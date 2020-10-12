import pandas as pd
my_url = 'https://www.data.jma.go.jp/cpdinfo/temp/list/csv/an_wld.csv'
my_data = pd.read_csv(my_url, encoding='sjis') # 文字コードはShift_JIS
my_data.head()
#>       年  世界全体   北半球   南半球
#> 0  1891 -0.63 -0.68 -0.59
#> 1  1892 -0.71 -0.80 -0.62
#> 2  1893 -0.75 -0.87 -0.63
#> 3  1894 -0.70 -0.73 -0.68
#> 4  1895 -0.68 -0.75 -0.60

my_data = my_data.iloc[:129, 0:2] # 最初の129年分，年と世界全体の2列だけ残す．
my_data.columns = ['year', 'world']
my_data.to_csv('an_wld_en.csv', index=False)

my_data = pd.read_csv('an_wld_en.csv')
my_data.head()
#>    year  world
#> 0  1891  -0.63
#> 1  1892  -0.71
#> 2  1893  -0.75
#> 3  1894  -0.70
#> 4  1895  -0.68

my_data.query('1981 <= year <= 2010')[['world']].mean()
#> world    0.003667
#> dtype: float64

my_data = pd.read_csv('an_wld_en.csv')

from sklearn.linear_model import LinearRegression
X, y = my_data[['year']], my_data['world']
my_model = LinearRegression().fit(X, y)

[my_model.intercept_, my_model.coef_] # 係数
#> [-14.844194897883124, array([0.00744024])]


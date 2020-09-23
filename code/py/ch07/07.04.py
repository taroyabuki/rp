### 7.4.2 Pythonの場合

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
X, y = my_data[['speed']], my_data['dist'] # 入力変数（データフレーム）と出力変数（1次元データ）

from sklearn.linear_model import LinearRegression
my_model = LinearRegression() # 線形回帰分析
my_model.fit(X, y)            # 訓練

[my_model.intercept_, my_model.coef_] # 係数の確認
#> -17.579094890510973 [3.93240876]


import pandas as pd
from sklearn.preprocessing import StandardScaler
my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)
X, y = my_data.drop(columns=['LPRICE2']), my_data['LPRICE2']

# StandardScalerで標準化した結果をデータフレームに戻してから描画する．
pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns).boxplot()

my_model = Pipeline([
    ('sc', StandardScaler()),
    ('lm', LinearRegression())])
my_model.fit(X, y)

tmp = my_model.named_steps.lm
[tmp.intercept_, tmp.coef_]
[my_model.intercept_, my_model.coef_]
#> [-1.4517651851851847,  # (Intercept)
#>  array([ 0.14774133,   # WRAIN
#>          0.39872399,   # DEGREES
#>         -0.27680173,   # HRAIN
#>          0.19297881])] # TIME_SV

my_test = [[500, 17, 120, 2]]
my_model.predict(my_test)
#> array([-1.49884253])


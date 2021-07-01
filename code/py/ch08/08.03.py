## 8.3 標準化

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)
X, y = my_data.drop(columns=['LPRICE2']), my_data['LPRICE2']

# StandardScalerで標準化した結果をデータフレームに戻してから描画する．
pd.DataFrame(StandardScaler().fit_transform(X),
             columns=X.columns).boxplot(showmeans=True)

## 8.3 標準化

my_pipeline = Pipeline([
    ('sc', StandardScaler()),
    ('lr', LinearRegression())])
my_pipeline.fit(X, y)

## 8.3 標準化

# 線形回帰の部分だけを取り出す．
my_lr = my_pipeline.named_steps.lr
my_lr.intercept_
#> -1.4517651851851847

pd.Series(my_lr.coef_,
          index=X.columns)
#> WRAIN      0.147741
#> DEGREES    0.398724
#> HRAIN     -0.276802
#> TIME_SV    0.192979
#> dtype: float64

## 8.3 標準化

my_test = [[500, 17, 120, 2]]
my_model.predict(my_test)
#> array([-1.49884253])


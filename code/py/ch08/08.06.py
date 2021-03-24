import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet, enet_path
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore

my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)
X, y = my_data.drop(columns=['LPRICE2']), my_data['LPRICE2']

A = 2
B = 0.1

my_model = Pipeline([
    ('sc', StandardScaler()),
    ('enet', ElasticNet(
        alpha=A,
        l1_ratio=B))])
my_model.fit(X, y)

tmp = my_model.named_steps.enet
[tmp.intercept_, tmp.coef_]
#> [-1.4517651851851852,
#>  array([ 0.        ,   # WRAIN
#>          0.07410095,   # DEGREES
#>         -0.04115856,   # HRAIN
#>          0.02402688])] # TIME_SV

my_test = pd.DataFrame(
    [[500, 17, 120, 2]])
my_model.predict(my_test)
#> array([-1.41981616])

As = np.e**np.arange(
    2, -5.5, -0.1)
B = 0.1

_, my_path, _ = enet_path(
    zscore(X), zscore(y),
    alphas=As,
    l1_ratio=B)

pd.DataFrame(
    my_path.T,
    columns = X.columns,
    index = np.log(As)
).plot(
    xlabel='log A ( = log alpha)',
    ylabel='Coefficients')

As = np.linspace(0, 0.1, 21)
Bs = np.linspace(0, 0.1,  6)

my_pipeline = Pipeline([('sc', StandardScaler()),
                        ('enet', ElasticNet())])
my_search = GridSearchCV(
    estimator=my_pipeline,
    param_grid={'enet__alpha': As, 'enet__l1_ratio': Bs},
    cv=LeaveOneOut(),
    scoring='neg_mean_squared_error',
    n_jobs=-1).fit(X, y)
my_search.best_params_
#> {'enet__alpha': 0.075, 'enet__l1_ratio': 0.0}

my_model = my_search.best_estimator_ # 最良モデル

my_scores = (-my_search.cv_results_['mean_test_score'])**0.5

tmp = pd.DataFrame(
    my_scores.reshape(len(As), -1),
    index = As,
    columns = Bs.round(3))
tmp.plot(style='o-', xlabel='A ( = alpha)', ylabel='RMSE').legend(
    title='B ( = l1_ratio)')

y_ = my_model.predict(X)
mean_squared_error(y_, y)**0.5
#> 0.2627174747098049  # RMSE（訓練）

(-my_search.best_score_)**0.5
#> 0.31839530644830927 # RMSE（検証）

A = 2
B = 0.1

my_model = Pipeline([
    ('sc', StandardScaler()),
    ('enet', ElasticNet(
        alpha=A,
        l1_ratio=B))])
my_model.fit(X, zscore(y)) # 対策1

u = y.mean()
s = y.std(ddof=0)

my_test = pd.DataFrame(
    [[500, 17, 120, 2]])
my_model.predict(my_test) * s + u
#> array([-1.4347718])

tmp = my_model.named_steps.enet
[tmp.intercept_ - sum(
    tmp.coef_ * X.mean() /
    X.std(ddof=0)),
 tmp.coef_ / X.std(ddof=0)]
#> [-3.950668387804453,
#>  WRAIN      0.000000
#>  DEGREES    0.243667
#>  HRAIN     -0.001532
#>  TIME_SV    0.009727

[tmp.intercept_, tmp.coef_]
#> [6.39844527890396e-16,
#>  array([ 0.        ,   # WRAIN
#>          0.15761997,   # DEGREES
#>         -0.10983842,   # HRAIN
#>          0.07870943])] # TIME_SV


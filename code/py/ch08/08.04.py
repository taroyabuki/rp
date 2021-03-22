import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)

n = len(my_data)
my_data2 = my_data.assign(rand1=np.random.random(n), rand2=np.random.random(n))
my_data2.head()
#>    LPRICE2  WRAIN  DEGREES  HRAIN  TIME_SV     rand1     rand2
#> 0 -0.99868    600  17.1167    160       31  0.089076  0.877133
#> 1 -0.45440    690  16.7333     80       30  0.645344  0.397617
#> 2 -0.80796    502  17.1500    130       28  0.238390  0.238026
#> 3 -1.50926    420  16.1333    110       26  0.753152  0.951262
#> 4 -1.71655    582  16.4167    187       25  0.148555  0.866770

X, y = my_data2.drop(columns=['LPRICE2']), my_data2['LPRICE2']
my_model2 = LinearRegression().fit(X, y)

y_ = my_model2.predict(X)
mean_squared_error(y_, y)**0.5
#> 0.2530051445030606 # RMSE（訓練）

my_scores = cross_val_score(my_model2, X, y,
                            cv=len(y),                        # LOOCV           
                            scoring='neg_mean_squared_error') # MSE
(-my_scores.mean())**0.5
#> 0.35191104236501053 # RMSE（検証）


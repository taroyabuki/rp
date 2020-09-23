### 9.1.2 Pythonの場合

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
iris.head()
#>    Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
#> 0           5.1          3.5           1.4          0.2  setosa
#> 1           4.9          3.0           1.4          0.2  setosa
#> 2           4.7          3.2           1.3          0.2  setosa
#> 3           4.6          3.1           1.5          0.2  setosa
#> 4           5.0          3.6           1.4          0.2  setosa

iris.info()
#> <class 'pandas.core.frame.DataFrame'>
#> RangeIndex: 150 entries, 0 to 149
#> Data columns (total 5 columns):
#>  #   Column        Non-Null Count  Dtype
#> ---  ------        --------------  -----
#>  0   Sepal.Length  150 non-null    float64
#>  1   Sepal.Width   150 non-null    float64
#>  2   Petal.Length  150 non-null    float64
#>  3   Petal.Width   150 non-null    float64
#>  4   Species       150 non-null    object
#> dtypes: float64(4), object(1)
#> memory usage: 6.0+ KB


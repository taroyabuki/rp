### 3.8.1 よく遭遇するエラーとその対処方法

my_model = xgboost.XGBClassifier()
#> Traceback (most recent call last):
#>   File "<stdin>", line 1, in <module>
#> NameError: name 'xgboost' is not defined
# xgboostが定義されていないというエラーです．
# モジュールxgboostを読み込むことで対応します．

import xgboost
#> Traceback (most recent call last):
#>   File "<stdin>", line 1, in <module>
#> ModuleNotFoundError: No module named 'xgboost'
# xgboostというモジュールが見つからないというエラーです．
# xgboostをインストールすることで対応します．

# Jupyter Notebookなら次のとおりです．
!pip install xgboost

### 3.8.2 変数や関数についての調査

x = 123
type(x)
#> int

### 3.8.2 変数や関数についての調査

%whos
#> Variable   Type      Data/Info
#> ------------------------------
#> math       module    <module 'math' from '/opt<...>-38-x86_64-linux-gnu.so'>
#> x          int       123

### 3.8.2 変数や関数についての調査

import math
?math.log
# あるいは
help(math.log)

### 3.8.3 RのNA，Pythonのnan

import numpy as np
my_v = [1, np.nan, 3]
my_v
#> [1, nan, 3]

### 3.8.3 RのNA，Pythonのnan

np.isnan(my_v[1])
#> True

my_v[1] == np.nan # 誤り
#> False


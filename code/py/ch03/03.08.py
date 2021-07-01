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

x = 123
type(x)
#> int

%whos
#> Variable   Type      Data/Info
#> ------------------------------
#> math       module    <module 'math' from '/opt<...>-38-x86_64-linux-gnu.so'>
#> x          int       123

import math
?math.log
# あるいは
help(math.log)

import numpy as np
my_v = [1, np.nan, 3]
my_v
#> [1, nan, 3]

np.isnan(my_v[1])
#> True

my_v[1] == np.nan # 誤り
#> False


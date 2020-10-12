### 9.6.2 Pythonの場合

from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

my_model = Pipeline([('sc', StandardScaler()), # 標準化
                     ('mlp', MLPClassifier(max_iter=1000))])

# 収束に関する警告を非表示にする．
import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.simplefilter('ignore', ConvergenceWarning)

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

from sklearn.model_selection import *
my_cv = KFold(5) # 5分割交差検証
my_score = cross_validate(my_model, X, y,
                          cv=my_cv,
                          return_train_score=True)
my_score['test_score'].mean() # 正解率（検証）
#> 0.9266666666666667


### 9.6.2 Pythonの場合

from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

my_model = Pipeline([('sc', StandardScaler()), ('mlp', MLPClassifier())])
my_model.set_params(mlp__activation='logistic',
                    mlp__max_iter=50000)

# チューニングの設定（隠れ層のニューロン数：1, 3, 5）
params = {'mlp__hidden_layer_sizes': [(1, ), (3, ), (5, )]}

# 収束に関する警告を非表示にする．
import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.simplefilter('ignore', ConvergenceWarning)

# 割愛（データの読み込み，交差検証の設定，チューニングの実行）

my_search.best_params_ # 最良パラメータ
#> {'mlp__hidden_layer_sizes': (5,)}

my_search.best_score_ # 正解率（検証）
#> 0.9633333333333333


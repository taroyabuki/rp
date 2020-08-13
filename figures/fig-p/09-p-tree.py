import numpy
numpy.random.seed(0)

from sklearn import tree
my_model = tree.DecisionTreeClassifier(random_state=3)

# チューニングの設定
params = {'max_depth': range(3, 7), 'min_samples_leaf': range(1, 11)}

# データの読み込み
import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

from sklearn.model_selection import *
my_cv = RepeatedKFold(n_splits=5, n_repeats=10) # 5分割交差検証（10回）

my_search = GridSearchCV(my_model,
                         params,
                         cv=my_cv,
                         return_train_score=True, # 正解率（訓練）の保存
                         n_jobs=-1)               # 並列処理
my_search.fit(X, y) # 訓練

tree.plot_tree(my_search.best_estimator_, filled=True)
import matplotlib.pyplot as plt
plt.savefig('09-p-tree.pdf')
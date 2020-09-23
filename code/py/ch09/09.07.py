### 9.7.2 Pythonの場合

from sklearn import tree
my_model = tree.DecisionTreeClassifier()

# チューニングの設定
params = {'max_depth': range(3, 7),         # 木の深さの最大値（3から6）
          'min_samples_leaf': range(1, 11)} # 葉に該当するサンプルの最小数

# 割愛（データの読み込み，交差検証の設定，チューニングの実行）

my_search.best_params_ # 最良パラメータ
#> {'max_depth': 4, 'min_samples_leaf': 3}

my_search.best_score_ # 正解率（検証）
#> 0.9620000000000002

tree.plot_tree(my_search.best_estimator_, filled=True)


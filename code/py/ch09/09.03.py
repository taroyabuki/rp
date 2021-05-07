import pandas as pd
import statsmodels.api as sm
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, GridSearchCV, LeaveOneOut

my_data = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = my_data.iloc[:, 0:4], my_data.Species

my_model = tree.DecisionTreeClassifier(max_depth=2).fit(X, y)
y_ = my_model.predict(X)
confusion_matrix(y_true=y, y_pred=y_)
#> array([[50,  0,  0],
#>        [ 0, 49,  1],
#>        [ 0,  5, 45]])

my_model.score(X, y)
# あるいは
y_ = my_model.predict(X)
(y_ == y).mean()

#> 0.96

cross_val_score(my_model, X, y, cv=LeaveOneOut()).mean()
#> 0.9533333333333334

my_search = GridSearchCV(estimator=tree.DecisionTreeClassifier(),
                         param_grid={'max_depth':range(1, 11)},
                         cv=LeaveOneOut(),
                         n_jobs=-1).fit(X, y)
[my_search.best_params_, my_search.best_score_]
#> [{'max_depth': 2}, 0.9533333333333334]

my_params = {
    'max_depth':range(2, 6),
    'min_samples_split':[2, 20],
    'min_samples_leaf':range(1, 8)}

my_search = GridSearchCV(
    estimator=tree.DecisionTreeClassifier(min_impurity_decrease=0.01),
    param_grid=my_params,
    cv=LeaveOneOut(),
    n_jobs=-1).fit(X, y)
[my_search.best_params_, my_search.best_score_]
#> [{'max_depth': 3, 'min_samples_leaf': 5, 'min_samples_split': 2},
#>  0.9733333333333334]

tmp = my_search.cv_results_
my_results = pd.DataFrame(tmp['params']).assign(
    Accuracy = tmp['mean_test_score'])
my_results[my_results.Accuracy == my_results.Accuracy.max()] # 正解率（検証）の最大値
#>     max_depth  min_samples_leaf  min_samples_split  Accuracy
#> 22          3                 5                  2  0.973333
#> 23          3                 5                 20  0.973333
#> 36          4                 5                  2  0.973333
#> 37          4                 5                 20  0.973333
#> 50          5                 5                  2  0.973333
#> 51          5                 5                 20  0.973333

my_model = my_search.best_estimator_
my_dot = tree.export_graphviz(
    decision_tree=my_model,
    out_file=None,
    feature_names=X.columns,
    class_names=my_model.classes_,
    filled=True)
graphviz.Source(my_dot)


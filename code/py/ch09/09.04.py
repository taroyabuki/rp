import pandas as pd
import statsmodels.api as sm
import xgboost
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, LeaveOneOut

my_data = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = my_data.iloc[:, 0:4], my_data.Species

my_search = GridSearchCV(RandomForestClassifier(),
                         param_grid={'max_features':[2, 3, 4]},
                         cv=LeaveOneOut(),
                         n_jobs=-1).fit(X, y)
my_search.best_params_
#> {'max_features': 2}

my_search.cv_results_['mean_test_score']
#> array([0.96      , 0.96      , 0.95333333])

my_search = GridSearchCV(
    xgboost.XGBClassifier(),
    param_grid={'n_estimators'    :[50, 100, 150],
                'max_depth'       :[1, 2, 3],
                'learning_rate'   :[0.3, 0.4],
                'gamma'           :[0],
                'colsample_bytree':[0.6, 0.8],
                'min_child_weight':[1],
                'subsample'       :[0.5, 0.75, 1]},
    cv=LeaveOneOut(),
    n_jobs=1).fit(X, y) # n_jobs=-1ではない．
my_search.best_params_
#> {'colsample_bytree': 0.6,
#>  'learning_rate': 0.3,
#>  'max_depth': 1,
#>  'n_estimators': 50,
#>  'subsample': 0.5}

my_search.best_score_
#> 0.9533333333333334

my_model = RandomForestClassifier().fit(X, y)
tmp = pd.Series(my_model.feature_importances_, index=X.columns)
tmp.sort_values().plot(kind='barh')


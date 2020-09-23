import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

import xgboost as xgb
my_model = xgb.XGBClassifier().fit(X, y)

xgb.plot_importance(my_model) # 変数の重要度の可視化


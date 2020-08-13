import numpy
numpy.random.seed(0)

import xgboost as xgb
my_model = xgb.XGBClassifier()

# データの読み込み
import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

my_model.fit(X, y) # 訓練

import matplotlib.pyplot as plt
xgb.plot_importance(my_model)
plt.savefig('09-p-varimp.pdf')
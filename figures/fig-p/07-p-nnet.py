import matplotlib.pyplot as plt

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline

# Pipelineの説明が必要．
# パラメータの値はどうするか？（どう説明するか？）
my_model = Pipeline([('sc', StandardScaler()), ('mlp', MLPRegressor())])
my_model.set_params(mlp__hidden_layer_sizes=(3, ),
                    mlp__activation='logistic',
                    mlp__max_iter=50000)

# 手動でパラメータ調整しましたが，5万を超えるとちょっと時間がかかりすぎかなという気がしたので，この辺でやめておきます．
my_model.fit(my_data[['speed']], my_data['dist'])

# scaler.inverse_transformを使うべきか・・・
import numpy as np
tmp = np.linspace(my_data['speed'].min(), my_data['speed'].max(), num=100)
# 2行にわけてもよいかも．
y_ = my_model.predict(tmp[:, np.newaxis])
plt.scatter(my_data['speed'], my_data['dist'], c='c', label='train')
plt.plot(tmp, y_, c='k', label='prediction')
plt.xlabel('speed')
plt.ylabel('dist')
plt.legend()
plt.savefig('07-p-nnet.pdf')
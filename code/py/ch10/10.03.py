### 10.3.2 Pythonの場合

import pandas as pd
my_data = pd.DataFrame({
  'answer': [  0,   1,   1,   0,   1,   0,    1,   0,   0,   1],  # 正解
  'prob':   [0.7, 0.8, 0.3, 0.4, 0.9, 0.6, 0.99, 0.1, 0.2, 0.5]}) # 陽性確率

from sklearn.metrics import roc_curve
fpr, tpr, _ = roc_curve(my_data.answer, my_data.prob)

import matplotlib.pyplot as plt
plt.plot(fpr, tpr)
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')

from sklearn.metrics import auc
auc(fpr, tpr)
#> 0.8


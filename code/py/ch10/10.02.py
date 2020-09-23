import pandas as pd
my_data = pd.DataFrame({
  'answer': [  0,   1,   1,   0,   1,   0,    1,   0,   0,   1],  # 正解
  'prob':   [0.7, 0.8, 0.3, 0.4, 0.9, 0.6, 0.99, 0.1, 0.2, 0.5]}) # 陽性確率

my_pred = [1 if p >= 0.5 else 0 for p in my_data.prob]
my_pred
#> [1, 1, 0, 0, 1, 1, 1, 0, 0, 1]

from sklearn.metrics import confusion_matrix
confusion_matrix(my_pred, my_data.answer) # Rの仕様に合わせる．
#> array([[3, 1],
#>        [2, 4]])

from sklearn.metrics import classification_report
print(classification_report(my_data.answer, my_pred))
#>               precision    recall  f1-score   support
#> 
#>            0       0.75      0.60      0.67         5
#>            1       0.67      0.80      0.73         5
#> 
#>     accuracy                           0.70        10
#>    macro avg       0.71      0.70      0.70        10
#> weighted avg       0.71      0.70      0.70        10


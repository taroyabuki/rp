import numpy
numpy.random.seed(0)

import pandas as pd
my_data = pd.read_csv('https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/titanic.csv')
X, y = pd.get_dummies(my_data.iloc[:,0:3], drop_first=True), my_data.Survived

from sklearn import tree
my_model = tree.DecisionTreeClassifier(max_depth=3)
my_model.fit(X, y)

tree.plot_tree(my_model, filled=True)
import matplotlib.pyplot as plt
plt.savefig('10-p-titanic.pdf')
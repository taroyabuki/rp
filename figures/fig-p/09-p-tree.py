import numpy
numpy.random.seed(0)

import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
X, y = iris.iloc[:, 0:4], iris.Species

from sklearn import tree
my_model = tree.DecisionTreeClassifier(random_state=3)

my_model.fit(X, y)
tree.plot_tree(my_model, filled=True)
import matplotlib.pyplot as plt
plt.savefig('09-p-tree.pdf')
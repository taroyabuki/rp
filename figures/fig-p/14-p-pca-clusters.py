# アヤメのデータ
import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data
my_data = iris.iloc[:, 0:4]

# 階層的クラスター分析
#from scipy.cluster import hierarchy
#my_hc = hierarchy.linkage(my_data)
#my_data.index = hierarchy.cut_tree(my_hc, 3)[:,0] # 結果の保存

# 非階層的クラスター分析
from sklearn.cluster import KMeans
my_data.index = KMeans(n_clusters=3).fit(my_data).labels_ # 結果の保存

# 主成分分析
from pca import pca
my_model = pca(n_components=4)
my_result = my_model.fit_transform(my_data)

# バイプロット
my_model.biplot()

import matplotlib.pyplot as plt
plt.savefig('14-p-pca-clusters.pdf')

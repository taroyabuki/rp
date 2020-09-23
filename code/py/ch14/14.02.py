import pandas as pd
my_data = pd.DataFrame(
    {'x': [0, -16, 10, 10],
     'y': [0, 0, 10, -15]},
    index=['A', 'B', 'C', 'D'])

from scipy.spatial import distance

# ユークリッド距離
distance.cdist(my_data, my_data)
# あるいは
distance.cdist(my_data, my_data, metric='euclidean')
#> array([[ 0.        , 16.        , 14.14213562, 18.02775638],
#>        [16.        ,  0.        , 27.85677655, 30.01666204],
#>        [14.14213562, 27.85677655,  0.        , 25.        ],
#>        [18.02775638, 30.01666204, 25.        ,  0.        ]])

# マンハッタン距離
distance.cdist(my_data, my_data, metric='cityblock')
#> array([[ 0., 16., 20., 25.],
#>        [16.,  0., 36., 41.],
#>        [20., 36.,  0., 25.],
#>        [25., 41., 25.,  0.]])

#### 14.2.2.2 Pythonの場合

import pandas as pd
my_data = pd.DataFrame(
    {'x': [0, -16, 10, 10],
     'y': [0, 0, 10, -15]},
    index=['A', 'B', 'C', 'D'])

# クラスター分析
from scipy.cluster import hierarchy
my_result = hierarchy.linkage(my_data)
# あるいは
my_result = hierarchy.linkage(my_data, metric='euclidean', method='complete')

# デンドログラムの描画
hierarchy.dendrogram(my_result, labels=my_data.index)

# クラスター数を3にする場合に，各点がどのクラスターに属しているかを確認する．
hierarchy.cut_tree(my_result, 3)
#> array([[0],
#>        [1],
#>        [0],
#>        [2]])

#### 14.2.3.2 Pythonの場合

import pandas as pd
my_data = pd.DataFrame(
    {'language': (  0, 20, 20, 25, 22, 17),
     'english':  (  0, 20, 40, 20, 24, 18),
     'math':     (100, 20,  5, 30, 17, 25),
     'science':  (  0, 20,  5, 25, 16, 23),
     'society':  (  0, 20, 30,  0, 21, 17)},
    index=['A', 'B', 'C', 'D', 'E', 'F'])

import seaborn as sns
sns.clustermap(my_data,
               z_score=1, # 列ごとの標準化
               metric='euclidean',
               method='complete')

#### 14.2.4.2 Pythonの場合

import pandas as pd
my_data = pd.DataFrame(
    {'x': [0, -16, 10, 10],
     'y': [0, 0, 10, -15]},
    index=['A', 'B', 'C', 'D'])

# クラスター数を3として，非階層的クラスター分析を行う．
from sklearn.cluster import KMeans
my_result = KMeans(n_clusters=3).fit(my_data)

# 各データがどのクラスターに属しているかを確認する．
my_result.labels_
#> array([1, 0, 1, 2], dtype=int32)

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


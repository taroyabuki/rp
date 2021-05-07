import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data

import pandas as pd
my_df = pd.DataFrame({
    'Species':iris.Species,
    'w_Sepal':iris['Sepal.Width'] > 3})

my_table = pd.crosstab(
    my_df['Species'],
    my_df['w_Sepal'])

from statsmodels.graphics.mosaicplot \
import mosaic

my_table.columns = [str(x) for x in my_table.columns]
my_table.index   = [str(x) for x in my_table.index]
mosaic(my_df, index=['Species', 'w_Sepal'], labelizer=lambda k: my_table.loc[k])

import matplotlib.pyplot as plt
plt.savefig('04-p-mosaic2.pdf')
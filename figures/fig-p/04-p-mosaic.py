import statsmodels.api as sm
iris = sm.datasets.get_rdataset('iris', 'datasets').data

import pandas as pd
my_df = pd.DataFrame({
    'Species':iris.Species,
    'w_Sepal':iris['Sepal.Width'] > 3})

from statsmodels.graphics.mosaicplot \
import mosaic

mosaic(my_df, index=['Species', 'w_Sepal'])

import matplotlib.pyplot as plt
plt.savefig('04-p-mosaic.pdf')
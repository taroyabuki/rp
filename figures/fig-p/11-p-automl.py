import h2o
import numpy as np
import pandas as pd
from h2o.automl import H2OAutoML

h2o.init()
h2o.no_progress()

import statsmodels.api as sm
my_data = sm.datasets.get_rdataset('cars', 'datasets').data
my_frame = h2o.H2OFrame(my_data)

y = 'dist'

my_model = H2OAutoML(max_runtime_secs=30)
my_model.train(y=y, training_frame=my_frame)

print(my_model.leaderboard.head(rows=6))

tmp = pd.DataFrame({'speed':np.linspace(min(my_data.speed),
                                        max(my_data.speed),
                                        100)})
my_pred = my_model.predict(h2o.H2OFrame(tmp))
tmp['model'] = my_pred['predict'].as_data_frame()

pd.concat([my_data, tmp]).plot(
  x='speed', style=['o', '-'])

h2o.cluster().shutdown()

import matplotlib.pyplot as plt
plt.savefig('11-p-automl.pdf')

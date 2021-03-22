import pandas as pd
my_url = 'http://www.liquidasset.com/winedata.html'
tmp = pd.read_table(my_url, skiprows=62, nrows=38, sep='\s+', na_values='.')
tmp.describe()
#>              OBS         VINT    LPRICE2       WRAIN    DEGREES       HRAIN    TIME_SV
#> count  38.000000    38.000000  27.000000   38.000000  37.000000   38.000000  38.000000
#> mean   19.500000  1970.500000  -1.451765  605.000000  16.522973  137.000000  12.500000
#> std    11.113055    11.113055   0.634588  135.283087   0.662480   66.740725  11.113055
#> min     1.000000  1952.000000  -2.288790  376.000000  14.983300   38.000000  -6.000000
#> 25%    10.250000  1961.250000  -1.985365  510.250000  16.166700   87.500000   3.250000
#> 50%    19.500000  1970.500000  -1.509260  586.500000  16.533300  120.500000  12.500000
#> 75%    28.750000  1979.750000  -1.052200  713.500000  17.066700  171.000000  21.750000
#> max    38.000000  1989.000000   0.000000  845.000000  17.650000  292.000000  31.000000

my_data = tmp.iloc[:, 2:].dropna()
my_data.head()
#>    LPRICE2  WRAIN  DEGREES  HRAIN  TIME_SV
#> 0 -0.99868    600  17.1167    160       31
#> 1 -0.45440    690  16.7333     80       30
#> 3 -0.80796    502  17.1500    130       28
#> 5 -1.50926    420  16.1333    110       26
#> 6 -1.71655    582  16.4167    187       25

len(my_data)
#> 27

my_data.to_csv('wine.csv',
               index=False)

import pandas as pd
#my_data = pd.read_csv('wine.csv') # 作ったファイルを使う場合
my_url = ('https://raw.githubusercontent.com'
          '/taroyabuki/fromzero/master/data/wine.csv')
my_data = pd.read_csv(my_url)


import pandas as pd
my_df = pd.read_csv('exam.csv')
my_df
#>   name  english  math gender
#> 0    A       60    70      f
#> 1    B       90    80      m
#> 2    C       70    90      m
#> 3    D       90   100      f

my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/exam.csv'
my_df = pd.read_csv(my_url)

import pandas as pd
my_df2 = pd.read_csv('exam.csv',
    index_col='name')
my_df2
#>       english  math gender
#> name
#> A          60    70      f
#> B          90    80      m
#> C          70    90      m
#> D          90   100      f

my_df.to_csv('exam2.csv',
    index=False) # 行名を出力しない．

my_df2.to_csv('exam3.csv')

import pandas as pd
my_df = pd.read_csv('exam.csv',
    encoding='UTF-8')

my_df.to_csv('exam2.csv', index=False, encoding='UTF-8')

import pandas as pd
my_url = 'https://github.com/taroyabuki/rp/blob/master/data/exam.csv'
my_tables = pd.read_html(my_url)

#> [   Unnamed: 0 name  english  math gender
#>  0         NaN    A       60    70      f
#>  1         NaN    B       90    80      m
#>  2         NaN    C       70    90      m
#>  3         NaN    D       90   100      f]

my_tables[0]
#>    Unnamed: 0 name  english  math gender
#> 0         NaN    A       60    70      f
#> 1         NaN    B       90    80      m
#> 2         NaN    C       70    90      m
#> 3         NaN    D       90   100      f

# 1列目以降を取り出す．
my_data = my_tables[0].iloc[:, 1:]
my_data
#>   name  english  math gender
#> 0    A       60    70      f
#> 1    B       90    80      m
#> 2    C       70    90      m
#> 3    D       90   100      f


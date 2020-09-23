import pandas as pd

my_df = pd.DataFrame({
    'name':    ['A', 'B', 'C', 'D'],
    'english': [ 60,  90,  70,  90],
    'math':    [ 70,  80,  90, 100],
    'gender':  ['f', 'm', 'm', 'f']})

my_df = pd.DataFrame([
    ['A', 60, 70, 'f'],
    ['B', 90, 80, 'm'],
    ['C', 70, 90, 'm'],
    ['D', 90, 100, 'f']],
    columns=['name', 'english',
             'math', 'gender'])

import itertools
import pandas as pd
my_df2 = pd.DataFrame(
    itertools.product([1, 2, 3],
                      [10, 100]),
    columns=['X', 'Y'])
my_df2
#>    X    Y
#> 0  1   10
#> 1  1  100
#> 2  2   10
#> 3  2  100
#> 4  3   10
#> 5  3  100

my_df.columns
#> Index(['name', 'english', 'math', 'gender'], dtype='object')

my_df.columns = ['NAME', 'ENGLISH', 'MATH', 'GENDER']
# あるいは
my_df.columns = pd.Series(my_df.columns).apply(str.upper)

my_df
#>   NAME  ENGLISH  MATH GENDER
#> 0    A       60    70      f
#> 1    B       90    80      m
# 以下略

my_df.columns = pd.Series(my_df.columns).apply(str.lower) # 元に戻す．

my_df2 = pd.DataFrame({
    'english': [ 60,  90,  70,  90],
    'math':    [ 70,  80,  90, 100],
    'gender':  ['f', 'm', 'm', 'f']},
    index=     ['A', 'B', 'C', 'D'])
my_df2
#>    english  math gender
#> A       60    70      f
#> B       90    80      m
#> C       70    90      m
#> D       90   100      f

tmp = pd.DataFrame({
    'name':['E'],
    'english': [80],
    'math': [80],
    'gender': ['m']})
pd.concat([my_df, tmp])

my_df.assign(id=[1, 2, 3, 4])

my_df['id'] = [1, 2, 3, 4]

my_df['english']
#> 0    60
#> 1    90
#> 2    70
#> 3    90
#> Name: english, dtype: int64

my_df[['name', 'math']]

my_df.iloc[:, [0, 2]]

my_df.iloc[[0, 2], :]

my_df[my_df['gender'] == 'm']

my_df.query('english > 80 and gender == "m"')

my_df[my_df['english'] == my_df['english'].max()]

my_df.sort_values('english')

my_df.sort_values('english', ascending=False)


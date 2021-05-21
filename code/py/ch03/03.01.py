2 * 3
#> 6

10 / 3
#> 0.3333333333333333

10 // 3 # 商
#> 3

10 % 3 # 余り
#> 1

0.1 + 0.1 + 0.1 == 0.3
#> False

import numpy as np
np.isclose(0.1 + 0.1 + 0.1, 0.3)
#> True

x = 2
y = 3
x * y
#> 6

x, y = 20, 30 # まとめて名付け
x * y
#> 600

x = 1 + 1
# この段階では結果は表示されない

x # 変数名
#> 2

my_s = 'abcde'

len(my_s)
#> 5

'This is ' + 'a' + ' pen.'
#> 'This is a pen.'

my_s[1:4]
#> 'bcd'

my_t = "{} is {}."
my_t.format('This', 'a pen')
#> 'This is a pen.'

1 <= 2
#> True

1 < 0
#> False

True and False # 論理積（かつ）
#> False

True or False # 論理和（または）
#> True

not True      # 否定（でない）
#> False

0 if 3 < 5 else 10
#> 0

%pwd
# あるいは
import os
os.getcwd()
#> '/home/jovyan/work'

%cd fromzero
# あるいは
os.chdir('fromzero')

os.getcwd()
#> '/home/jovyan/work/fromzero'


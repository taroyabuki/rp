import math
math.sqrt(4)
# あるいは
4**0.5

#> 2.0

math.log(100, 10)
#> 2.0

math.log(100) # 自然対数
あるいは
math.log(100, math.e) # 省略しない場合

#> 4.605170185988092

import math
math.log10(100) # 常用対数
#> 2.0

math.log2(1024)
#> 10.0

def my_f(a, b):
    return a - b

my_f(3, 5)
#> -2

def my_f(a, b=5):
    return a - b

my_f(3) # my_f(3, 5)と同じこと
#> -2

(lambda a, b: a - b)(3, 5)
#> -2


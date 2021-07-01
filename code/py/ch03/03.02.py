import math
math.sqrt(4)
#> 2.0

math.log(100, 10)
#> 2.0

math.log(100)         # 自然対数
# あるいは
math.log(100, math.e) # 省略しない場合

#> 4.605170185988092

math.log10(100) # 常用対数
#> 2.0

math.log2(1024) # 底が2の対数
#> 10.0

def f(a, b):
    return a - b

f(3, 5)
#> -2

def f(a, b=5):
    return a - b

f(3) # f(3, 5)と同じこと
#> -2

(lambda a, b: a - b)(3, 5)
#> -2


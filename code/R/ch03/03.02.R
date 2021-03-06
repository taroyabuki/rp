## 3.2 関数

### 3.2.1 関数の利用

sqrt(4)
#> [1] 2

log(100, 10)
#> [1] 2

log(100)         # 自然対数
# あるいは
log(100, exp(1)) # 省略しない場合

#> [1] 4.60517

log10(100) # 常用対数
#> [1] 2

log2(1024) # 底が2の対数
#> [1] 10

#### 3.2.1.1 パイプ（Rのみ）

library(tidyverse)
4 %>% sqrt

exp(log(5))          # 通常の書き方
# あるいは
5 %>% log %>% exp    # パイプを使う書き方

#> 5

### 3.2.2 関数の定義

f <- function(a, b) {
  a - b
}

f(3, 5)
#> [1] -2

#### 3.2.2.1 デフォルト引数

f <- function(a, b = 5) {
  a - b
}

f(3) # f(3, 5)と同じこと
#> [1] -2

#### 3.2.2.2 無名関数

(function(a, b) { a - b })(3, 5)
#> [1] -2


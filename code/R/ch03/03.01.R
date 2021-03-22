### 3.1.1 数値

2 * 3
#> [1] 6

10 / 3
#> [1] 0.3333333

10 %/% 3 # 商
#> [1] 3

10 %% 3 # 余り
#> [1] 1

0.1 + 0.1 + 0.1 == 0.3
#> [1] FALSE

all.equal(0.1 + 0.1 + 0.1, 0.3)
#> [1] TRUE

### 3.1.2 変数

x <- 2
y <- 3
x * y
#> [1] 6

library(keras)
c(x, y) %<-% c(20, 30) # まとめて名付け
x * y
#> [1] 600

my_x <- 2
my_y <- 3
my_x * my_y
#> [1] 6

x <- 1 + 1
# この段階では結果は表示されない

x # 変数名
#> [1] 2

### 3.1.3 文字列

my_s <- "abcde"

nchar(my_s)
#> [1] 5

library(tidyverse)
str_c("This is ", "a", " pen.")
#> [1] "This is a pen."

substr(x = my_s,
       start = 2, stop = 4)
#> [1] "bcd"

my_t <- "%s is %s."
sprintf(my_t, "This", "a pen")
#> [1] "This is a pen."

### 3.1.4 論理値

1 <= 2
#> [1] TRUE

1 < 0
#> [1] FALSE

TRUE & FALSE # 論理積（かつ）
#> [1] FALSE

TRUE | FALSE # 論理和（または）
#> [1] TRUE

!TRUE # 否定（でない）
#> [1] FALSE

### 3.1.5 作業ディレクトリ

getwd()
#> '/home/jovyan/work'

setwd("fromzero")
getwd()
#> '/home/jovyan/work/fromzero'


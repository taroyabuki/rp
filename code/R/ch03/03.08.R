## 3.8 反復処理

library(furrr)
plan(multisession)

### 3.8.1 1次元データ→1次元データ

my_f1 <- function(x) {
  tmp <- runif(x)
  mean(tmp)
}

my_f1(10) # 動作確認
#> [1] 0.5776604 （結果の例）

my_v <- c(5, 10, 100)
my_v %>% map_dbl(my_f1)
#> [1] 0.4857329 0.5322183 0.5084124

### 3.8.2 1次元データ→データフレーム

my_f2 <- function(n) {
  tmp = runif(n)
  list(x = n,
       p = mean(tmp),
       q = sd(tmp))
}

my_f2(10) # 動作確認
#> $x
#> [1] 10
#> 
#> $p
#> [1] 0.6840032 （平均の例）
#> 
#> $q
#> [1] 0.3750788 （標準偏差の例）

my_v <- c(5, 10, 100)
my_v %>% map_dfr(my_f2)
#>       x     p     q
#>   <dbl> <dbl> <dbl>
#> 1     5 0.560 0.320
#> 2    10 0.559 0.271
#> 3   100 0.507 0.283

### 3.8.3 データフレーム→データフレーム

my_f3 = function(x, y) {
  tmp <- runif(x, min = 1,
                  max = y + 1) %>%
    as.integer
  list(x = x,
       y = y,
       p = mean(tmp),
       q = sd(tmp))
}

my_f3(x = 10, y = 6) # 動作確認
#> $x
#> [1] 10
#> 
#> $y
#> [1] 6
#> 
#> $p
#> [1] 3.2 （平均の例）
#> 
#> $q
#> [1] 1.316561 （標準偏差の例）

my_df = data.frame(
  x = c(5, 10, 100, 5, 10, 100),
  y = c(6, 6, 6, 12, 12, 12))

my_df %>% pmap_dfr(my_f3)
#>       x     y     p     q
#>   <dbl> <dbl> <dbl> <dbl>
#> 1     5     6  3     1.41
#> 2    10     6  3     1.49
#> 3   100     6  3.57  1.78
#> 4     5    12  7.6   5.22
#> 5    10    12  5.7   3.77
#> 6   100    12  6.36  3.59

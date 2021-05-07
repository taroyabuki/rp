### 3.4.1 データフレームの作成

library(tidyverse)

#### 3.4.1.1 データを列ごとに記述する方法

my_df <- data.frame(
  name    = c("A", "B", "C", "D"),
  english = c( 60,  90,  70,  90),
  math    = c( 70,  80,  90, 100),
  gender  = c("f", "m", "m", "f"))

#### 3.4.1.2 データを行ごとに記述する方法

my_df <- tribble(
  ~name, ~english, ~math, ~gender,
  "A",         60,    70,     "f",
  "B",         90,    80,     "m",
  "C",         70,    90,     "m",
  "D",         90,   100,     "f")

#### 3.4.1.3 データフレームのサイズ

dim(my_df)  # 行数と列数
[1] 4 4

nrow(my_df) # 行数
[1] 4

ncol(my_df) # 列数
[1] 4

#### 3.4.1.4 組合せ

my_df2 <- expand.grid(
  X = c(1, 2, 3),
  Y = c(10, 100))
my_df2
#>   X   Y
#> 1 1  10
#> 2 2  10
#> 3 3  10
#> 4 1 100
#> 5 2 100
#> 6 3 100

#### 3.4.1.5 列と行の名前

colnames(my_df2)
#> [1] "P" "Q"

colnames(my_df2) <- c("P", "Q")
my_df2
#>   P   Q
#> 1 1  10
#> 2 2  10
# 以下略

row.names(my_df)
#> [1] "1" "2" "3" "4"

row.names(my_df2) <-
  c("a", "b", "c", "d", "e", "f")
my_df2
#>   P   Q
#> a 1  10
#> b 2  10
#> c 3  10
# 以下略

my_df3 <- data.frame(
  english =   c( 60,  90,  70,  90),
  math    =   c( 70,  80,  90, 100),
  gender  =   c("f", "m", "m", "f"),
  row.names = c("A", "B", "C", "D"))
my_df3
#>   english math gender
#> A      60   70      f
#> B      90   80      m
#> C      70   90      m
#> D      90  100      f

#### 3.4.2.1 行の追加（データフレームの結合）

tmp <- data.frame(
  name = "E",
  english = 80,
  math = 80,
  gender = "m")
rbind(my_df, tmp)

#### 3.4.2.2 列の追加

my_df %>% mutate(id = c(1, 2, 3, 4))

my_df["id"] <- c(1, 2, 3, 4)

#### 3.4.3.1 1列の取り出し（結果は1次元データ）

my_df[, 2]         # 参照
# あるいは
my_df$english      # 参照
# あるいは
my_df$"english"    # 参照
# あるいは
my_df[["english"]] # 参照
# あるいは
tmp <- "english"
my_df[[tmp]]       # 参照

#> [1] 60 90 70 90

#### 3.4.3.2 複数列の取り出し（結果はデータフレーム）

my_df %>% select(name, math)

my_df[, c(1, 3)] # 参照

my_df %>% select(-c(english, gender))
# あるいは
my_df[, -c(2, 4)] # 参照

#### 3.4.3.3 複数行の取り出し（結果はデータフレーム）

my_df[c(1, 3), ] # 参照

my_df[-c(2, 4), ] # 参照

#### 3.4.3.4 検索

my_df[my_df$gender == "m", ] # 参照
# あるいは
my_df %>% filter(gender == "m")

my_df[my_df$english > 80 & my_df$gender == "m", ] # 参照
# あるいは
my_df %>% filter(english > 80 & gender == "m")

my_df[my_df$english == max(my_df$english), ] # 参照
# あるいは
my_df %>% filter(english == max(my_df$english))

#### 3.4.3.5 並べ替え

my_df %>% arrange(english)

my_df %>% arrange(-english)

#### 3.4.4.1 行列の生成

x = c(2, 3, 5, 7, 11, 13,
      17, 19, 23, 29, 31, 37)
A <- matrix(
  data = x,     # 1次元データ
  nrow = 3,     # 行数
  byrow = TRUE) # 行ごとの生成
A
#>      [,1] [,2] [,3] [,4]
#> [1,]    2    3    5    7
#> [2,]   11   13   17   19
#> [3,]   23   29   31   37

#### 3.4.4.2 データフレームと行列

my_df[, c(2, 3)] %>% as.matrix
#>      english math
#> [1,]      60   70
#> [2,]      90   80
#> [3,]      70   90
#> [4,]      90  100

as.data.frame(A)
#>   english math
#> 1      60   70
#> 2      90   80
#> 3      70   90
#> 4      90  100

#### 3.4.4.3 行列の変形

t(A)
#>      [,1] [,2] [,3]
#> [1,]    2   11   23
#> [2,]    3   13   29
#> [3,]    5   17   31
#> [4,]    7   19   37

#### 3.4.4.4 行列の積

t(A) %*% A
#>      [,1] [,2] [,3] [,4]
#> [1,]  654  816  910 1074
#> [2,]  816 1019 1135 1341
#> [3,]  910 1135 1275 1505
#> [4,] 1074 1341 1505 1779

### 3.4.5 縦型と横型

library(tidyverse)

my_wider <- data.frame(
  day = c(25, 26, 27),
  min = c(20, 21, 15),
  max = c(24, 27, 21))

my_longer <- my_wider %>%
  pivot_longer(-day)
my_longer
#> # A tibble: 6 x 3
#>     day name  value
#>   <dbl> <chr> <dbl>
#> 1    25 min      20
#> 2    25 max      24
#> 3    26 min      21
#> 4    26 max      27
#> 5    27 min      15
#> 6    27 max      21

my_longer %>% pivot_wider()
#> # A tibble: 3 x 3
#>     day   min   max
#>   <dbl> <dbl> <dbl>
#> 1    25    20    24
#> 2    26    21    27
#> 3    27    15    21

my_longer %>%
  ggplot(aes(x = day, y = value,
             color = name)) +
  geom_point() +
  geom_line() +
  ylab("temperature") +
  scale_x_continuous(
    breaks = my_longer$day)


## 3.5 データフレーム

library(tidyverse)

#### 3.5.1.1 データを列ごとに記述する方法

my_df <- data.frame(
  name    = c("A", "B", "C", "D"),
  english = c( 60,  90,  70,  90),
  math    = c( 70,  80,  90, 100),
  gender  = c("f", "m", "m", "f"))

#### 3.5.1.2 データを行ごとに記述する方法

my_df <- tribble(
  ~name, ~english, ~math, ~gender,
  "A",         60,    70,     "f",
  "B",         90,    80,     "m",
  "C",         70,    90,     "m",
  "D",         90,   100,     "f")

#### 3.5.1.3 組合せ

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

#### 3.5.1.4 列と行の名前

colnames(my_df)
#> [1] "name"    "english" "math"    "gender" 

colnames(my_df) <- c("NAME", "ENGLISH", "MATH", "GENDER")
# あるいは
colnames(my_df) = toupper(colnames(my_df))

my_df
#>   NAME  ENGLISH  MATH GENDER
#>   <chr>   <dbl> <dbl> <chr> 
#> 1 A          60    70 f    
#> 2 B          90    80 m     
# 以下略

colnames(my_df) = tolower(colnames(my_df)) # 元に戻す．

my_df2 <- data.frame(
  english =   c( 60,  90,  70,  90),
  math    =   c( 70,  80,  90, 100),
  gender  =   c("f", "m", "m", "f"),
  row.names = c("A", "B", "C", "D"))
my_df2
#>   english math gender
#> A      60   70      f
#> B      90   80      m
#> C      70   90      m
#> D      90  100      f

#### 3.5.2.1 行の追加

tmp <- data.frame(
  name = "E",
  english = 80,
  math = 80,
  gender = "m")
rbind(my_df, tmp)

#### 3.5.2.2 列の追加

my_df %>% mutate(id = c(1, 2, 3, 4))

my_df["id"] <- c(1, 2, 3, 4)

#### 3.5.3.1 1列の取り出し（結果は1次元データ）

my_df$english
# あるいは
my_df[["english"]]
#> [1] 60 90 70 90

#### 3.5.3.2 複数列の取り出し（結果はデータフレーム）

my_df %>% select(name, math)

my_df[, c(1, 3)]

my_df[, -c(2, 4)]

#### 3.5.3.3 複数行の取り出し（結果はデータフレーム）

my_df[c(1, 3), ]

my_df[-c(2, 4), ]

#### 3.5.3.4 検索

my_df %>% filter(gender == "m")

my_df %>% filter(english > 80 & gender == "m")

my_df %>% filter(english == max(my_df$english))

#### 3.5.3.5 並べ替え

my_df %>% arrange(english)

my_df %>% arrange(-english)


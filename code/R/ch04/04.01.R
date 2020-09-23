### 4.1.1 平均・分散・標準偏差

x <- c(165, 170, 175, 180, 185)

mean(x) # 平均（その1）
#> [1] 175

sum(x) / length(x) # 平均（その2）
#> [1] 175

x - mean(x)
#> [1] -10  -5   0   5  10

mean(x - mean(x))
#> [1] 0

mean((x - mean(x))^2)
#> [1] 50

sqrt(mean((x - mean(x))^2))
#> [1] 7.071068

y <- c(173, 174, 175, 176, 177)

mean(y)
#> [1] 175 # 平均

sqrt(mean((y - mean(y))^2))
#> [1] 1.414214 # 標準偏差

var(x) # 分散
#> [1] 62.5

sd(x) # 標準偏差
#> [1] 7.905694

var(x) # 不偏分散
#> [1] 62.5

sd(x) # 平方根
#> [1] 7.905694

n <- length(x)
var(x) * (n - 1) / n # 不偏でない分散
#> [1] 50

sd(x) * sqrt((n - 1) / n) # 平方根
#> [1] 7.071068

psych::describe(x)
#>    vars n mean   sd ...
#> X1    1 5  175 7.91 ...

x <- 1:9
quantile(x)
#>   0%  25%  50%  75% 100% 
#>    1    3    5    7    9 

my_df <- data.frame(
  english = c( 60,  90,  70,  90),
  math    = c( 70,  80,  90, 100))
psych::describe(my_df)

#>         vars n mean    sd ...
#> english    1 4 77.5 15.00 ...
#> math       2 4 85.0 12.91 ...

### 4.1.2 可視化

head(iris)
#>   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
#> 1          5.1         3.5          1.4         0.2  setosa
#> 2          4.9         3.0          1.4         0.2  setosa
#> 3          4.7         3.2          1.3         0.2  setosa
#> 4          4.6         3.1          1.5         0.2  setosa
#> 5          5.0         3.6          1.4         0.2  setosa
#> 6          5.4         3.9          1.7         0.4  setosa

#### 4.1.2.1 ヒストグラム

hist(iris$Sepal.Length) # ヒストグラム

x <- c(1, 2, 3)
hist(x, breaks = 2) # 階級数は2

#### 4.1.2.2 箱ひげ図

boxplot(iris[, -5])

psych::describe(iris)
#>              vars   n mean   sd median trimmed  mad min max range  skew kurtosis   se
#> Sepal.Length    1 150 5.84 0.83   5.80    5.81 1.04 4.3 7.9   3.6  0.31    -0.61 0.07
#> Sepal.Width     2 150 3.06 0.44   3.00    3.04 0.44 2.0 4.4   2.4  0.31     0.14 0.04
#> Petal.Length    3 150 3.76 1.77   4.35    3.76 1.85 1.0 6.9   5.9 -0.27    -1.42 0.14
#> Petal.Width     4 150 1.20 0.76   1.30    1.18 1.04 0.1 2.5   2.4 -0.10    -1.36 0.06
#> Species*        5 150 2.00 0.82   2.00    2.00 1.48 1.0 3.0   2.0  0.00    -1.52 0.07

boxplot(x = iris,
  formula = Sepal.Length ~ Species)

iris %>% 
  group_by(Species) %>%
  summarise(mean = mean(Sepal.Length),
            median = median(Sepal.Length))
#>   Species     mean median
#>   <fct>      <dbl>  <dbl>
#> 1 setosa      5.01    5  
#> 2 versicolor  5.94    5.9
#> 3 virginica   6.59    6.5

#### 4.1.2.3 散布図

plot(iris$Sepal.Length,
     iris$Sepal.Width)

#### 4.1.2.4 関数のグラフ

curve(x^3 - x, -2, 2)

# あるいは
f <- function(x) { x^3 - x }
data.frame(x = c(-2, 2)) %>%
  ggplot(aes(x)) +
  stat_function(fun = f)

### 4.1.3 ggplot2 (R)

データフレーム %>%
  ggplot(aes(x = 横軸に使うもの, y = 縦軸に使うもの)) +
  幾何オブジェクト1(オプション) +
  幾何オブジェクト2(オプション) + ...

# ヒストグラム
g1 <- iris %>%
  ggplot(aes(x = Sepal.Length)) +
  geom_histogram(bins = 8)

# 箱ひげ図（その1）
tmp <- iris %>% pivot_longer(-Species) # 整然データ
g2 <- tmp %>% 
  ggplot(aes(x = name, y = value)) +
  geom_boxplot()

# 箱ひげ図（その2）
g3 <- iris %>%
  ggplot(aes(x = Species, y = Sepal.Length)) +
  geom_boxplot()

# 散布図
g4 <- iris %>%
  ggplot(aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point()

# 並べて描画（列数は2）
gridExtra::grid.arrange(g1, g2, g3, g4, ncol = 2)


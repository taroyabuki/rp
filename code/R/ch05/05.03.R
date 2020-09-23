### 5.3.1 標準化

x <- c(2, 3)
y <- (x - mean(x)) / sd(x)
y
#> [1] -0.7071068  0.7071068

c(mean(y), sd(y))
#> [1] 0 1

tmp <- scale(iris[, -5])
head(tmp)
#>      Sepal.Length Sepal.Width Petal.Length Petal.Width
#> [1,]   -0.8976739  1.01560199    -1.335752   -1.311052
#> [2,]   -1.1392005 -0.13153881    -1.335752   -1.311052
#> [3,]   -1.3807271  0.32731751    -1.392399   -1.311052
#> [4,]   -1.5014904  0.09788935    -1.279104   -1.311052
#> [5,]   -1.0184372  1.24503015    -1.335752   -1.311052
#> [6,]   -0.5353840  1.93331463    -1.165809   -1.048667

attr(tmp, "scaled:center") # 元のデータの平均
Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
    5.843333     3.057333     3.758000     1.199333 

attr(tmp, "scaled:scale") # 元のデータの標準偏差
Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
   0.8280661    0.4358663    1.7652982    0.7622377 

psych::describe(tmp) # 基本統計量
#>              vars   n mean sd median trimmed  mad   min  max range  skew kurtosis   se
#> Sepal.Length    1 150    0  1  -0.05   -0.04 1.25 -1.86 2.48  4.35  0.31    -0.61 0.08
#> Sepal.Width     2 150    0  1  -0.13   -0.03 1.02 -2.43 3.08  5.51  0.31     0.14 0.08
#> Petal.Length    3 150    0  1   0.34    0.00 1.05 -1.56 1.78  3.34 -0.27    -1.42 0.08
#> Petal.Width     4 150    0  1   0.13   -0.02 1.36 -1.44 1.71  3.15 -0.10    -1.36 0.08

### 5.3.2 ワンホットエンコーディング

library(tidyverse)
library(caret)

my_df <- data.frame(
  id = c(1, 2, 3),
  class = as.factor(c("A", "B", "C")))

dummyVars(formula = ~ ., data = my_df) %>%
  predict(my_df)
#>   id class.A class.B class.C
#> 1  1       1       0       0
#> 2  2       0       1       0
#> 3  3       0       0       1

dummyVars(formula = ~ .,
          data = my_df,
          fullRank = TRUE) %>%
  predict(my_df)
#>   id class.B class.C
#> 1  1       0       0
#> 2  2       1       0
#> 3  3       0       1

### 5.3.3 整然データ（R）

library(tidyverse)

my_df <- data.table(
  名前 = c("A", "B"),
  身長 = c(160, 170),
  体重 = c(60, 70)
)

my_tidy <- my_df %>% pivot_longer(c(身長, 体重))
# あるいは
my_tidy <- my_df %>% pivot_longer(-名前)

my_tidy
#>   名前  name  value
#>   <chr> <chr> <dbl>
#> 1 A     身長    160
#> 2 A     体重     60
#> 3 B     身長    170
#> 4 B     体重     70

my_tidy %>% pivot_wider()
#>   名前   身長  体重
#>   <chr> <dbl> <dbl>
#> 1 A       160    60
#> 2 B       170    70


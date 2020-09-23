## 13.1 世界の平均気温

library(tidyverse)
my_url <- "https://www.data.jma.go.jp/cpdinfo/temp/list/csv/an_wld.csv"
my_data <- read_csv(my_url, locale = locale(encoding="sjis")) # 文字コードはShift_JIS
head(my_data)
#>      年 世界全体 北半球 南半球
#>   <dbl>    <dbl>  <dbl>  <dbl>
#> 1  1891    -0.63  -0.68  -0.59
#> 2  1892    -0.71  -0.8   -0.62
#> 3  1893    -0.75  -0.87  -0.63
#> 4  1894    -0.7   -0.73  -0.68
#> 5  1895    -0.68  -0.75  -0.6 
#> 6  1896    -0.47  -0.53  -0.42

my_data <- my_data[1:129, 1:2] # 最初の129年分，年と世界全体の2列だけ残す．
colnames(my_data) <- c("year", "world")
my_data %>% write_csv("an_wld_en.csv")

my_data <- read_csv("an_wld_en.csv")
head(my_data)
#>    year world
#>   <dbl> <dbl>
#> 1  1891 -0.63
#> 2  1892 -0.71
#> 3  1893 -0.75
#> 4  1894 -0.7 
#> 5  1895 -0.68
#> 6  1896 -0.47

my_data %>%
  filter(1981 <= year & year <= 2010) %>%
  summarize(mean(world))
#>   `mean(world)`
#>           <dbl>
#> 1       0.00367

### 13.1.1 回帰分析

library(tidyverse)
library(caret)
my_data <- read_csv("an_wld_en.csv")

my_model <- train(form = world ~ year, data = my_data, method = "lm")

my_model$finalModel$coefficients # 係数
#>   (Intercept)          year 
#> -14.844194898   0.007440239


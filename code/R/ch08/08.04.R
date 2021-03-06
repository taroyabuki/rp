## 8.4 入力変数の数とモデルの良さ

library(caret)
library(tidyverse)
my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/wine.csv")
my_data <- read_csv(my_url)

n <- nrow(my_data)
my_data2 <- my_data %>% mutate(v1 = 0:(n - 1) %% 2,
                               v2 = 0:(n - 1) %% 3)
head(my_data2)
#> # A tibble: 6 x 7
#>   LPRICE2 WRAIN DEGREES HRAIN TIME_SV    v1    v2
#>     <dbl> <dbl>   <dbl> <dbl>   <dbl> <dbl> <dbl>
#> 1  -0.999   600    17.1   160      31     0     0
#> 2  -0.454   690    16.7    80      30     1     1
#> 3  -0.808   502    17.2   130      28     0     2
#> 4  -1.51    420    16.1   110      26     1     0
#> 5  -1.72    582    16.4   187      25     0     1
#> 6  -0.418   485    17.5   187      24     1     2

my_model2 <- train(form = LPRICE2 ~ ., data = my_data2, method = "lm",
                   trControl = trainControl(method = "LOOCV"))
y  <- my_data2$LPRICE2
y_ <- my_model2 %>% predict(my_data2)

RMSE(y_, y)
#> [1] 0.256212 # RMSE（訓練）

my_model2$results$RMSE
#> [1] 0.3569918 # RMSE（検証）


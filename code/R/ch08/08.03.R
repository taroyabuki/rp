## 8.3 入力変数の数と訓練誤差・検証誤差の関係

library(tidyverse)
library(caret)
my_data <- read.csv("wine.csv")
my_model1 <- train(form = LPRICE2 ~ .,
                   data = my_data,
                   method = "lm")

my_pred <- my_model1 %>% predict(my_data)
RMSE(my_pred, my_data$LPRICE2) # RMSE（訓練）
#> [1] 0.2586167

n <- nrow(my_data) # データの件数
my_data2 <- my_data %>% mutate(rand1 = runif(n)) # 乱数からなる列の追加

my_model2 <- train(form = LPRICE2 ~ .,
                   data = my_data2,
                   method = "lm")

my_pred2 <- my_model2 %>% predict(my_data2)
RMSE(my_pred2, my_data$LPRICE2) # RMSE（訓練）
#> [1] 0.2534026

c(my_model1$result$RMSE,  # RMSE（検証）（rand1なしのモデル）
  my_model22$result$RMSE) # RMSE（検証）（rand1ありのモデル）

#> [1] 0.3680248 0.3842703


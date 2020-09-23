### 7.8.1 Rの場合

library(tidyverse)
library(caret)
my_data <- cars
my_result <- train(form = dist ~ speed, data = my_data, method = "knn")

my_pred <- my_result %>% predict(my_data)
RMSE(my_pred, my_data$speed)
#> [1] 32.24723

f <- function(x) { my_result %>% predict(data.frame(speed = x))}

my_data %>% ggplot(aes(x = speed, y = dist)) +
  geom_point() +         # データ
  stat_function(fun = f) # モデル


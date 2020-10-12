### 7.8.1 Rの場合

library(tidyverse)
library(caret)
my_data <- cars
my_model <- train(form = dist ~ speed, data = my_data, method = "knn")

y_ <- my_model %>% predict(my_data)
RMSE(y_, my_data$speed)
#> [1] 32.24723

f <- function(x) { my_model %>% predict(data.frame(speed = x))}

my_data %>% ggplot(aes(x = speed, y = dist)) +
  geom_point() +         # データ
  stat_function(fun = f) # モデル


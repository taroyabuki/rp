pdf(file = "07-r-nnet.pdf", width = 5.83, height = 4.13)

set.seed(5)

library(tidyverse)
library(caret)
my_data <- cars
my_result <- train(form = dist ~ speed, data = my_data, method = "nnet",
                   linout = TRUE,                     # 回帰（nnetで回帰を行う際は必須）
                   preProcess = c("center", "scale")) # 標準化

f <- function(x) { my_result %>% predict(data.frame(speed = x))}
my_data %>% ggplot(aes(x = speed, y = dist)) +
  geom_point() +         # データ
  stat_function(fun = f) # モデル

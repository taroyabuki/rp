pdf(file = "07-r-10degree.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(caret)
my_data <- cars
my_idx <- c(2, 7, 11, 18, 27, 30, 34, 38, 39, 44) # 抜き出すデータの番号
my_train <- my_data[my_idx, ]                     # データを抜き出す．

my_result <- train(form = dist ~ poly(speed, degree = 10, raw = TRUE),
                   data = my_train, method = "lm")

f <- function(x) { my_result %>% predict(data.frame(speed = x)) }

my_data %>% ggplot(aes(x = speed, y = dist)) +
  coord_cartesian(ylim = c(0, 120)) + # y座標の描画範囲
  geom_point(data = my_train, color = "red", size = 3) + # 訓練データ
  geom_point(data = my_data[-my_idx, ]) + # 訓練に使わなかったデータ
  stat_function(fun = f)

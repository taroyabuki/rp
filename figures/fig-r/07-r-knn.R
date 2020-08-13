pdf(file = "07-r-knn.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(caret)
my_data <- cars
my_result <- train(form = dist ~ speed, data = my_data, method = "knn",
                   tuneGrid = data.frame(k = 5))

f <- function(x) { my_result %>% predict(data.frame(speed = x))}
my_data %>% ggplot(aes(x = speed, y = dist)) +
  geom_point() +         # データ
  stat_function(fun = f) # モデル

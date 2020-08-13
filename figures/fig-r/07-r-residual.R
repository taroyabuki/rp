pdf(file = "07-r-residual.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(caret)
my_data <- cars

my_result <- train(form = dist ~ speed, data = my_data, method = "lm") # モデル生成
my_data$prediction <- my_result %>% predict(my_data)                   # 予測
my_data$residual <- my_data$dist - my_data$prediction # 残差

f <- function(x) { my_result %>% predict(data.frame(speed = x)) }

my_data %>% ggplot(aes(x = speed, y = dist)) +
  geom_point() +
  stat_function(fun = f) +
  geom_linerange(mapping = aes(ymin = dist, ymax = prediction),
                 linetype = "dotted")

### 7.5.1 Rの場合

library(tidyverse)
library(caret)
my_data <- cars
my_model <- train(form = dist ~ speed, data = my_data, method = "lm")

my_test <- data.frame(speed = 21.5) # 予測対象の準備

my_model %>% predict(my_test) # 予測対象に対する予測

#>        1 
#> 66.96769 

f <- function(x) { my_model %>% predict(data.frame(speed = x)) }
f(21.5)

#>        1 
#> 66.96769 

my_data %>% ggplot(aes(x = speed, y = dist)) +
  geom_point() +
  stat_function(fun = f) # 結果は割愛

my_data %>% ggplot(aes(x = speed, y = dist)) +
  geom_point() +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE)


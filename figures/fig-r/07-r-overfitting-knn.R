pdf(file = "07-r-overfitting-knn.pdf", width = 5.83, height = 4.13)

library(furrr)
plan(multisession)

set.seed(0)

library(tidyverse)
library(caret)
library(furrr)
my_data <- cars

f <- function(x) {
  my_result <- train(form = dist ~ speed, data = my_data,method = "knn",
                     tuneGrid = data.frame(k = x),
                     trControl = trainControl(method = "boot", number = 1000))
  list(
    x = x,
    training = RMSE(predict(my_result, my_data), my_data$dist), # 訓練RMSE
    validation = my_result$results$RMSE)                        # 検証RMSE
}

tmp <- 1:15 %>% future_map_dfr(f)

my_result <- tmp %>% pivot_longer(-x)

my_result %>% ggplot(aes(x = x, y = value, color = name)) +
  geom_point() +
  geom_line()
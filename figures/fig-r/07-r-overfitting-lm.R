pdf(file = "07-r-overfitting-lm.pdf", width = 5.83, height = 4.13)

set.seed(0)

library(tidyverse)
library(caret)
library(furrr)
plan(multisession)

my_data <- cars

n <- 50
f <- function(x) {
  my_samples <- createResample(my_data$dist, times = n)
  my_samples %>% map_dfr(function(sample) {
    my_train <- my_data[ sample, ]
    my_test  <- my_data[-sample, ]
    tmp <- as.formula(bquote(dist ~ poly(speed, degree = .(x), raw = TRUE)))
    my_model <- train(form = tmp, data = my_train, method = "lm",
                      trControl = trainControl(method = "none"))
    list(
      x = x,
      train = RMSE(my_train$dist, predict(my_model, newdata = my_train)),
      validation = RMSE(my_test$dist, predict(my_model, newdata = my_test))
    )
  })
}

my_scores <- 1:6 %>% future_map_dfr(f)
head(my_scores)

tmp <- my_scores %>% pivot_longer(-x)
tmp %>% ggplot(aes(x = x, y = value, color = name)) +
  stat_summary(fun = mean, geom = "line") +
  stat_summary(fun.data = mean_se) +
  xlab("degree") + ylab("RMSE")

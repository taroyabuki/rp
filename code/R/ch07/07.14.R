## 7.14 補足：モデルの柔軟さと予測性能

library(tidyverse)
library(caret)
library(furrr)
plan(multisession)

my_data <- cars
my_samples <- createResample(my_data$dist, times = n) # ブートストラップ
#my_samples <- createMultiFolds(my_data$dist, k = 5, times = 10) # 5分割交差検証（10回）

f <- function(x) {
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
#>       x train validation
#>   <int> <dbl>      <dbl>
#> 1     1  12.3       17.5
#> 2     1  12.5       20.3
#> 3     1  13.1       17.4
#> 4     1  15.9       12.2
#> 5     1  14.5       12.7
#> 6     1  16.2       12.2

tmp <- my_scores %>% pivot_longer(-x)
tmp %>% ggplot(aes(x = x, y = value, color = name)) +
  stat_summary(fun = mean, geom = "line") +
  stat_summary(fun.data = mean_se) +
  xlab("degree") + ylab("RMSE")


### 9.8.1 Rの場合

library(tidyverse)
library(caret)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "rf")
my_model$results
#>   mtry  Accuracy     Kappa AccuracySD    KappaSD
#> 1    2 0.9541731 0.9304340 0.01731558 0.02635300
#> 2    3 0.9520800 0.9273056 0.01973786 0.03001535
#> 3    4 0.9477295 0.9207535 0.02067023 0.03139036

my_model <- train(form = Species ~ ., data = my_data, method = "xgbTree")
my_model$results %>%
  filter(Accuracy == max(Accuracy)) %>% # 正解率（検証）の最大値
  select(Accuracy)
#>   Accuracy
#> 1 0.949123


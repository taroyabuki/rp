### 9.6.1 Rの場合

library(tidyverse)
library(caret)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "nnet",
                   preProcess = c("center", "scale")) # 標準化

my_model$results %>% filter(Accuracy == max(Accuracy)) # 正解率（検証）の最大値
#>   size      decay  Accuracy     Kappa AccuracySD    KappaSD
#> 1    3 0.01778279 0.9684804 0.9521008 0.02219845 0.03344919


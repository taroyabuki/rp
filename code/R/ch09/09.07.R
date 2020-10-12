### 9.7.1 Rの場合

library(tidyverse)
library(caret)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "rpart")
my_model$results %>% filter(Accuracy == max(Accuracy)) # 正解率（検証）の最大値
#>   cp  Accuracy     Kappa AccuracySD    KappaSD
#> 1  0 0.9512972 0.9262777  0.0270735 0.04098842

rpart.plot::rpart.plot(my_model$finalModel, digit = 3, type = 5)


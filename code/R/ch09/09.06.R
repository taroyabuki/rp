## 9.6 他の分類手法

### 9.6.1 K最近傍法

library(caret)
library(tidyverse)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "knn",
                  trControl = trainControl(method = "LOOCV"))
my_model$results %>% filter(Accuracy == max(Accuracy))
#>   k  Accuracy Kappa
#> 1 9 0.9733333  0.96

### 9.6.2 ニューラルネットワーク

library(caret)
library(tidyverse)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "nnet",
                  preProcess = c("center", "scale"), # 標準化
                  trControl = trainControl(method = "LOOCV"),
                  trace = FALSE) # 途中経過を表示しない
my_model$results %>% filter(Accuracy == max(Accuracy))
#>   size decay  Accuracy Kappa
#> 1    3   0.1 0.9733333  0.96
#> 2    5   0.1 0.9733333  0.96


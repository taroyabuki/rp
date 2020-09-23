### 9.5.1 Rの場合

library(tidyverse)
library(caret)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "knn",
                  tuneGrid = data.frame(k = c(1:20)),
                  trControl = trainControl(method = "boot", number = 1000))
                   
my_model$results %>% filter(Accuracy == max(Accuracy)) # 正解率（検証）の最大値
#>    k  Accuracy     Kappa AccuracySD    KappaSD
#> 1 13 0.9591608 0.9381671 0.02507297 0.03777022

ggplot(my_model) # チューニング結果の描画


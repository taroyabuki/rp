## 9.4 複数の木を使う方法

### 9.4.1 ランダムフォレスト

library(caret)
library(tidyverse)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "rf",
                  tuneGrid = data.frame(mtry = 2:4), # 省略可
                  trControl = trainControl(method = "LOOCV"))
my_model$results
#>   mtry Accuracy Kappa
#> 1    2     0.96  0.94
#> 2    3     0.96  0.94
#> 3    4     0.96  0.94

### 9.4.2 ブースティング

my_model <- train(
  form = Species ~ ., data = my_data, method = "xgbTree",
  tuneGrid = expand.grid(
    nrounds          = c(50, 100, 150),
    max_depth        = c(1, 2, 3),
    eta              = c(0.3, 0.4),
    gamma            = 0,
    colsample_bytree = c(0.6, 0.8),
    min_child_weight = 1,
    subsample        = c(0.5, 0.75, 1)),
  trControl = trainControl(method = "cv", number = 5)) # 5分割交差検証
my_model$results %>% filter(Accuracy == max(Accuracy)) %>% head(5) %>% t
#>                            1           2           3           4           5
#> eta               0.30000000  0.30000000  0.30000000  0.40000000  0.30000000
#> max_depth         1.00000000  1.00000000  1.00000000  1.00000000  3.00000000
#> gamma             0.00000000  0.00000000  0.00000000  0.00000000  0.00000000
#> colsample_bytree  0.60000000  0.60000000  0.80000000  0.60000000  0.80000000
#> min_child_weight  1.00000000  1.00000000  1.00000000  1.00000000  1.00000000
#> subsample         0.50000000  0.75000000  0.75000000  0.50000000  0.50000000
#> nrounds          50.00000000 50.00000000 50.00000000 50.00000000 50.00000000
#> Accuracy          0.96000000  0.96000000  0.96000000  0.96000000  0.96000000
#> Kappa             0.94000000  0.94000000  0.94000000  0.94000000  0.94000000
#> AccuracySD        0.02788867  0.02788867  0.02788867  0.01490712  0.01490712
#> KappaSD           0.04183300  0.04183300  0.04183300  0.02236068  0.02236068

### 9.4.3 入力変数の重要度

my_model <- train(form = Species ~ ., data = my_data, method = "rf")
ggplot(varImp(my_model))


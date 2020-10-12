## 9.4 訓練データの再現

# 正解
y <- c("serosa", "setosa")

# 予測
y_A <- c("serosa", "versicolor")

# 比較
y_A == y
#> [1]  TRUE FALSE

# 正解率
mean(y_A == y)
#> [1] 0.5

### 9.4.1 Rの場合

library(tidyverse)
library(caret)
my_data <- iris
my_model <- train(form = Species ~ ., data = my_data, method = "knn")

y_ <- my_model %>% predict(my_data) # 訓練データの再現
table(y_, my_data$Species)           # 混同行列の作成
#> y_           setosa versicolor virginica
#>   setosa         50          0         0
#>   versicolor      0         48         1
#>   virginica       0          2        49

mean(y_ == my_data$Species)
#> [1] 0.98

y_ %>% confusionMatrix(my_data$Species)
#> Confusion Matrix and Statistics
#> 
#>             Reference
#> Prediction   setosa versicolor virginica
#>   setosa         50          0         0
#>   versicolor      0         48         1
#>   virginica       0          2        49
#> 
#> Overall Statistics
#>                                           
#>                Accuracy : 0.98 
# 以下は割愛


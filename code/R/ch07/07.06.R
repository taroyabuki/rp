### 7.6.3 交差検証の実践

library(caret)
library(tidyverse)
my_data <- cars

my_model <- train(form = dist ~ speed, data = my_data, method = "lm")

my_model$results
#>   intercept    RMSE  Rsquared      MAE   RMSESD RsquaredSD    MAESD
#> 1      TRUE 16.0206 0.6662176 12.14701 2.518604 0.09249158 1.920564

my_model <- train(form = dist ~ speed, data = my_data, method = "lm",
                  trControl = trainControl(method = "cv", number = 5))
my_model$results                 
#>   intercept     RMSE  Rsquared      MAE  RMSESD RsquaredSD    MAESD
#> 1      TRUE 15.06708 0.6724501 12.12448 4.75811  0.1848932 3.052435

my_model <- train(form = dist ~ speed, data = my_data, method = "lm",
                  trControl = trainControl(method="LOOCV"))
my_model$results
#>   intercept     RMSE  Rsquared      MAE
#> 1      TRUE 15.69731 0.6217139 12.05918

### 7.6.4 交差検証の並列化

library(doParallel)
cl <- makeCluster(detectCores())
registerDoParallel(cl)

#### 7.6.5.1 準備

library(caret)
library(tidyverse)
my_data <- cars
my_model <- train(form = dist ~ speed, data = my_data, method = "lm")
y  <- my_data$dist
y_ <- my_model %>% predict(my_data)

#### 7.6.5.2 当てはまりの良さの指標

# RMSE（訓練）
RMSE(y_, y)
#> [1] 15.06886



# 決定係数1（訓練）
R2(pred = y_, obs = y,
   form = "traditional")
#> [1] 0.6510794


# 決定係数6（訓練）
R2(pred = y_, obs = y,
   form = "corr")
#> [1] 0.6510794

#### 7.6.5.3 予測性能の指標

my_model <- train(form = dist ~ speed, data = my_data, method = "lm")
my_model$results
#>   intercept     RMSE  Rsquared      MAE   RMSESD RsquaredSD   MAESD
#> 1      TRUE 14.88504 0.6700353 11.59226 2.778445  0.1529552 2.05134

#### 7.6.5.4 補足：予測性能の指標（工夫が必要なもの）

# 決定係数1（検証）を求めるための準備
my_r2_1 <- function(data, lev, model) {
  c(defaultSummary(data),
    "R2_1" = R2(pred = data$pred, obs = data$obs, form="traditional"))
}

my_model <- train(form = dist ~ speed, data = my_data, method = "lm",
                  trControl = trainControl(summaryFunction = my_r2_1))
my_model$results
#>   intercept    RMSE  Rsquared      MAE      R2_1 ...
#> 1      TRUE 16.7833 0.6206035 12.93985 0.5718879 ...
# 左から，RMSE（検証），決定係数6（検証），MAE（検証），決定係数1（検証）

#### 7.6.5.5 補足：予測性能の指標（RとPythonで同じ結果を得る）

my_model <- train(form = dist ~ speed, data = my_data, method = "lm",
                  trControl = trainControl(
                    method = "LOOCV",
                    summaryFunction = my_r2_1))
my_model$results
#>   intercept     RMSE  Rsquared      MAE      R2_1
#> 1      TRUE 15.69731 0.6217139 12.05918 0.6213689
# 左から，RMSE（検証），決定係数 6（検証），MAE（検証），決定係数 1（検証）


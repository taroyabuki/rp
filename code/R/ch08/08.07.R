### 8.7.1 ニューラルネットワークとは何か

curve(1 / (1 + exp(-x)), -6, 6)

### 8.7.2 ニューラルネットワークの訓練

library(caret)
library(tidyverse)
my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/wine.csv")
my_data <- read_csv(my_url)

my_model <- train(form = LPRICE2 ~ .,
                  data = my_data,
                  method = "neuralnet",              # ニューラルネットワーク
                  preProcess = c("center", "scale"), # 標準化
                  trControl = trainControl(method = "LOOCV"))
plot(my_model$finalModel) # 訓練済ネットワークの描画（結果は割愛）

y  <- my_data$LPRICE2
y_ <- my_model %>% predict(my_data)
RMSE(y_, y)      # RMSE（訓練）
#> [1] 0.2199101

my_model$results # RMSE（検証）
#>   layer1 layer2 layer3      RMSE ...
#> 1      1      0      0 0.2957813 ...
#> 2      3      0      0 0.3095204 ...
#> 3      5      0      0 0.3937699 ...

### 8.7.3 ニューラルネットワークのチューニング

my_model <- train(
  form = LPRICE2 ~ .,
  data = my_data,
  method = "neuralnet",
  preProcess = c("center", "scale"),
  trControl = trainControl(method = "LOOCV"),
  tuneGrid = expand.grid(layer1 = 1:5,
                         layer2 = 0:2,
                         layer3 = 0))

y  <- my_data$LPRICE2
y_ <- my_model %>% predict(my_data)

RMSE(y_, y)          # RMSE（訓練）
#> [1] 0.1336863

my_model$results %>% # RMSE（検証）
  filter(RMSE == min(RMSE))
#>   layer1 layer2 layer3      RMSE ...
#> 1      2      0      0 0.3165704 ...


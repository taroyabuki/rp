### 8.2.1 Rの場合

library(tidyverse)
library(caret)
my_data <- read_csv("wine.csv") # 8.1節で作成したwine.csvを使う．
#my_url <- "https://raw.githubusercontent.com/taroyabuki/rp/master/data/wine.csv"
#my_data <- read_csv(my_url)

my_model <- train(form = LPRICE2 ~ WRAIN + DEGREES + HRAIN + TIME_SV,
                  data = my_data,
                  method = "lm")

my_model$finalModel$coefficients
#>   (Intercept)         WRAIN       DEGREES         HRAIN       TIME_SV 
#> -12.145333577   0.001166782   0.616392441  -0.003860554   0.023847413 

my_test <- data.frame(WRAIN = 500, DEGREES = 17, HRAIN = 120, TIME_SV = 2)
my_model %>% predict(my_test)
#> 1 
#> -1.498843 

my_model$results
#>   intercept     RMSE Rsquared       MAE     RMSESD RsquaredSD      MAESD
#> 1      TRUE 0.339309 0.751259 0.2834835 0.06092742  0.1486527 0.05348568

### 8.2.3 補足：行列計算による再現

A <- my_data[, -1] %>% # 1列目（LPRICE2）を除外して，
  mutate(b = 1) %>%    # すべて1の列を追加して，
  as.matrix            # 行列にする．
y <- my_data$LPRICE2
solve(t(A) %*% A, t(A) %*% y) # AT A = AT yを解く（ATはAの転置行列）
#>                  [,1]
#> WRAIN     0.001166782
#> DEGREES   0.616392441
#> HRAIN    -0.003860554
#> TIME_SV   0.023847413
#> b       -12.145333577

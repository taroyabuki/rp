### 7.11.1 Rの場合

library(tidyverse)
library(caret)
my_data <- cars

my_model <- train(form = dist ~ speed, data = my_data, method = "lm",
                  trControl = trainControl(method = "cv", number = 5))

my_model$results
#>   intercept     RMSE  Rsquared      MAE   RMSESD RsquaredSD    MAESD
#> 1      TRUE 15.54312 0.6844412 12.37043 3.497211  0.1979125 3.068685

### 7.11.3 補足：交差検証による手法の比較

library(tidyverse)
library(caret)
my_data <- cars

# 線形単回帰分析
my_lm_model  <- train(form = dist ~ ., data = my_data, method = "lm")
my_lm_model$results
#>   intercept     RMSE  Rsquared      MAE RMSESD RsquaredSD    MAESD
#> 1      TRUE 15.78902 0.6699013 12.21545 3.1511  0.1050254 2.267991

# K最近傍法
my_knn_model <- train(form = dist ~ ., data = my_data, method = "knn")
my_knn_model$results
#>   k     RMSE  Rsquared      MAE   RMSESD RsquaredSD    MAESD
#> 1 5 16.95169 0.6179135 13.12438 2.742619  0.1380670 1.970236
#> 2 7 17.16295 0.6136017 13.24059 2.304467  0.1185074 1.483025
#> 3 9 17.63868 0.5898739 13.56792 2.749958  0.1251806 1.733104

my_df <- data.frame(lm = my_lm_model$resample$RMSE,
                    knn = my_knn_model$resample$RMSE)
head(my_df)
#>         lm      knn
#> 1 11.65310 15.88667
#> 2 19.02267 16.50157
#> 3 15.19800 17.99563
#> 4 11.99702 19.17346
#> 5 19.39390 21.07320
#> 6 16.20855 11.63737

boxplot(my_df)

wilcox.test(my_df$lm, my_df$knn, alternative = "two.sided")
#>         Wilcoxon rank sum exact test
#> 
#> data:  my_df$lm and my_df$knn
#> W = 243, p-value = 0.1823
#> alternative hypothesis: true location shift is not equal to 0


## 10.2 2値分類の性能指標

library(tidyverse)
library(caret)

my_data <- data.frame(
  answer = factor(c(  0,   1,   1,   0,   1,   0,    1,   0,   0,   1)), # 正解
  prob =          c(0.7, 0.8, 0.3, 0.4, 0.9, 0.6, 0.99, 0.1, 0.2, 0.5))  # 陽性確率

my_pred <- ifelse(my_data$prob >= 0.5, 1, 0) %>% # 0.5以上を陽性とする．
  as.factor                                      # 因子に変換する．
my_pred
#>  [1] 1 1 0 0 1 1 1 0 0 1
#> Levels: 0 1

confusionMatrix(data = my_data$pred,        # 予測
                reference = my_data$answer, # 正解
                positive = "1",             # 陽性
                mode = "everything")        # すべての指標を求める．
#> Confusion Matrix and Statistics
#> 
#>           Reference
#> Prediction 0 1
#>          0 3 1
#>          1 2 4
#>                                           
#>                Accuracy : 0.7             
#>                  95% CI : (0.3475, 0.9333)
#>     No Information Rate : 0.5             
#>     P-Value [Acc > NIR] : 0.1719          
#>                                           
#>                   Kappa : 0.4             
#>                                           
#>  Mcnemar's Test P-Value : 1.0000          
#>                                           
#>             Sensitivity : 0.8000          
#>             Specificity : 0.6000          
#>          Pos Pred Value : 0.6667          
#>          Neg Pred Value : 0.7500          
#>               Precision : 0.6667          
#>                  Recall : 0.8000          
#>                      F1 : 0.7273          
#>              Prevalence : 0.5000          
#>          Detection Rate : 0.4000          
#>    Detection Prevalence : 0.6000          
#>       Balanced Accuracy : 0.7000          
#>                                           
#>        'Positive' Class : 1

### 7.4.1 Rの場合

library(tidyverse)
library(caret)
my_data <- cars

my_model <- train(form = dist ~ speed, # モデル式
                  data = my_data,      # データ
                  method = "lm")       # 手法（線形回帰分析）

my_model$finalModel$coefficients # 係数の確認

#> (Intercept)       speed 
#> -17.579095    3.932409 


## 10.5 ロジスティック回帰

curve(1 / (1 + exp(-x)), -6, 6)

#> (Intercept)    Class2nd    Class3rd   ClassCrew   SexFemale    AgeAdult 
#>   0.6853195  -1.0180950  -1.7777622  -0.8576762   2.4200603  -1.0615424 

### 10.5.1 Rの場合

library(tidyverse)
library(caret)
my_data <- epitools::expand.table(Titanic)

my_model <- train(form = Survived ~ .,data = my_data,  method = "glm") 
my_model$results # 正解率（検証）
#>   parameter  Accuracy     Kappa AccuracySD    KappaSD
#> 1      none 0.7789422 0.4455538 0.01106743 0.02311639

my_model$finalModel$coefficients
#> (Intercept)    Class2nd    Class3rd   ClassCrew   SexFemale    AgeAdult 
#>   0.6853195  -1.0180950  -1.7777622  -0.8576762   2.4200603  -1.0615424 

mean(my_pred == my_data$Survived)
#> [1] 0.7782826


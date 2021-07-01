### 3.8.2 変数や関数についての調査

x <- 123
typeof(x)
#> [1] "double"

library(caret)
library(tidyverse)
my_data <- cars
my_model <- train(form = dist ~ speed, data = my_data, method = "knn")
my_model$results
# 結果は割愛

attributes(my_model)
#> $names
#>  [1] "method"       "modelInfo"    "modelType"    "results"     
#>  [5] "pred"         "bestTune"     "call"         "dots"        
#>  [9] "metric"       "control"      "finalModel"   "preProcess"  
#> [13] "trainingData" "resample"     "resampledCM"  "perfNames"   
#> [17] "maximize"     "yLimits"      "times"        "levels"      
#> [21] "terms"        "coefnames"    "xlevels"    
#> 
#> $class
#> [1] "train"         "train.formula"

?log
# あるいは
help(log)

### 3.8.3 RのNA，Pythonのnan

my_v = c(1, NA, 3)
my_v
#> [1]  1 NA  3

is.na(my_v[2])
#> [1] TRUE

my_v[2] == NA # 誤り
#> [1] NA


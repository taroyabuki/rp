## 8.5 変数選択

library(caret)
library(tidyverse)
my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/wine.csv")
my_data <- read_csv(my_url)
n <- nrow(my_data)
my_data2 <- my_data %>% mutate(rand1 = runif(n), rand2 = runif(n))

my_model <- train(form = LPRICE2 ~ .,
                  data = my_data2,
                  method = "leapForward",
                  trControl = trainControl(method = "LOOCV"))
summary(my_model$finalModel)$outmat
#>          WRAIN DEGREES HRAIN TIME_SV rand1 rand2
#> 1  ( 1 ) " "   "*"     " "   " "     " "   " "  
#> 2  ( 1 ) " "   "*"     "*"   " "     " "   " "  
#> 3  ( 1 ) " "   "*"     "*"   "*"     " "   " "  
#> 4  ( 1 ) "*"   "*"     "*"   "*"     " "   " "  

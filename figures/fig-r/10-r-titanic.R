pdf(file = "10-r-titanic.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(caret)
my_data <- epitools::expand.table(Titanic)

my_model <- train(form = Survived ~ .,data = my_data,  method = "rpart")
rpart.plot::rpart.plot(my_model$finalModel, digit = 3, type = 5) # 可視化
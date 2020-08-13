pdf(file = "09-r-knn.pdf", width = 5.83, height = 4.13)

library(doParallel)
cl <- makeCluster(detectCores())
registerDoParallel(cl)

set.seed(0)

library(tidyverse)
library(caret)
my_data <- iris

my_result <- train(form = Species ~ ., data = my_data, method = "knn",
                   tuneGrid = data.frame(k = c(1:20)),
                   trControl = trainControl(method = "boot", number = 1000))
                   

ggplot(my_result)

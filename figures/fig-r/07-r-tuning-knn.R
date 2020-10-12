pdf(file = "07-r-tuning-knn.pdf", width = 5.83, height = 4.13)

set.seed(4)

library(tidyverse)
library(caret)
my_data <- cars
my_model <- train(form = dist ~ speed, data = my_data, method = "knn",
                  tuneGrid = expand.grid(k = 1:15))
my_model$results %>% filter(RMSE == min(my_model$results$RMSE))
ggplot(my_model)

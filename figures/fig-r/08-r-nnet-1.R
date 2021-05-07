pdf(file = "08-r-nnet-1.pdf", width = 5.83, height = 4.13)

library(tidyverse)
my_url <- str_c("https://raw.githubusercontent.com/taroyabuki",
                "/fromzero/master/data/wine.csv")
my_data <- read_csv(my_url)

library(caret)
my_model <- train(form = LPRICE2 ~ .,
                  data = my_data,
                  method = "neuralnet",
                  preProcess = c("center", "scale"),
                  trControl = trainControl(method = "repeatedcv",
                                           number = 5, repeats = 10))
my_model$results
plot(my_model$finalModel)

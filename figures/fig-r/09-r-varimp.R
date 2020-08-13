pdf(file = "09-r-varimp.pdf", width = 5.83, height = 4.13)

set.seed(0)

library(caret)
my_data <- iris

my_model <- train(form = Species ~ ., data = my_data, method = "xgbTree")

plot(varImp(my_model))

pdf(file = "07-r-boxplot.pdf", width = 5.83, height = 4.13)

set.seed(0)

library(tidyverse)
library(caret)
my_data <- cars

my_lm_model  <- train(form = dist ~ ., data = my_data, method = "lm")
my_lm_model$results

my_knn_model <- train(form = dist ~ ., data = my_data, method = "knn")
my_knn_model$results

my_df <- data.frame(lm = my_lm_model$resample$RMSE,
                    knn = my_knn_model$resample$RMSE)
head(my_df)

boxplot(my_df)

wilcox.test(my_df$lm, my_df$knn)
pdf(file = "10-r-roc.pdf", width = 5.83, height = 4.13)

library(tidyverse)

my_data <- data.frame(
  answer = factor(c(  0,   1,   1,   0,   1,   0,    1,   0,   0,   1)),
  prob =          c(0.7, 0.8, 0.3, 0.4, 0.9, 0.6, 0.99, 0.1, 0.2, 0.5))

library(ROCR)
my_pred <- my_data$prob %>% prediction(labels = my_data$answer)
my_pred %>% performance(measure = "tpr", x.measure = "fpr") %>% plot

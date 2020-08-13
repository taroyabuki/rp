pdf(file = "11-r-b-iris-1.pdf", width = 5.83, height = 4.13)

set.seed(0)

my_data <- iris[sample(nrow(iris)), ]

library(tidyverse)
library(caret)
library(keras)
my_model <- keras_model_sequential() %>%
  layer_dense(units = 3, activation = "relu", input_shape = c(4)) %>%
  layer_dense(units = 3,              # 出力層のニューロン数
              activation = "softmax") # 活性化関数

X <- scale(my_data[, -5])            # 標準化
y <- as.integer(my_data$Species) - 1 # 0から始まる整数

my_model %>% compile(
  loss = "sparse_categorical_crossentropy",
  optimizer = "rmsprop",
  metrics = c("accuracy"))

my_history <- my_model %>% fit(x = X,
                               y = y,
                               validation_split = 0.25,
                               batch_size = 1, epochs = 50)

plot(my_history)

my_history

my_model %>% evaluate(x = X, y = y)

my_prob <- my_model %>% predict(X)
head(my_prob)

my_pred <- my_model %>% predict_classes(X)
my_pred <- apply(my_prob, 1, which.max) - 1
head(my_pred)

f <- function(i) { -log(my_prob[i, y[i] + 1]) }
1:length(y) %>% map_dbl(f) %>% mean

mean(my_pred == y)

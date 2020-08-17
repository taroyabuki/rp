pdf(file = "12-r-mnist1.pdf", width = 5.83, height = 4.13)

set.seed(0)

library(tidyverse)
library(caret)
library(keras)
#c(c(x_train, y_train), c(x_test, y_test)) %<-% dataset_mnist()
#↑がうまく行かない場合
c(c(x_train, y_train), c(x_test, y_test)) %<-% readRDS("/tmp/mnist.obj")

x_train <- x_train / 255
x_test  <- x_test  / 255

my_index <- createDataPartition(y = y_train, p = 6000 / 60000, list = FALSE)
x_train <- x_train[my_index, , ]
y_train <- y_train[my_index]

x_train1d <- array_reshape(x = x_train, dim = c(nrow(x_train), 784))
x_test1d  <- array_reshape(x = x_test,  dim = c(nrow(x_test),  784))

my_model <- keras_model_sequential() %>%
  layer_dense(units = 256, activation = "relu", input_shape = c(784)) %>%
  layer_dense(units = 10, activation = "softmax")

my_model %>% compile(
  loss = "sparse_categorical_crossentropy",
  optimizer = "rmsprop",
  metrics = c("accuracy"))

my_history <- my_model %>%
  fit(x = x_train1d, y = y_train, batch_size = 128, epochs = 20,
      validation_split = 0.1,
      callbacks = callback_early_stopping(patience = 5, restore_best_weights = TRUE))

#plot(my_history)
#↑がうまく行かない場合
tmp <- my_history
tmp$params$epochs<-length(tmp$metrics$loss)
plot(tmp)
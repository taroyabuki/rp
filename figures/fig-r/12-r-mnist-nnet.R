pdf(file = "12-r-mnist-nnet.pdf", width = 5.83, height = 4.13)

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

my_cb <- callback_early_stopping(patience = 5,                # 訓練停止条件
                                 restore_best_weights = TRUE) # 最善を保持

my_history <- my_model %>%
  fit(x = x_train1d,          # 入力変数
      y = y_train,            # 出力変数
      validation_split = 0.2, # 検証データの割合
      batch_size = 128,       # バッチサイズ
      epochs = 20,            # エポック数の上限
      callbacks = my_cb)      # エポックごとに行う処理

#plot(my_history)
#↑がうまく行かない場合
tmp <- my_history
tmp$params$epochs<-length(tmp$metrics$loss)
plot(tmp)

my_prob <- my_model %>% predict(x_test1d)
my_pred <- apply(my_prob, 1, which.max) - 1
table(my_pred, y_test)

my_model %>% evaluate(x = x_test1d, y = y_test)
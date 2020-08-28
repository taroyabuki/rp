pdf(file = "12-r-mnist-lenet.pdf", width = 5.83, height = 4.13)

set.seed(0)

set.seed(0)

library(keras)
#c(c(x_train, y_train), c(x_test, y_test)) %<-% dataset_mnist()
#↑がうまく行かない場合
c(c(x_train, y_train), c(x_test, y_test)) %<-% readRDS("/tmp/mnist.obj")

x_train <- x_train / 255
x_test  <- x_test  / 255

my_index <- sample(1:60000, 6000)
x_train <- x_train[my_index, , ]
y_train <- y_train[my_index]

x_train2d <- array_reshape(x = x_train, dim = c(nrow(x_train), 28, 28, 1))
x_test2d  <- array_reshape(x = x_test,  dim = c(nrow(x_test),  28, 28, 1))

my_model <- keras_model_sequential() %>%
  layer_conv_2d(filters = 20, kernel_size = 5, activation = "relu", input_shape = c(28, 28, 1)) %>% 
  layer_max_pooling_2d(pool_size = 2, strides = 2) %>% 
  layer_conv_2d(filters = 50, kernel_size = 5, activation = "relu") %>% 
  layer_max_pooling_2d(pool_size = 2, strides = 2) %>% 
  layer_dropout(rate = 0.25) %>% 
  layer_flatten() %>% 
  layer_dense(units = 500, activation = "relu") %>% 
  layer_dropout(rate = 0.5) %>% 
  layer_dense(units = 10, activation = "softmax")

my_model %>% compile(
  loss = "sparse_categorical_crossentropy",
  optimizer = "rmsprop",
  metrics = c("accuracy"))

my_cb <- callback_early_stopping(patience = 5,                # 訓練停止条件
                                 restore_best_weights = TRUE) # 最善を保持

my_history <- my_model %>%
  fit(x = x_train2d,          # 入力変数
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

my_model %>% evaluate(x = x_test2d, y = y_test)
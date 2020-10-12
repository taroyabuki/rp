### 12.2.1 前処理

library(keras)
#c(c(x_train, y_train), c(x_test, y_test)) %<-% dataset_mnist()
#↑がうまく行かない場合
c(c(x_train, y_train), c(x_test, y_test)) %<-% readRDS("/tmp/mnist.obj")
x_train <- x_train / 255
x_test  <- x_test  / 255

my_index <- sample(1:60000, 6000)
x_train <- x_train[my_index, , ]
y_train <- y_train[my_index]

x_train1d <- array_reshape(x = x_train, dim = c(nrow(x_train), 784))
x_test1d  <- array_reshape(x = x_test,  dim = c(nrow(x_test),  784))

### 12.2.2 訓練

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

tmp <- my_history
tmp$params$epochs<-length(tmp$metrics$loss)
plot(tmp)

my_prob <- my_model %>% predict(x_test1d)
my_pred <- apply(X = my_prob, MARGIN = 1, FUN = which.max) - 1

table(my_pred, y_test)
#>        y_test
#> my_pred    0    1    2    3    4    5    6    7    8    9
#>       0  962    0    8    2    0    6   11    0    8   11
#>       1    0 1110    1    0    3    1    3    8    2    4
#>       2    0    5  959   13    4    4    2   16    6    1
#>       3    1    1   22  958    1   27    0    7   33   13
#>       4    2    0    6    1  905    8    6    6    3   14
#>       5    5    2    0   12    1  809    9    1   15    4
#>       6    6    3    8    0    8   11  922    0    5    1
#>       7    1    1    7    7    1    2    0  963    4    8
#>       8    2   13   19   13    4   16    5    0  890    5
#>       9    1    0    2    4   55    8    0   27    8  948

mean(my_pred == y_test)
#> [1] 0.9426000

my_model %>%
  evaluate(x = x_test1d, y = y_test)
#>      loss  accuracy
#> 0.2071411 0.9426000


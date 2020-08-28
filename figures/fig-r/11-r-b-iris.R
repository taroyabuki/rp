pdf(file = "11-r-b-iris.pdf", width = 5.83, height = 4.13)

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

my_cb <- callback_early_stopping(patience = 20,               # 訓練停止条件
                                 restore_best_weights = TRUE) # 最善を保持

my_history <- my_model %>%
  fit(x = X,                   # 入力変数
      y = y,                   # 出力変数
      validation_split = 0.25, # 検証データの割合
      batch_size = 20,         # バッチサイズ
      epochs = 500,            # エポック数の上限
      callbacks = my_cb)       # エポックごとに行う処理

#plot(my_history)
#↑がうまく行かない場合
tmp <- my_history
tmp$params$epochs<-length(tmp$metrics$loss)
plot(tmp)

my_history

my_model %>% evaluate(x = X, y = y)

my_prob <- my_model %>% predict(X)
head(my_prob)

f <- function(i) { -log(my_prob[i, y[i] + 1]) }
1:length(y) %>% map_dbl(f) %>% mean

my_pred <- my_model %>% predict_classes(X)
my_pred <- apply(my_prob, 1, which.max) - 1
head(my_pred)

mean(my_pred == y)

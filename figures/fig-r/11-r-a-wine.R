pdf(file = "11-r-a-wine.pdf", width = 5.83, height = 4.13)

set.seed(0)

library(tidyverse)
my_url <- "https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/wine.csv"
tmp <- read_csv(my_url)
head(tmp)

my_data <- tmp[sample(nrow(tmp)), ] %>% scale
X <- my_data[, -1] # 入力変数
y <- my_data[,  1] # 出力変数

library(keras)
my_model <- keras_model_sequential() %>% # 層状のネットワーク
  layer_dense(
    units = 3,              # 隠れ層のニューロン数
    activation = "relu",    # 活性化関数
    input_shape = c(4)) %>% # 入力層のニューロン数
  layer_dense(units = 1)    # 出力層のニューロン数

my_model %>% compile(loss = "mean_squared_error",
                     optimizer = "rmsprop")

my_cb <- callback_early_stopping(patience = 20,               # 訓練停止条件
                                 restore_best_weights = TRUE) # 最善を保持

my_history <- my_model %>%
  fit(x = X,                   # 入力変数
      y = y,                   # 出力変数
      validation_split = 0.25, # 検証データの割合
      batch_size = 10,         # バッチサイズ
      epochs = 500,            # エポック数の上限
      callbacks = my_cb)       # エポックごとに行う処理

#plot(my_history)
#↑がうまく行かない場合
tmp <- my_history
tmp$params$epochs<-length(tmp$metrics$loss)
plot(tmp)

my_history
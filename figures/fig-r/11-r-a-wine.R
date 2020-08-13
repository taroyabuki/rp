pdf(file = "11-r-a-wine.pdf", width = 5.83, height = 4.13)

set.seed(0)

library(tidyverse)
my_url <- "https://raw.githubusercontent.com/taroyabuki/rp/master/data/wine.csv"
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

my_history <- my_model %>%
  fit(x = X,                   # 入力変数
      y = y,                   # 出力変数
      validation_split = 0.25, # 検証データの割合
      batch_size = 1,          # バッチサイズ
      epochs = 50)             # エポック数の上限

plot(my_history)

my_history

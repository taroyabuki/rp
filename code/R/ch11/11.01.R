## 11.1 Kerasによる回帰

library(keras)
library(tidyverse)

my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/wine.csv")
tmp <- read_csv(my_url)

## 11.1 Kerasによる回帰

my_data <- tmp[sample(nrow(tmp)), ]

## 11.1 Kerasによる回帰

X <- my_data %>%
  select(-LPRICE2) %>% scale
y <- my_data$LPRICE2

## 11.1 Kerasによる回帰

curve(activation_relu(x), -3, 3)

## 11.1 Kerasによる回帰

my_model <- keras_model_sequential() %>%
  layer_dense(units = 3, activation = "relu", input_shape = c(4)) %>%
  layer_dense(units = 1)

summary(my_model) # ネットワークの概要
# 割愛（Pythonの結果を参照）

## 11.1 Kerasによる回帰

my_model %>% compile(
  loss = "mse",
  optimizer = "rmsprop")

## 11.1 Kerasによる回帰

my_cb <- callback_early_stopping(
  patience = 20,
  restore_best_weights = TRUE)

## 11.1 Kerasによる回帰

my_history <- my_model %>%
  fit(x = X,
    y = y,
    validation_split = 0.25,
    batch_size = 10,
    epochs = 500,
    callbacks = list(my_cb),
    verbose = 0)

## 11.1 Kerasによる回帰

plot(my_history)

## 11.1 Kerasによる回帰

my_history
#> Final epoch (plot to see history):
#>     loss: 0.1218
#> val_loss: 0.1129


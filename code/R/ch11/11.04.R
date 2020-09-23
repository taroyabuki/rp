### 11.4.1 準備

library(keras)
tmp <- epitools::expand.table(Titanic)
tmp2 <- caret::dummyVars(formula = ~ ., data = tmp, fullRank = TRUE) %>%
  predict(tmp)
head(tmp2)
#>   Class.2nd Class.3rd Class.Crew Sex.Female Age.Adult Survived.Yes
#> 1         0         0          0          0         0            1
#> 2         0         0          0          0         0            1
#> 3         0         0          0          0         0            1
#> 4         0         0          0          0         0            1
#> 5         0         0          0          0         0            1
#> 6         0         0          0          0         1            0

my_data <- tmp2[sample(nrow(tmp2)), ] # シャッフル
X <- my_data[, -6] # 入力変数
y <- my_data[,  6] # 出力変数

### 11.4.2 ネットワークの構築

my_model <- keras_model_sequential() %>%
  layer_dense(units = 5, activation = "relu", input_shape = c(5)) %>%
  layer_dense(units = 1, activation = "sigmoid") # 変更箇所1

my_model %>% compile(
  loss = "binary_crossentropy", # 変更箇所2
  optimizer = "rmsprop",
  metric = c("accuracy"))

my_cb <- callback_early_stopping(patience = 20,               # 訓練停止条件
                                 restore_best_weights = TRUE) # 最善を保持

my_history <- my_model %>%
  fit(x = X,                   # 入力変数
      y = y,                   # 出力変数
      validation_split = 0.25, # 検証データの割合
      batch_size = 10,         # バッチサイズ
      epochs = 500,            # エポック数の上限
      callbacks = my_cb)       # エポックごとに行う処理

my_model %>% evaluate(x = X, y = y)
#>      loss  accuracy 
#> 0.4797515 0.7891867 

# 予測確率
p_A <- my_model %>% predict(X)

# 予測カテゴリ
y_A <- p_A > 0.5

# 正解率（訓練）
mean(y_A == y)
#> [1] 0.7891867

# 交差エントロピー（訓練）
-mean(log(
  p_A * y + (1 - p_A) * (!y)))
#> [1] 0.4797515


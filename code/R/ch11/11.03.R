### 11.3.1 交差エントロピー

y <- c(2, 1, 0, 1) # 正解

# 予測例A
p_A <- matrix(
  c(0.1, 0.1, 0.8,
    0.1, 0.7, 0.2,
    0.3, 0.4, 0.3,
    0.1, 0.8, 0.1),
  nrow = 4, byrow = TRUE)

# 予測例B
p_B <- matrix(
  c(0.1, 0.2, 0.7,
    0.2, 0.6, 0.2,
    0.2, 0.5, 0.3,
    0.2, 0.7, 0.1),
  nrow = 4, byrow = TRUE)

# 予測カテゴリA
y_A <- apply(X = p_A,
             MARGIN = 1,
             FUN = which.max) - 1
y_A
#> [1] 2 1 1 1

# 予測カテゴリB
y_B <- apply(X = p_B,
             MARGIN = 1,
             FUN = which.max) - 1
y_B
#> [1] 2 1 1 1

mean(y_A == y) # 正解率A
#> [1] 0.75

mean(y_B == y) # 正解率B
#> [1] 0.75

p <- to_categorical(y)
p
#>      [,1] [,2] [,3]
#> [1,]    0    0    1
#> [2,]    0    1    0
#> [3,]    1    0    0
#> [4,]    0    1    0

p_A * p
#>      [,1] [,2] [,3]
#> [1,]  0.0  0.0  0.8
#> [2,]  0.0  0.7  0.0
#> [3,]  0.3  0.0  0.0
#> [4,]  0.0  0.8  0.0

# 予測例Aの交差エントロピー
-mean(log(apply(X = p_A * p,
                MARGIN = 1,
                FUN = sum)))
#> [1] 0.5017337

# 予測例Bの交差エントロピー
-mean(log(apply(X = p_B * p,
                MARGIN = 1,
                FUN = sum)))
#> [1] 0.7084034

#### 11.3.2.1 出力変数が0から始まる整数の場合（表\ref{ネットワーク構築の基本原則

library(keras)
my_data <- iris[sample(nrow(iris)), ] # シャッフル
X <- scale(my_data[, -5])             # 標準化
y <- as.integer(my_data$Species) - 1  # 0から始まる整数

my_model <- keras_model_sequential() %>%
  layer_dense(units = 3, activation = "relu", input_shape = c(4)) %>%
  layer_dense(units = 3, activation = "softmax")

my_model %>% compile(loss = "sparse_categorical_crossentropy",
                     optimizer = "rmsprop",
                     metrics = c("accuracy")) # 正解率を記録する．

my_cb <- callback_early_stopping(patience = 20,               # 訓練停止条件
                                 restore_best_weights = TRUE) # 最善を保持

my_history <- my_model %>%
  fit(x = X,                   # 入力変数
      y = y,                   # 出力変数
      validation_split = 0.25, # 検証データの割合
      batch_size = 20,         # バッチサイズ
      epochs = 500,            # エポック数の上限
      callbacks = my_cb)       # エポックごとに行う処理

tmp <- my_history
tmp$params$epochs<-length(tmp$metrics$loss)
plot(tmp)

my_history
#>         loss: 0.06704
#>     accuracy: 0.9732
#>     val_loss: 0.144
#> val_accuracy: 0.9474

my_model %>% evaluate(x = X, y = y)
#>       loss   accuracy
#> 0.08633477 0.96666664

p_A <- my_model %>% predict(X)
head(p_A)
#>              [,1]         [,2]         [,3]
#> [1,] 5.627665e-08 6.949594e-03 9.930503e-01
#> [2,] 7.952168e-05 9.933645e-01 6.556002e-03
#> [3,] 2.432919e-09 6.402077e-03 9.935979e-01
#> [4,] 9.999996e-01 3.476715e-07 5.606830e-11
#> [5,] 9.999999e-01 1.118252e-07 1.196033e-11
#> [6,] 7.851200e-05 9.281746e-01 7.174686e-02

# 予測カテゴリ
y_A <- apply(X = p_A,
             MARGIN = 1,
             FUN = which.max) - 1

# 正解率（訓練）
mean(y_A == y)
#> [1] 0.96666664

p <- to_categorical(y)

# 交差エントロピー（訓練）
-mean(log(apply(X = p_A * p,
                MARGIN = 1,
                FUN = sum)))
#> [1] 0.08633477

#### 11.3.2.2 ワンホットエンコーディングの場合（表\ref{ネットワーク構築の基本原則

library(keras)
my_data <- iris[sample(nrow(iris)), ]      # シャッフル
X <- scale(my_data[, -5])                  # 標準化
p <- (as.integer(my_data$Species) - 1) %>% # 0から始まる整数
  to_categorical                           # ワンホットエンコーディング
head(p)
#>      [,1] [,2] [,3]
#> [1,]    0    1    0
#> [2,]    0    1    0
#> [3,]    1    0    0
#> [4,]    0    1    0
#> [5,]    0    1    0
#> [6,]    0    0    1

my_model <- keras_model_sequential() %>%
  layer_dense(units = 3, activation = "relu", input_shape = c(4)) %>%
  layer_dense(units = 3, activation = "softmax")

my_model %>% compile(
  loss = "categorical_crossentropy", # 変更箇所
  optimizer = "rmsprop",
  metrics = c("accuracy"))

my_cb <- callback_early_stopping(patience = 20,               # 訓練停止条件
                                 restore_best_weights = TRUE) # 最善を保持

my_history <- my_model %>%
  fit(x = X,                   # 入力変数
      y = p,                   # 出力変数
      validation_split = 0.25, # 検証データの割合
      batch_size = 20,         # バッチサイズ
      epochs = 500,            # エポック数の上限
      callbacks = my_cb)       # エポックごとに行う処理

my_model %>% evaluate(x = X, y = p)
#>       loss   accuracy 
#> 0.07238474 0.96666664 

# 正解カテゴリ
y <- apply(X = p,
           MARGIN = 1,
           FUN = which.max) - 1

# 予測確率
p_A <- my_model %>% predict(X)

# 予測カテゴリ
y_A <- apply(X = p_A,
             MARGIN = 1,
             FUN = which.max) - 1

# 正解率（訓練）
mean(y_A == y)
#> [1] 0.96666664

# 交差エントロピー（訓練）
-mean(log(apply(p_A * p, 1, sum)))
#> [1] 0.07238474

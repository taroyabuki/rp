## 8.6 補足：正則化

library(caret)
library(tidyverse)
my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/wine.csv")
my_data <- read_csv(my_url)

### 8.6.1 正則化の実践

A <- 2
B <- 0.1

my_model <- train(
  form = LPRICE2 ~ .,
  data = my_data,
  method = "glmnet",
  standardize = TRUE,
  tuneGrid = data.frame(
    lambda = A,
    alpha = B))

coef(my_model$finalModel, A)
#>                         1
#> (Intercept) -2.8015519302
#> WRAIN        .           
#> DEGREES      0.0832910512
#> HRAIN       -0.0004147386
#> TIME_SV      0.0023104647

my_test <- data.frame(
  WRAIN = 500, DEGREES = 17,
  HRAIN = 120, TIME_SV = 2)
my_model %>% predict(my_test)
#> [1] -1.430752

### 8.6.2 ペナルティの強さと係数の関係

library(ggfortify)
library(glmnetUtils)

my_data2 <- my_data %>% scale %>%
  as.data.frame

B <- 0.1

glmnet(
  form = LPRICE2 ~ .,
  data = my_data2,
  alpha = B) %>%
  autoplot(xvar = "lambda") +
  xlab("log A ( = log lambda)") +
  theme(legend.position =
          c(0.15, 0.25))

### 8.6.3 パラメータ$A,\,B$の決定

As <- seq(0, 0.1, length.out = 21)
Bs <- seq(0, 0.1, length.out =  6)

my_model <- train(
  form = LPRICE2 ~ ., data = my_data, method = "glmnet", standardize = TRUE,
  trControl = trainControl(method = "LOOCV"),
  tuneGrid = expand.grid(lambda = As, alpha  = Bs))

my_model$bestTune
#>   alpha lambda
#> 8     0  0.035

tmp <- "B ( = alpha)"
ggplot(my_model) +
  theme(legend.position = c(0, 1), legend.justification = c(0, 1)) +
  xlab("A ( = lambda)") +
  guides(shape = guide_legend(tmp), color = guide_legend(tmp))

y  <- my_data$LPRICE2
y_ <- my_model %>% predict(my_data)

RMSE(y_, y)          # RMSE（訓練）
#> [1] 0.2627595

my_model$results %>% # RMSE（検証）
  filter(RMSE == min(RMSE))
#>   alpha lambda      RMSE ...
#> 1     0 0.0595 0.3117092 ...

### 8.6.4 補足：RとPythonで結果を同じにする方法

my_sd <- function(x) { # 標準偏差'を計算する関数
  n <- length(x)
  sd(x) * sqrt((n - 1) / n)
}

y = my_data$LPRICE2
u = mean(y)
s = my_sd(y)
my_data2 <- my_data %>% mutate(LPRICE2 = (y - u) / s) # 対策1

A <- 2
B <- 0.1

library(glmnetUtils)
my_model <-
  glmnetUtils::glmnet( # 対策2
    form = LPRICE2 ~ .,
    data = my_data2,
    lambda = A,
    alpha = B,
    standardize = TRUE)

my_test <- data.frame(
  WRAIN = 500, DEGREES = 17,
  HRAIN = 120, TIME_SV = 2)
my_model %>%
  predict(newdata = my_test,
          exact = T) * s + u # 対策3
#>             s0
#> [1,] -1.434772

coef(my_model)
#>                       s0
#> (Intercept) -3.950668388
#> WRAIN        .          
#> DEGREES      0.243666704
#> HRAIN       -0.001531916
#> TIME_SV      0.009726541

tmp <- coef(my_model)
my_intercept <- tmp[1]
my_coef <- tmp[-1]

X = my_data[, -1]
X_mean <- apply(X, 2, mean)
X_sd <- apply(X, 2, my_sd)

my_intercept + sum(my_coef * X_mean)
#> [1] 8.881784e-16

my_coef * X_sd %>% as.data.frame
#>                   .
#> WRAIN    0.00000000
#> DEGREES  0.15761997
#> HRAIN   -0.10983842
#> TIME_SV  0.07870943


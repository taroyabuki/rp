### 4.3.1 一様乱数（整数）

x <- sample(x = 1:6,        # 範囲
            size = 10000,   # 個数
            replace = TRUE) # 重複あり
hist(x, breaks = 0:6) # ヒストグラム

### 4.3.2 一様乱数（連続）

x <- runif(n = 1000, # 個数
           min = 0,  # これ以上
           max = 1)  # これ未満
hist(x)

x <- runif(n = 1000,
           min = 1,
           max = 7) %>% as.integer
hist(x) # 結果は割愛

### 4.3.3 二項乱数

x <- rbinom(n = 1000,   # 乱数の数
            size = 100, # 試行回数
            prob = 0.5) # 確率
hist(x)

### 4.3.4 正規乱数

x <- rnorm(n = 1000,   # 乱数の数
           mean = 165, # 平均
           sd = 10)    # 標準偏差
hist(x)

#### 4.3.4.1 不偏性の具体例

n <- 100000
x <- replicate(n = n,
  expr = var(rnorm(n = 5, sd = 3)))

mean(x)
#> [1] 9.013718

hist(x)

x <- replicate(n = n,
  expr = sd(rnorm(n = 5, sd = 3)))

mean(x)
#> [1] 2.805624


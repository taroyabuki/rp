### 4.2.1 一様乱数（整数）

x <- sample(1:6,            # 範囲
            size = 10000,   # 個数
            replace = TRUE) # 重複あり
hist(x, breaks = 0:6) # ヒストグラム

### 4.2.2 一様乱数（連続）

x <- runif(n = 1000, # 個数
           min = 0,  # これ以上
           max = 1)  # これ未満
hist(x)

x <- runif(n = 1000,
           min = 1,
           max = 7) %>% as.integer
hist(x) # 結果は割愛

### 4.2.3 二項乱数

x <- rbinom(n = 1000,   # 乱数の数
            size = 100, # 試行回数
            prob = 0.5) # 確率
hist(x)

### 4.2.4 正規乱数

x <- rnorm(n = 1000,   # 乱数の数
           mean = 165, # 平均
           sd = 10)    # 標準偏差
hist(x)


pdf(file = "04-r-random-sample.pdf", width = 5.83, height = 4.13)

x <- sample(x = 1:6,        # 範囲
            size = 10000,   # 個数
            replace = TRUE) # 重複あり
hist(x, breaks = 0:6) # ヒストグラム

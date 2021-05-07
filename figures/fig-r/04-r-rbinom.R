pdf(file = "04-r-rbinom.pdf", width = 5.83, height = 4.13)

x <- rbinom(n = 1000,   # 乱数の数
            size = 100, # 試行回数
            prob = 0.5) # 確率
hist(x)

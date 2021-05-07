pdf(file = "04-r-rnorm.pdf", width = 5.83, height = 4.13)

x <- rnorm(n = 1000,   # 乱数の数
           mean = 165, # 平均
           sd = 10)    # 標準偏差
hist(x)

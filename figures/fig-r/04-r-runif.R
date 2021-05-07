pdf(file = "04-r-runif.pdf", width = 5.83, height = 4.13)

x <- runif(n = 1000, # 個数
           min = 0,  # これ以上
           max = 1)  # これ未満
hist(x)

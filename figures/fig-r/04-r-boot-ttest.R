pdf(file = "04-r-boot-ttest.pdf", width = 5.83, height = 4.13)

X <- c(32.1, 26.2, 27.5, 31.8, 32.1, 31.2, 30.1, 32.4, 32.3, 29.9, 29.6,
       26.6, 31.2, 30.9, 29.3)
Y <- c(35.4, 34.6, 31.1, 32.4, 33.3, 34.7, 35.3, 34.3, 32.1, 28.3, 33.3,
       30.5, 32.6, 33.3, 32.2)
Z <- X - Y # 対標本として扱う．

n <- 10^5
result <- replicate(n, mean(sample(Z, length(Z), replace = TRUE)))

hist(result)

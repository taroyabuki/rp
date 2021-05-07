pdf(file = "04-r-bias-var.pdf", width = 5.83, height = 4.13)

n <- 100000
x <- replicate(
  n,
  var(rnorm(n = 5, sd = 3)))

print(mean(x))

hist(x)

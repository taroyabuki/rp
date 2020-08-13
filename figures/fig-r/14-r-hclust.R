pdf(file = "14-r-hclust.pdf", width = 5.83, height = 4.13)

library(tidyverse)

name <- c("A", "B", "C", "D")
x    <- c(  0, -16,  10,  10)
y    <- c(  0,   0,  10, -15)
my_data <- data.frame(x, y, row.names = name)

my_dist <- dist(my_data)
my_result <- hclust(my_dist)

plot(my_result, hang = -1)
rect.hclust(my_result, k = 3)
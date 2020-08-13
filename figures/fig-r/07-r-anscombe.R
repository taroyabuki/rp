pdf(file = "07-r-anscombe.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(caret)
my_data <- data.frame(
  X1 = c(10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5),
  X2 = c(8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8),
  Y1 = c(8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68),
  Y2 = c(9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74),
  Y3 = c(7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73),
  Y4 = c(6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89))

g1 <- ggplot(data = my_data,
             mapping = aes(x = X1, y = Y1)) +
  xlim(0, 20) + ylim(0, 15) +
  geom_point() +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE, fullrange = TRUE) +
  ggtitle("a: {X1, Y1}")

g2 <- ggplot(data = my_data,
             mapping = aes(x = X1, y = Y2)) +
  xlim(0, 20) + ylim(0, 15) +
  geom_point() +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE, fullrange = TRUE) +
  ggtitle("b: {X1, Y2}")

g3 <- ggplot(data = my_data,
             mapping = aes(x = X1, y = Y3)) +
  xlim(0, 20) + ylim(0, 15) +
  geom_point() +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE, fullrange = TRUE) +
  ggtitle("c: {X1, Y3}")

g4 <- ggplot(data = my_data,
             mapping = aes(x = X2, y = Y4)) +
  xlim(0, 20) + ylim(0, 15) +
  geom_point() +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE, fullrange = TRUE) +
  ggtitle("d: {X2, Y4}")

gridExtra::grid.arrange(g1, g2, g3, g4, ncol = 2)

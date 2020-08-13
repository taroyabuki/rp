pdf(file = "07-r-regression.pdf", width = 5.83, height = 4.13)

library(tidyverse)
my_data <- cars

g1 <- my_data %>% ggplot(aes(x = speed, y = dist)) +
  coord_cartesian(ylim = c(0, 120)) +
  geom_point() +
  ggtitle("data")

g2 <- my_data %>% ggplot(aes(x = speed, y = dist)) +
  coord_cartesian(ylim = c(0, 120)) +
  geom_point(size = 0) +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE) +
  ggtitle("model")

tmp <- data.frame(speed = 21.5, dist = 66.96769)

g3 <- my_data %>% ggplot(aes(x = speed, y = dist)) +
  coord_cartesian(ylim = c(0, 120)) +
  geom_point(size = 0) +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE) +
  geom_pointrange(data = tmp, aes(ymin = 0, ymax = dist), linetype = "dotted") +
  geom_errorbarh(data = tmp, aes(xmin = 0, xmax = speed), linetype = "dotted") +
  ggtitle("prediction")

gridExtra::grid.arrange(g1, g2, g3, ncol = 3)
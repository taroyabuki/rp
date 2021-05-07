pdf(file = "07-r-regression.pdf", width = 5.83, height = 4.13)

library(tidyverse)

my_data <- cars
tmp <- data.frame(speed = 21.5, dist = 67)
my_data %>% ggplot(aes(x = speed, y = dist)) +
  coord_cartesian(xlim = c(4, 25), ylim = c(0, 120)) +
  geom_point() +
  stat_smooth(formula = y ~ x, method = "lm") +
  geom_pointrange(data = tmp, aes(ymin = -9, ymax = dist),  linetype = "dotted") +
  geom_pointrange(data = tmp, aes(xmin =  0, xmax = speed), linetype = "dotted")

pdf(file = "07-r-cars.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(caret)
my_data <- cars

ggplot(data = my_data, mapping = aes(x = speed, y = dist)) +
  geom_point() +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE)
pdf(file = "07-r-plot.pdf", width = 5.83, height = 4.13)

library(tidyverse)
my_data <- cars

my_data %>%
  ggplot(aes(x = speed, y = dist)) +
  geom_point()

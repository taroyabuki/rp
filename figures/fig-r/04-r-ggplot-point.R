pdf(file = "04-r-ggplot-point.pdf", width = 5.83, height = 4.13)

library(tidyverse)

iris %>%
  ggplot(aes(x = Sepal.Length,
             y = Sepal.Width)) +
  geom_point()

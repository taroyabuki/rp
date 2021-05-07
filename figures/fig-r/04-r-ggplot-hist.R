pdf(file = "04-r-ggplot-hist.pdf", width = 5.83, height = 4.13)

library(tidyverse)

iris %>%
  ggplot(aes(x = Sepal.Length)) +
  geom_histogram(bins = 8)

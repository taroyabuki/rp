pdf(file = "04-r-ggplot-box.pdf", width = 5.83, height = 4.13)

library(tidyverse)

iris %>%
  pivot_longer(-Species) %>%
  ggplot(aes(
    x = factor(name,
               levels = names(iris)),
    y = value)) +
  geom_boxplot() +
  xlab(NULL)

pdf(file = "04-r-pvalue1.pdf", width = 5.83, height = 4.13)

library(tidyverse)

t <- 4 / 10
n <- 15
x <- 0:n
my_pr  <- dbinom(x, n, t)
my_pr2 <- dbinom(2, n, t)

my_data <- data.frame(x = x) %>%
  mutate(probability = my_pr) %>%
  mutate(color = my_pr <= my_pr2)

my_data %>% ggplot(aes(x = x, y = probability, color = color)) +
  geom_point(size = 3) +
  geom_linerange(aes(ymin = 0, ymax = probability), ) +
  geom_hline(yintercept = my_pr2) +
  theme(legend.position = "none")

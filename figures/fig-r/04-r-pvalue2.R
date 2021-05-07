pdf(file = "04-r-pvalue2.pdf", width = 5.83, height = 4.13)

library(tidyverse)

t <- 4 / 10
n <- 15
x <- 0:n
my_pr  <- dbinom(x, n, t)

my_data <- data.frame(x = x) %>%
  mutate(probability = my_pr) %>%
  mutate(color = x <= 2) # “–‚½‚é‰ñ”‚ª2‰ñˆÈ‰º

my_data %>% ggplot(aes(x = x, y = probability, color = color)) +
  geom_point(size = 3) +
  geom_linerange(aes(ymin = 0, ymax = probability), ) +
  theme(legend.position = "none")

pdf(file = "04-r-iris.pdf", width = 5.83, height = 4.13)

library(tidyverse)
my_df <- psych::describe(iris[, -5])

tmp = rownames(my_df)
my_df %>% ggplot(aes(x = factor(tmp, levels = tmp), y = mean)) +
  geom_col() +
  geom_errorbar(aes(ymin = mean - se, ymax = mean + se)) +
  xlab(NULL)

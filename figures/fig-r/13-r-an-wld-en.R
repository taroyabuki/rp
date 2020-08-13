pdf(file = "13-r-an-wld-en.pdf", width = 5.83, height = 4.13)

library(tidyverse)

my_data <- read_csv("https://raw.githubusercontent.com/taroyabuki/rp/master/data/an_wld_en.csv")
my_data %>% ggplot(aes(x = year, y = value)) +
  geom_point() + 
  geom_line() +
  stat_smooth(formula = y ~ x, method = "lm", se = FALSE)


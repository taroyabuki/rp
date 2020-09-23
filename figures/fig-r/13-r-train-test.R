pdf(file = "13-r-train-test.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(tsibble)
tmp <- read_csv("https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/an_wld_en.csv")
my_data <- tmp %>% as_tsibble(index = year)

my_index = 1:109
my_train <- my_data[ my_index, ] # 訓練データ
my_test  <- my_data[-my_index, ] # 検証データ

my_data %>%
  mutate(name = rep(c("train", "test"), c(109, 20))) %>%
  ggplot(aes(x = year, y = world, color = name)) +
    geom_line()

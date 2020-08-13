pdf(file = "13-r-an-wld-en-rollmean.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(tsibble)
library(zoo)
my_data <- read_csv("https://raw.githubusercontent.com/taroyabuki/rp/master/data/an_wld_en.csv")
my_ts <- my_data %>% as_tsibble(index = year)

my_ts$mean5 = my_ts$value %>%
  rollmean(k = 5,            # 5年の平均
           fill = NA,        # 計算できないところはNa
           align = "right") # 過去の値を使う．

my_ts %>% ggplot(aes(x = year, y = value)) +
  geom_point() +                                # 散布図
  geom_line() +                                 # 折れ線グラフ
  stat_smooth(formula = y ~ x, method = "lm",   # 線形回帰分析（出力変数はy）
              se = FALSE,                       # 信頼区間は描かない．
              color = "blue",                   # 青
              size = 1) +                       # 線を太くする．
  geom_line(mapping = aes(x = year, y = mean5), # 移動平均
            color = "red",                      # 赤
            size = 1)                           # 線を太くする．
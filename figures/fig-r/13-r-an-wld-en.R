pdf(file = "13-r-an-wld-en.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(tsibble)
my_data <- read_csv("https://raw.githubusercontent.com/taroyabuki/rp/master/data/an_wld_en.csv")

library(zoo)
my_data$mean5 <- my_data$world %>%
  rollmean(k = 5,           # 移動平均（5年）
           fill = NA,       # 計算できないところはNa
           align = "right") # 過去の値を使う．

# 回帰分析の結果をデータフレームに追加する．
library(caret)
my_data$lm <- train(form = world ~ year, data = my_data, method = "lm") %>%
  predict(my_data)
head(my_data)

my_data %>% pivot_longer(-year) %>% head # 整然データ

# 折れ線（元データ，移動平均，回帰分析）と散布図（元データ）
my_data %>% pivot_longer(-year) %>%
  ggplot(aes(x = year)) +
  geom_line(aes(y = value, color = name)) +
  geom_point(data = my_data, mapping = aes(y = world))

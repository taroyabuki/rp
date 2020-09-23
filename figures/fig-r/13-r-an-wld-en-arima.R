pdf(file = "13-r-an-wld-en-arima.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(tsibble)
library(forecast)

tmp <- read_csv("https://raw.githubusercontent.com/taroyabuki/fromzero/master/data/an_wld_en.csv")
my_data <- tmp %>% as_tsibble(index = year)
my_model <- my_data %>% auto.arima() # すべてのデータを使う．
my_df <- my_model %>% forecast(30)   # 30 年分の予測
autoplot(my_df)
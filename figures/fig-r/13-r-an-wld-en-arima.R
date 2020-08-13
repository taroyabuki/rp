pdf(file = "13-r-an-wld-en-arima.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(tsibble)
library(forecast)

my_data <- read_csv("https://raw.githubusercontent.com/taroyabuki/rp/master/data/an_wld_en.csv")
my_ts <- my_data %>% select(year, value) %>% as_tsibble(index = year)
my_ts_model <- my_ts %>% auto.arima()
my_ts_pred <- my_ts_model %>% forecast(30)
my_ts_pred %>% autoplot
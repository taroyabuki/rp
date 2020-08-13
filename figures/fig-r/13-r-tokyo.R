pdf(file = "13-r-tokyo.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(tsibble)
library(forecast)

my_data <- read_csv("https://raw.githubusercontent.com/taroyabuki/rp/master/data/tokyo-max-temp-2015--2019.csv",
                    locale = locale(encoding="sjis"),
                    skip = 5,
                    col_names = c("date", "value", "quality", "no"))
my_ts <- my_data %>%
  mutate(month = yearmonth(my_data$date)) %>%
  select(month, value) %>%
  as_tsibble(index = month)
my_ts_model <- my_ts %>% auto.arima()
my_ts_pred <- my_ts_model %>% forecast(12)
my_ts_pred %>% autoplot
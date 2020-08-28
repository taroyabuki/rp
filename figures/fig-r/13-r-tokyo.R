pdf(file = "13-r-tokyo.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(tsibble)
library(forecast)

my_url <- "https://raw.githubusercontent.com/taroyabuki/rp/master/data/tokyo-max-temp-2015--2019.csv"
tmp <- read_csv(my_url,
                locale = locale(encoding="sjis"),
                skip = 5,
                col_names = c("date", "tokyo", "quality", "no"))

my_data <- tmp %>%
  mutate(month = yearmonth(tmp$date)) %>%
  select(month, tokyo) %>%
  as_tsibble(index = month)

my_model <- my_data %>% auto.arima
my_df <- my_model %>% forecast(24)
autoplot(my_df)
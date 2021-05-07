pdf(file = "11-r-automl.pdf", width = 5.83, height = 4.13)

library(h2o)
library(tidyverse)

h2o.init()
h2o.no_progress()

my_data <- cars
my_frame <- as.h2o(my_data)

y <- "dist"

my_model <- h2o.automl(y = y,
                       training_frame = my_frame,
                       max_runtime_secs = 30)

my_model@leaderboard

tmp <- data.frame(speed = seq(from = min(my_data$speed),
                              to = max(my_data$speed),
                              length.out = 100))
my_pred <- my_model %>% h2o.predict(as.h2o(tmp)) %>% as.data.frame
tmp$dist <- my_pred$predict

my_data %>%
  ggplot(aes(x = speed,
             y = dist,
             color = "data")) +
  geom_point() +
  geom_line(data = tmp, mapping = aes(color = "model"))

h2o.shutdown(prompt = FALSE)

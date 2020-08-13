pdf(file = "14-r-abcd.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(ggrepel)

name <- c("A", "B", "C", "D")
x    <- c(  0, -16,  10,  10)
y    <- c(  0,   0,  10, -15)
my_data <- data.frame(x, y, row.names = name)

my_data %>% ggplot(mapping = aes(x = x, y = y, label = row.names(my_data))) +
  geom_point(size = 3) +
  geom_text_repel()
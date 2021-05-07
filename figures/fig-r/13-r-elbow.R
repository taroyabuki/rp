pdf(file = "13-r-elbow.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(factoextra)

my_data <- iris[, -5]
fviz_nbclust(my_data, kmeans, method = "wss")

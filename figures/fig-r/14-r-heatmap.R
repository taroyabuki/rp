pdf(file = "14-r-heatmap.pdf", width = 5.83, height = 4.13)

library(tidyverse)

my_data <- data.frame(
  language = c(  0, 20, 20, 25, 22, 17),
  english  = c(  0, 20, 40, 20, 24, 18),
  math     = c(100, 20,  5, 30, 17, 25),
  science  = c(  0, 20,  5, 25, 16, 23),
  society  = c(  0, 20, 30,  0, 21, 17))
row.names(my_data) <- c("A", "B", "C", "D", "E", "F")

my_data %>%
  scale %>%     # 標準化，
  as.matrix %>% # 行列にしてから，
  gplots::heatmap.2( # 可視化
    distfun = function(m) { dist(x = m, method = 'euclidean') },
    hclustfun = function(d) { hclust(d = d, method = 'complete') },
    cexRow = 1, # 行ラベルのサイズ
    cexCol = 1) # 列ラベルのサイズ
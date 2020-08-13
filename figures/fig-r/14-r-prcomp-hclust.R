pdf(file = "14-r-prcomp-hclust.pdf", width = 5.83, height = 4.13)

library(tidyverse)

my_data <- iris[, -5] # アヤメのデータ

# 主成分分析
my_result <- prcomp(my_data)

# 階層的クラスター分析を使う場合
my_cluster <- my_data %>% scale %>% dist %>% hclust %>% cutree(3)

# 非階層的クラスター分析を使う場合
# my_cluster <- (my_data %>% scale %>% kmeans(3))$cluster

my_result %>%
  ggbiplot::ggbiplot(
    scale = 0,
    labels = row.names(my_data),
    groups = as.factor(my_cluster))

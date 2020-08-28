pdf(file = "14-r-pca-clusters.pdf", width = 5.83, height = 4.13)

library(tidyverse)
# アヤメのデータ
my_data <- iris[, -5]

# 主成分分析
my_result <- prcomp(my_data)

# 階層的クラスター分析
my_cluster <- my_data %>% scale %>% dist %>% hclust %>% cutree(3)

# 非階層的クラスター分析
#my_cluster <- (my_data %>% scale %>% kmeans(3))$cluster

my_result %>%
  ggbiplot::ggbiplot(
    scale = 0,
    groups = as.factor(my_cluster)) # クラスターによるグループ分け
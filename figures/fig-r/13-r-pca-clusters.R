pdf(file = "13-r-pca-clusters.pdf", width = 5.83, height = 4.13)

library(tidyverse)
my_data <- iris[, -5] %>% scale

my_result <- prcomp(my_data)$x %>% as.data.frame # 主成分分析

# 非階層的クラスタ分析の場合
my_result$cluster <- (my_data %>% scale %>% kmeans(3))$cluster %>% as.factor

# 階層的クラスタ分析の場合
#my_result$cluster <- my_data %>% dist %>% hclust %>% cutree(3) %>% as.factor

my_result %>%
  ggplot(aes(x = PC1, y = PC2, color = cluster)) +
  geom_point(shape = iris$Species) +
  theme(legend.position = "none")

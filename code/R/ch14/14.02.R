### 14.2.1 距離

my_data <- data.frame(
  x = c(  0, -16,  10,  10),
  y = c(  0,   0,  10, -15),
  row.names = c("A", "B", "C", "D"))

# ユークリッド距離
my_data %>% dist
# あるいは
my_data %>% dist("euclidian")

#>          A        B        C
#> B 16.00000                  
#> C 14.14214 27.85678         
#> D 18.02776 30.01666 25.00000

# マンハッタン距離
my_data %>% dist("manhattan")
#>    A  B  C
#> B 16      
#> C 20 36   
#> D 25 41 25

#### 14.2.2.1 Rの場合

library(tidyverse)
my_data <- data.frame(
  x = c(  0, -16,  10,  10),
  y = c(  0,   0,  10, -15),
  row.names = c("A", "B", "C", "D"))

# 距離の計算
my_dist <- my_data %>% dist
# あるいは
my_dist <- my_data %>% dist("euclidian")

# 階層的クラスター分析
my_result <- my_dist %>% hclust
# あるいは
my_result <- my_dist %>% hclust("complete")

plot(my_result, hang = -1)    # デンドログラム
rect.hclust(my_result, k = 3) # クラスター（3個）の明示
# あるいは
factoextra::fviz_dend(my_result, # デンドログラム（図14.3の左）
                      k = 3,     # クラスター（3個）の明示
                      rect = T, rect_fill = T) # クラスターを囲む長方形

# クラスター数を3にする場合に，各点がどのクラスターに属しているかを確認する．
my_result %>% cutree(3)
#> A B C D 
#> 1 2 1 3 

#### 14.2.3.1 Rの場合

library(tidyverse)
my_data <- data.frame(
  language = c(  0, 20, 20, 25, 22, 17),
  english  = c(  0, 20, 40, 20, 24, 18),
  math     = c(100, 20,  5, 30, 17, 25),
  science  = c(  0, 20,  5, 25, 16, 23),
  society  = c(  0, 20, 30,  0, 21, 17),
  row.names = c("A", "B", "C", "D", "E", "F"))

my_data %>%
  scale %>%          # 標準化，
  as.matrix %>%      # 行列にしてから，
  gplots::heatmap.2( # 可視化
    distfun = function(m) { dist(x = m, method = 'euclidean') },
    hclustfun = function(d) { hclust(d = d, method = 'complete') },
    cexRow = 1, # 行ラベルのサイズ
    cexCol = 1) # 列ラベルのサイズ

#### 14.2.4.1 Rの場合

my_data <- data.frame(
  x = c(  0, -16,  10,  10),
  y = c(  0,   0,  10, -15),
  row.names = c("A", "B", "C", "D"))

# クラスター数を3として，非階層的クラスター分析を行う．
my_result <- my_data %>% kmeans(3)

# 各データがどのクラスターに属しているかを確認する．
my_cluster <- my_result$cluster
my_cluster
#> A B C D 
#> 2 3 2 1 

### 14.2.5 主成分分析とクラスター分析

library(tidyverse)
# アヤメのデータ
my_data <- iris[, -5]

# 主成分分析
my_result <- prcomp(my_data)

# 階層的クラスター分析
my_cluster <- my_data %>% scale %>% dist %>% hclust %>% cutree(3)

# 非階層的クラスター分析
#my_cluster <- (my_data %>% scale %>% kmeans(3))$cluster

# バイプロット
my_result %>%
  ggbiplot::ggbiplot(
    scale = 0,
    groups = as.factor(my_cluster)) # クラスターによるグループ分け


## 8.1 ワインの生育条件と価格

library(caret)
library(tidyverse)

my_url <- "http://www.liquidasset.com/winedata.html"
tmp <- read.table(file = my_url,   # 読み込む対象
                  header = TRUE,   # 1行目は変数名
                  na.string = ".", # 欠損値を表す文字列
                  skip = 62,       # 読み飛ばす行数
                  nrows = 38)      # 読み込む行数
psych::describe(tmp)
#>         vars  n    mean     sd  median trimmed    mad     min     max  range  skew kurtosis    se
#> OBS        1 38   19.50  11.11   19.50   19.50  14.08    1.00   38.00  37.00  0.00    -1.30  1.80
#> VINT       2 38 1970.50  11.11 1970.50 1970.50  14.08 1952.00 1989.00  37.00  0.00    -1.30  1.80
#> LPRICE2    3 27   -1.45   0.63   -1.51   -1.49   0.72   -2.29    0.00   2.29  0.41    -0.82  0.12
#> WRAIN      4 38  605.00 135.28  586.50  603.06 174.95  376.00  845.00 469.00  0.15    -1.10 21.95
#> DEGREES    5 37   16.52   0.66   16.53   16.55   0.67   14.98   17.65   2.67 -0.34    -0.73  0.11
#> HRAIN      6 38  137.00  66.74  120.50  132.19  59.30   38.00  292.00 254.00  0.69    -0.20 10.83
#> TIME_SV    7 38   12.50  11.11   12.50   12.50  14.08   -6.00   31.00  37.00  0.00    -1.30  1.80

my_data <- na.omit(tmp[, -c(1, 2)])
head(my_data)
#>    LPRICE2 WRAIN DEGREES HRAIN TIME_SV
#> 1 -0.99868   600 17.1167   160      31
#> 2 -0.45440   690 16.7333    80      30
#> 4 -0.80796   502 17.1500   130      28
#> 6 -1.50926   420 16.1333   110      26
#> 7 -1.71655   582 16.4167   187      25
#> 8 -0.41800   485 17.4833   187      24

nrow(my_data)
#> [1] 27

my_data %>% write_csv("wine.csv")

library(tidyverse)
#my_data <- read_csv("wine.csv") # 作ったファイルを使う場合
my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/wine.csv")
my_data <- read_csv(my_url)


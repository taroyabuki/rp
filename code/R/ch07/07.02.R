### 7.2.1 Rの場合

library(tidyverse)
library(caret)

my_data <- cars # データに別名を付ける．

dim(my_data) # データ数の表示
#> [1] 50  2

head(my_data) # 最初の数件の表示
#>   speed dist
#> 1     4    2
#> 2     4   10
#> 3     7    4
#> 4     7   22
#> 5     8   16
#> 6     9   10

psych::describe(my_data) # 基本統計量
#>       vars  n  mean    sd median trimmed   mad min max range  skew kurtosis   se
#> speed    1 50 15.40  5.29     15   15.47  5.93   4  25    21 -0.11    -0.67 0.75
#> dist     2 50 42.98 25.77     36   40.88 23.72   2 120   118  0.76     0.12 3.64

plot(my_data) # 結果は割愛


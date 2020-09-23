### 9.3.1 Rの場合

library(tidyverse)
library(caret)
my_data <- iris
my_model <- train(form = Species ~ ., data = my_data, method = "knn")

my_test <- tribble(
~Sepal.Length, ~Sepal.Width, ~Petal.Length, ~Petal.Width,
          5.0,          3.5,           1.5,          0.5,
          6.5,          3.0,           5.0,          2.0)

my_model %>% predict(my_test)
#> [1] setosa    virginica
#> Levels: setosa versicolor virginica

my_model %>% predict(my_test, type = "prob")
#>   setosa versicolor virginica
#> 1      1      0.000     0.000
#> 2      0      0.125     0.875


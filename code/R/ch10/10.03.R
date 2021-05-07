### 10.3.1 質的入力変数を含むデータでの学習

library(caret)
library(PRROC)
library(tidyverse)

my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/titanic.csv")
my_data <- read_csv(my_url)

head(my_data)
#> # A tibble: 6 x 4
#>   Class Sex   Age   Survived
#>   <chr> <chr> <chr> <chr>   
#> 1 1st   Male  Child Yes     
#> 2 1st   Male  Child Yes     
#> 3 1st   Male  Child Yes     
#> 4 1st   Male  Child Yes     
#> 5 1st   Male  Child Yes     
#> 6 1st   Male  Adult No

### 10.3.2 分類木

my_model <- train(form = Survived ~ ., data = my_data, method = "rpart2",
                  tuneGrid = data.frame(maxdepth = 2),
                  trControl = trainControl(method = "LOOCV"))

#### 10.3.2.1 分類木の描画

rpart.plot::rpart.plot(my_model$finalModel, extra = 1)

#### 10.3.2.2 分類木の評価

my_model$results
#>   maxdepth  Accuracy     Kappa
#> 1        2 0.7832803 0.4096365

y <- my_data$Survived
tmp <- my_model %>% predict(newdata = my_data, type = "prob")
y_score <- tmp$Yes

my_roc <- roc.curve(scores.class0 = y_score[y == "Yes"],
                    scores.class1 = y_score[y == "No"],
                    curve = TRUE)
my_roc$auc
#> [1] 0.7114887

my_roc %>% plot(xlab = "False Positive Rate",
                ylab = "True Positive Rate",
                legend = FALSE)


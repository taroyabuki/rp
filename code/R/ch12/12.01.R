## 12.1 準備

library(keras)
#c(c(x_train, y_train), c(x_test, y_test)) %<-% dataset_mnist()
#↑がうまく行かない場合
c(c(x_train, y_train), c(x_test, y_test)) %<-% readRDS("/tmp/mnist.obj")

dim(x_train)
#> [1] 60000    28    28

x_train[5, , ]

plot(as.raster(x = x_train[5, , ],
               max = max(x_train)))

c(min(x_train), max(x_train))
#> [1]   0 255

x_train <- x_train / 255
x_test  <- x_test  / 255

head(y_train)
#> [1] 5 0 4 1 9 2

my_index <- sample(1:60000, 6000)
x_train <- x_train[my_index, , ]
y_train <- y_train[my_index]


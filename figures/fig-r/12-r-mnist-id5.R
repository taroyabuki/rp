pdf(file = "12-r-mnist-id5.pdf", width = 5.83, height = 4.13)

library(tidyverse)
library(caret)
library(keras)
#c(c(x_train, y_train), c(x_test, y_test)) %<-% dataset_mnist()
#↑がうまく行かない場合
c(c(x_train, y_train), c(x_test, y_test)) %<-% readRDS("/tmp/mnist.obj")

plot(as.raster(x = x_train[5, , ], max = max(x_train)))
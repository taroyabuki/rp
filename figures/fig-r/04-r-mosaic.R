pdf(file = "04-r-mosaic.pdf", width = 5.83, height = 4.13)

my_df <- data.frame(
  Species = iris$Species,
  w_Sepal = iris$Sepal.Width > 3)

mosaicplot(
  formula = ~ Species + w_Sepal,
  data = my_df)

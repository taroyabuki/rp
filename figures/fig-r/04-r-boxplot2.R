pdf(file = "04-r-boxplot2.pdf", width = 5.83, height = 4.13)

boxplot(
  formula = Sepal.Length ~ Species,
  data = iris)

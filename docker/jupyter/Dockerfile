FROM jupyter/datascience-notebook

RUN pip install \
  keras \
  pca \
  pmdarima \
  tensorflow \
  xgboost

RUN R -e 'devtools::install_version("foreign", version = "0.8.76", repos = "http://cran.us.r-project.org")'

RUN R -e 'install.packages(c(\
  "doParallel",\
  "e1071",\
  "epitools",\
  "factoextra",\
  "furrr",\
  "ggrepel",\
  "gridExtra",\
  "igraph",\
  "ROCR",\
  "rpart.plot",\
  "tsibble",\
  "xgboost"\
  ), repos="https://cran.rstudio.com")'

RUN R -e 'devtools::install_github(c(\
  "rstudio/keras",\
  "vqv/ggbiplot"\
  ))'

RUN Rscript -e '\
  saveRDS(keras::dataset_mnist(), "/tmp/mnist.obj");'

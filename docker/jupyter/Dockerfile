FROM jupyter/datascience-notebook

RUN pip install \
  keras \
  pca \
  pmdarima \
  tensorflow \
  xgboost

RUN R -e 'install.packages(c(\
  "doParallel",\
  "e1071",\
  "epitools",\
  "furrr",\
  "ggfortify", \
  "ggrepel",\
  "gridExtra",\
  "ROCR",\
  "rpart.plot",\
  "tsibble",\
  "xgboost"\
  ), repos="https://cran.rstudio.com")'

RUN R -e 'devtools::install_github(c(\
  "rstudio/keras"\
  ))'

RUN Rscript -e '\
  saveRDS(keras::dataset_mnist(), "/tmp/mnist.obj");'

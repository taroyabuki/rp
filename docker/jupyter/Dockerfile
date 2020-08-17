FROM jupyter/datascience-notebook

RUN pip install \
  keras \
  tensorflow \
  xgboost

RUN R -e 'install.packages(c(\
  "doParallel",\
  "e1071",\
  "epitools",\
  "furrr",\
  "ggrepel",\
  "gridExtra",\
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

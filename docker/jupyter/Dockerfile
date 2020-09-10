FROM jupyter/datascience-notebook

RUN pip install \
  keras \
  lxml \
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

USER root
RUN rm /etc/dpkg/dpkg.cfg.d/excludes \
  && apt-get update \
  && apt-get --reinstall install -y man-db coreutils manpages \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
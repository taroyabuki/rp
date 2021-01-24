FROM jupyter/datascience-notebook

RUN pip install \
  fbprophet \
  keras \
  lxml \
  pca \
  pmdarima \
  tensorflow \
  xgboost

#RUN Rscript -e 'devtools::install_version("foreign", version = "0.8.76", repos = "http://cran.us.r-project.org");\
RUN Rscript -e '\
  Sys.setenv(DOWNLOAD_STATIC_LIBV8=1); \
  install.packages(c(\
    "doParallel",\
    "e1071",\
    "epitools",\
    "factoextra",\
    "furrr",\
    "ggrepel",\
    "gridExtra",\
    "igraph",\
    "prophet",\
    "psych",\
    "ROCR",\
    "rpart.plot",\
    "xgboost"\
  ), repos="https://cran.rstudio.com");\
  devtools::install_github(c(\
    "rstudio/keras",\
    "vqv/ggbiplot"\
  ));\
  saveRDS(keras::dataset_mnist(), "/tmp/mnist.obj");'

USER root

RUN rm /etc/dpkg/dpkg.cfg.d/excludes \
  && apt-get update \
  && apt-get install \
    less \
  && apt-get --reinstall install -y man-db coreutils manpages \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && bash -c 'yes | unminimize' # ad hoc

WORKDIR /home/jovyan

#必要かも
#    "tsibble",\

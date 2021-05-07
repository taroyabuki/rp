FROM jupyter/datascience-notebook

# use pystan==2.18.0.0 for fbprophet (2021/05)
RUN pip install \
  fbprophet \
  graphviz \
  h2o \
  japanize_matplotlib \
  keras \
  lxml \
  pandarallel \
  pca \
  pmdarima \
  pystan==2.18.0.0 \
  tensorflow \
  xgboost

#RUN Rscript -e 'devtools::install_version("foreign", version = "0.8.76", repos = "http://cran.us.r-project.org");\
RUN Rscript -e '\
  Sys.setenv(DOWNLOAD_STATIC_LIBV8=1); \
  install.packages(c(\
    "doParallel",\
    "e1071",\
    "epitools",\
    "exactci",\
    "fable",\
    "factoextra",\
    "furrr",\
    "ggrepel",\
    "gridExtra",\
    "ggfortify",\
    "glmnetUtils",\
    "h2o",\
    "igraph",\
    "neuralnet",\
    "pastecs",\
    "prophet",\
    "PRROC",\
    "psych",\
    "rpart.plot",\
    "tsibble",\
    "vcd",\
    "xgboost"\
  ), repos="https://cran.rstudio.com");\
  devtools::install_github(c(\
    "haleyjeppson/ggmosaic",\
    "rstudio/keras",\
    "vqv/ggbiplot"\
  ));'

USER root

RUN rm /etc/dpkg/dpkg.cfg.d/excludes \
  && apt-get update \
  && apt-get install -y \
    default-jdk \
    dnsutils \
    graphviz \
    iputils-ping \
    less \
    net-tools \
  && apt-get --reinstall install -y man-db coreutils manpages \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && bash -c 'yes | unminimize' # ad hoc

WORKDIR /home/jovyan

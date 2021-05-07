FROM jupyter/datascience-notebook:python-3.8.8

# pystan==2.18.0.0 for fbprophet
RUN pip install \
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

RUN pip install fbprophet

#RUN Rscript -e 'devtools::install_version("foreign", version = "0.8.76", repos = "http://cran.us.r-project.org");\
RUN Rscript -e '\
  Sys.setenv(DOWNLOAD_STATIC_LIBV8=1); \
  install.packages("pak", repos = "https://r-lib.github.io/p/pak/dev/"); \
  pak::pkg_install(c(\
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
    "xgboost",\
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

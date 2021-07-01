FROM rocker/tidyverse

USER rstudio

RUN Rscript -e ' \
  install.packages("pak", repos = "https://r-lib.github.io/p/pak/dev/"); \
  pak::pkg_install(c( \
    "caret", \
    "doParallel", \
    "e1071", \
    "epitools", \
    "factoextra", \
    "forecast", \
    "furrr", \
    "ggrepel", \
    "gplots", \
    "gridExtra", \
    "igraph", \
    "MLmetrics", \
    "pastecs", \
    "prophet", \
    "PRROC", \
    "psych", \
    "randomForest", \
    "rpart.plot", \
    "vcd", \
    "xgboost", \
    "haleyjeppson/ggmosaic", \
    "rstudio/keras", \
    "vqv/ggbiplot" \
  )); \
  reticulate::install_miniconda(); \
  keras::install_keras();'

USER root

RUN rm /etc/dpkg/dpkg.cfg.d/excludes \
  && apt-get update \
  && apt-get install -y \
    curl \
    dnsutils \
    iputils-ping \
    less \
    libglpk-dev \
    libnode64 \
    libtbb2 \
    net-tools \
    vim-tiny \
  && apt-get --reinstall install -y man-db coreutils manpages \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && yes | unminimize

WORKDIR /home/rstudio

# 必要かも
#  exactci \
#  fable \
#  feasts \
#  glmnet \
#  glmnetUtils \
#  ggfortify \
#  neuralnet \
#  ploty \
#  pryr \
#  tsibble \

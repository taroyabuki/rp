FROM rocker/tidyverse

RUN install2.r --error \
  caret \
  doParallel \
  e1071 \
  epitools \
  factoextra \
  forecast \
  furrr \
  ggrepel \
  gplots \
  gridExtra \
  igraph \
  MLmetrics \
  ROCR \
  randomForest \
  rpart.plot \
  tsibble \
  xgboost

RUN installGithub.r \
  rstudio/keras \
  vqv/ggbiplot

USER rstudio
RUN Rscript -e '\
  reticulate::install_miniconda();\
  keras::install_keras();\
  saveRDS(keras::dataset_mnist(), "/tmp/mnist.obj");'
USER root

RUN apt-get update \
  && apt-get install -y \
    libglpk-dev \
  && rm /etc/dpkg/dpkg.cfg.d/excludes \
  && apt-get --reinstall install -y man-db coreutils manpages \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 必要かも
#  feasts \
#  glmnet \
#  leaps \
#  psych \
#  zoo

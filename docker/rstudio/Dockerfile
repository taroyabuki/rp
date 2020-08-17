FROM rocker/tidyverse

RUN install2.r --error \
  caret \
  doParallel \
  e1071 \
  epitools \
  forecast \
  furrr \
  ggrepel \
  gplots \
  gridExtra \
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

# 必要かも
#  feasts \
#  glmnet \
#  leaps \
#  psych \
#  zoo

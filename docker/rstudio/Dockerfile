FROM rocker/tidyverse

RUN install2.r --error \
  caret \
  doParallel \
  e1071 \
  epitools \
  feasts \
  forecast \
  furrr \
  ggrepel \
  glmnet \
  gplots \
  gridExtra \
  leaps \
  psych \
  ROCR \
  randomForest \
  rpart.plot \
  xgboost \
  zoo

RUN installGithub.r \
  rstudio/keras \
  vqv/ggbiplot

RUN Rscript -e "reticulate::install_miniconda();\
                keras::install_keras()"
FROM rocker/ml

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
  vqv/ggbiplot

# 必要かも
#  feasts \
#  glmnet \
#  leaps \
#  psych \
#  zoo

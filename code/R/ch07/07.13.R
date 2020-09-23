### 7.13.1 Rの場合

library(doParallel)
cl <- makeCluster(detectCores())
registerDoParallel(cl)

library(furrr)
plan(multisession)


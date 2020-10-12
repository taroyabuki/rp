### 7.13.2 Pythonの場合

my_score = cross_validate(my_model, X, y, cv=my_cv,
                          n_jobs=-1, # 並列計算
                          return_train_score=True)
# 以下は省略

my_scores = cross_val_score(my_model, X, y, cv=my_cv,
                            n_jobs=-1) # 並列計算
# 以下は省略

my_search = GridSearchCV(my_model,
                         my_params,
                         cv=my_cv,
                         n_jobs=-1, # 並列計算
                         return_train_score=True)
# 以下は省略


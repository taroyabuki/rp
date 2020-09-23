### 7.13.2 Pythonの場合

#  n_jobsがあるのとないのがあるんだよね．．．
clf = GridSearchCV(my_knr, params, cv=rkf, scoring='neg_mean_squared_error', return_train_score=True, n_jobs=4)


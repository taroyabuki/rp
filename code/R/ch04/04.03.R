### 4.3.1 検定

binom.test(x = 14,                # 表が出た回数
           n = 20,                # コインを投げた回数
           p = 0.5,               # 表が出る確率（仮説）
           conf.level = 1 - 0.05) # 信頼係数（後述） = 1 - 有意水準

#>         Exact binomial test
#> 
#> data:  14 and 20
#> number of successes = 14, number of trials = 20, p-value = 0.1153
#> alternative hypothesis: true probability of success is not equal to 0.5
#> 95 percent confidence interval:
#>  0.4572108 0.8810684
#> sample estimates:
#> probability of success 
#>                    0.7 

x = 5
s = pbinom(q = x,
           size = 20,
           prob = 0.5)
s
#> [1] 0.02069473

qbinom(p = s, size = 20, prob = 0.5)
#> [1] 5

alpha = 0.05
qbinom(p = c(alpha / 2,      # 左側 2.5%
             1 - alpha / 2), # 右側97.5%
       size = 20,            # コインを投げた回数
       prob = 0.5)           # 表が出る確率（仮説）
#> [1]  6 14 # 左側の境界は6，右側の境界は14

#### 4.3.2.2 ブートストラップ

X <- rep(0:1, c(6,14))                      # 手順1
tmp <- sample(X, size = 20, replace = TRUE) # 手順2
tmp
#>  [1] 1 0 1 0 1 0 0 0 1 0 0 1 0 1 1 1 1 1 1 1

mean(tmp) # 手順3
#> [1] 0.75

result <- replicate(10^5, mean(sample(X, size = 20, replace = TRUE))) # 手順4
quantile(result, c(0.025, 0.975))                                     # 手順5

#>  2.5% 97.5% 
#>   0.5   0.9 

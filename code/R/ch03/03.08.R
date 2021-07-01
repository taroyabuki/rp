### 3.8.2 変数や関数についての調査

x <- 123
typeof(x)
#> [1] "double"

?log
# あるいは
help(log)

### 3.8.3 RのNA，Pythonのnan

my_v = c(1, NA, 3)
my_v
#> [1]  1 NA  3

is.na(my_v[2])
#> [1] TRUE

my_v[2] == NA # 誤り
#> [1] NA


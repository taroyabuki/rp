### 3.6.1 RのNA，Pythonのnan

my_v = c(1, NA, 3)
my_v
#> [1]  1 NA  3

is.na(my_v[2])
#> [1] TRUE

my_v[2] == NA # 誤り
#> [1] NA

### 3.6.2 変数についての調査

x = 123
typeof(x)
#> [1] "double"

x <- list("apple"   = "りんご",
          "orange" = "みかん")
names(x)
#> [1] "apple"  "orange"

str(x)
#> List of 2
#>  $ apple : chr "りんご"
#>  $ orange: chr "みかん"


## 5.1 データの読み込み

### 5.1.1 CSV

library(tidyverse)
system(str_c("wget https://raw.githubusercontent.com/taroyabuki",
             "/fromzero/master/data/exam.csv"))

#### 5.1.1.1 CSVの読み込み

my_df <- read_csv("exam.csv")
# あるいは
my_df <- read.csv("exam.csv",
  stringsAsFactors = FALSE)

my_df
#>   name english math gender
#> 1    A      60   70      f
#> 2    B      90   80      m
#> 3    C      70   90      m
#> 4    D      90  100      f

my_url <- str_c("https://raw.githubusercontent.com/taroyabuki",
                "/fromzero/master/data/exam.csv")
my_df <- read_csv(my_url)
# あるいは
my_df <- read.csv(my_url, stringsAsFactors = FALSE)

my_df2 <- read.csv(
  file = "exam.csv",
  stringsAsFactors = FALSE,
  row.names = 1)
my_df2
#>   english math gender
#> A      60   70      f
#> B      90   80      m
#> C      70   90      m
#> D      90  100      f

#### 5.1.1.2 CSVファイルへの書き出し

my_df %>% write_csv("exam2.csv")
# あるいは
my_df %>% write.csv(file = "exam2.csv",
  row.names = FALSE) # 行名を出力しない．

my_df2 %>% write.csv("exam3.csv")

### 5.1.2 文字コード

my_df <- read_csv(file = "exam.csv",
  locale = locale(encoding = "UTF-8"))
# あるいは
my_df <- read.csv(file = "exam.csv",
  stringsAsFactors = FALSE,
  fileEncoding = "UTF-8")

my_df %>% write_csv("exam2.csv")
# あるいは
my_df %>% write.csv(file = "exam2.csv", row.names = FALSE,
                    fileEncoding = "UTF-8")

### 5.1.3 ウェブ上の表

my_url <- "https://github.com/taroyabuki/fromzero/blob/master/data/exam.csv"
my_tables <- xml2::read_html(my_url) %>% rvest::html_table()

my_tables 
#> [[1]]
#>   X1   X2      X3   X4     X5
#> 1 NA name english math gender
#> 2 NA    A      60   70      f
#> 3 NA    B      90   80      m
#> 4 NA    C      70   90      m
#> 5 NA    D      90  100      f

tmp <- my_tables[[1]]
tmp
#>   X1   X2      X3   X4     X5
#> 1 NA name english math gender
#> 2 NA    A      60   70      f
#> 3 NA    B      90   80      m
#> 4 NA    C      70   90      m
#> 5 NA    D      90  100      f

# 1行目のデータを使って列の名前を付け直す．
colnames(tmp) <- tmp[1,]

# 1行目と1列目を削除する．
my_data <- tmp[-1 ,-1]
my_data
#>   name english math gender
#> 2    A      60   70      f
#> 3    B      90   80      m
#> 4    C      70   90      m
#> 5    D      90  100      f

### 5.1.4 JSONとXML

#### 5.1.4.1 JSONデータの読み込み

library(jsonlite)

my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/exam.json")
my_data <- fromJSON(my_url)
#my_data <- fromJSON("exam.json") # （ファイルを使う場合）
my_data
#>   name english math gender
#> 1    A      60   70      f
#> 2    B      90   80      m
#> 3    C      70   90      m
#> 4    D      90  100      f

#### 5.1.4.2 XMLデータの読み込み

library(xml2)

my_url <- str_c("https://raw.githubusercontent.com",
                "/taroyabuki/fromzero/master/data/exam.xml")
my_xml <- read_xml(my_url)      # XMLデータの読み込み
#my_xml <- read_xml("exam.xml") # （ファイルを使う場合）
xml_ns(my_xml)                  # 名前空間の確認（d1）
#> d1 <-> https://www.example.net/ns/1.0

my_records <- xml_find_all(my_xml, ".//d1:record")

f <- function(record) {
  tmp <- xml_attrs(record)                    # 属性を全て取り出し，
  xml_children(record) %>% walk(function(e) {
    tmp[xml_name(e)] <<- xml_text(e)          # 子要素の名前と内容を追加する．
  })
  tmp
}

my_data <- my_records %>% map_dfr(f)
my_data$english <- as.numeric(my_data$english)
my_data$math    <- as.numeric(my_data$math)
my_data
#>   english  math gender name 
#>     <dbl> <dbl> <chr>  <chr>
#> 1      60    70 f      A    
#> 2      90    80 m      B    
#> 3      70    90 m      C    
#> 4      90   100 f      D  


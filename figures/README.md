# 図の生成コード


## Jupyter notebook用のコンテナ

## RStudio用のコンテナ（R）

作業フォルダにソースを用意する．

```bash
# 作業フォルダで
git clone https://github.com/taroyabuki/rp.git

# gitが無い場合は
docker run --rm -it -v ${PWD}:/home/rstudio/work taroyabuki/rstudio bash -c 'cd /home/rstudio/work && git clone https://github.com/taroyabuki/rp.git'
```

図を作る．

```bash
docker run --rm -it -v ${PWD}:/home/rstudio/work taroyabuki/rstudio bash -c 'cd /home/rstudio/work/rp/figures/fig-r && make clean && make'
```

## 補足：pdfcrop

書籍の図表はpdfcropで余白を削除しています．

### Jupyter notebook用のコンテナ

### RStudio用のコンテナ（R）

```bash
docker run -it -v ${PWD}:/home/rstudio/work --name rscrop taroyabuki/rstudio bash

#以下はコンテナ内での操作
#bash -c "echo 'Acquire::http::Proxy \"http://10.100.192.4:3142/\";' >> /etc/apt/apt.conf.d/02proxy"
apt-get update && apt-get install -y texlive-extra-utils # for pdfcrop
cd /home/rstudio/work/rp/fig-r && make clean && make
```
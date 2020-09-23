# 図の生成コード

## Jupyter notebook用のコンテナ（R・Python）

作業フォルダにソースを用意します．

```bash
# 作業フォルダで
docker run --rm -u root -it -v $(pwd):/home/jovyan/work taroyabuki/jupyter bash -c 'cd /home/jovyan/work && git clone https://github.com/taroyabuki/fromzero.git'
```

図を作ります

```bash
# R
docker run --rm -u root -it -v $(pwd):/home/jovyan/work taroyabuki/jupyter bash -c 'cd /home/jovyan/work/fromzero/figures/fig-r && make clean && make'

# Python
docker run --rm -u root -it -v $(pwd):/home/jovyan/work taroyabuki/jupyter bash -c 'cd /home/jovyan/work/fromzero/figures/fig-p && make clean && make'
```

## RStudio用のコンテナ（R）

作業フォルダにソースを用意します．

```bash
# 作業フォルダで
docker run --rm -u rstudio -it -v $(pwd):/home/rstudio/work taroyabuki/rstudio bash -c 'cd /home/rstudio/work && git clone https://github.com/taroyabuki/fromzero.git'
```

図を作ります．

```bash
docker run --rm -u rtsutio -it -v $(pwd):/home/rstudio/work taroyabuki/rstudio bash -c 'cd /home/rstudio/work/fromzero/figures/fig-r && make clean && make'
```

## 補足：pdfcrop

書籍の図表はpdfcropで余白を削除しています．

### Jupyter notebook用のコンテナ（R・Python）

```bash
docker run --rm -u root -it -v $(pwd):/home/jovyan/work taroyabuki/jupyter bash

#以下はコンテナ内での操作
apt-get update && apt-get install -y texlive-extra-utils # for pdfcrop
cd /home/jovyan/work/fromzero/figures/fig-r && make clean && make # R
cd /home/jovyan/work/fromzero/figures/fig-p && make clean && make # Python
```

### RStudio用のコンテナ（R）

```bash
docker run --rm -it -v $(pwd):/home/rstudio/work taroyabuki/rstudio bash

#以下はコンテナ内での操作
apt-get update && apt-get install -y texlive-extra-utils # for pdfcrop
su rstudio
cd /home/rstudio/work/fromzero/figures/fig-r && make clean && make
```
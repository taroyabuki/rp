# 図の生成コード

## Jupyter notebook用のコンテナ（R・Python）

作業フォルダにソースを用意します．

```bash
# 作業フォルダで
docker run --rm -u root -it -v ${PWD}:/home/jovyan/work taroyabuki/jupyter bash -c 'cd /home/jovyan/work && git clone https://github.com/taroyabuki/rp.git'
```

図を作ります

```bash
# R
docker run --rm -u root -it -v ${PWD}:/home/jovyan/work taroyabuki/jupyter bash -c 'cd /home/jovyan/work/rp/figures/fig-r && make clean && make'

# Python
docker run --rm -u root -it -v ${PWD}:/home/jovyan/work taroyabuki/jupyter bash -c 'cd /home/jovyan/work/rp/figures/fig-p && make clean && make'
```

## RStudio用のコンテナ（R）

作業フォルダにソースを用意します．

```bash
# 作業フォルダで
docker run --rm -it -v ${PWD}:/home/rstudio/work taroyabuki/rstudio bash -c 'cd /home/rstudio/work && git clone https://github.com/taroyabuki/rp.git'
```

図を作ります．

```bash
docker run --rm -it -v ${PWD}:/home/rstudio/work taroyabuki/rstudio bash -c 'cd /home/rstudio/work/rp/figures/fig-r && make clean && make'
```

## 補足：pdfcrop

書籍の図表はpdfcropで余白を削除しています．

### Jupyter notebook用のコンテナ（R・Python）

```bash
docker run --rm -u root -it -v ${PWD}:/home/jovyan/work taroyabuki/jupyter bash

#以下はコンテナ内での操作
#bash -c "echo 'Acquire::http::Proxy \"http://10.100.192.4:3142/\";' >> /etc/apt/apt.conf.d/02proxy"
apt-get update && apt-get install -y texlive-extra-utils # for pdfcrop
cd /home/jovyan/work/rp/figures/fig-r && make clean && make # R
cd /home/jovyan/work/rp/figures/fig-p && make clean && make # Python
```

### RStudio用のコンテナ（R）

```bash
docker run -it -v ${PWD}:/home/rstudio/work --name rscrop taroyabuki/rstudio bash

#以下はコンテナ内での操作
#bash -c "echo 'Acquire::http::Proxy \"http://10.100.192.4:3142/\";' >> /etc/apt/apt.conf.d/02proxy"
apt-get update && apt-get install -y texlive-extra-utils # for pdfcrop
cd /home/rstudio/work/rp/figures/fig-r && make clean && make
```
# Jupyter notebook

https://hub.docker.com/r/taroyabuki/jupyter

## 使い方

```bash
docker run \
-d \
-p 8888:8888 \
-v $(pwd):/home/jovyan/work \
--name jr \
taroyabuki/jupyter \
start-notebook.sh \
--NotebookApp.token='password'
```

ホスト側で8888を使っているなら，`-p 8080:8888`などとして，別のポートを使う．

ブラウザでhttp://localhost:8888 を開く．（ポートを変えた場合は数値を変える．）

## 起動スクリプト

起動スクリプトをダウンロードしておけば，`sh ~/start-jupyter.sh`で起動できる．（パスワードは`password`．変更したい場合はstart-rstudio.shを編集する．）

```bash
curl -o ~/start-jupyter.sh \
https://raw.githubusercontent.com/taroyabuki/rp/master/docker/jupyter/start-jupyter.sh
```
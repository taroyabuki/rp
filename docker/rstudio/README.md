# RStudio

https://hub.docker.com/r/taroyabuki/rstudio

## 使い方

```bash
docker run \
-d \
-e PASSWORD=password \
-e ROOT=TRUE \
-p 8787:8787 \
-v $(pwd):/home/rstudio/work \
--name rs \
taroyabuki/rstudio
```

ホスト側で8787を使っているなら，`-p 8080:8787`などとして，別のポートを使う．

ブラウザでhttp://localhost:8787 を開く．（ポートを変えた場合は数値を変える．）

## 起動スクリプト

起動スクリプトをダウンロードしておけば，`sh ~/start-rstudio.sh`で起動できる．（パスワードは`password`．変更したい場合は~/start-rstudio.shを編集する．）

```bash
curl -o ~/start-rstudio.sh \
https://raw.githubusercontent.com/taroyabuki/rp/master/docker/rstudio/start-rstudio.sh
```
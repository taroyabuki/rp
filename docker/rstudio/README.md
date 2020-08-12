# RStudio

## 使い方

```bash
docker run -e DISABLE_AUTH=true -d -p 8787:8787 -v ${PWD}:/home/rstudio/work --name rs taroyabuki/test-r
# -e DISABLE_AUTH=true　　パスワードなし（セキュリティ低下）
# -d　　バックグラウンドで動作させる．
# -p 8787:8787　　ホストのポート8787をコンテナのポート8787に転送する．
# --name rs　　名前をrsにする（変更可）
```

ホスト側で8787を使っているなら，`-p 8080:8787`などとして，別のポートを使う．

ブラウザでhttp://localhost:8787 を開く．（ポートを変えた場合は数値を変える．）

## 補足

図表作成環境の構築

```bash
docker exec -it rs bash
#bash -c "echo 'Acquire::http::Proxy \"http://10.100.192.4:3142/\";' >> /etc/apt/apt.conf.d/02proxy"
apt-get update && apt-get install -y texlive-extra-utils # for pdfcrop
```
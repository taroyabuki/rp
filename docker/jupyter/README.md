# Jupyter notebook

## 使い方

```bash
docker run -d -p 8888:8888 -v ${PWD}:/home/jovyan/work --name jr taroyabuki/test-p start-notebook.sh --NotebookApp.token=''
# -d　　バックグラウンドで動作させる．
# -p 8888:8888　　ホストのポート8888をコンテナのポート8888に転送する．
# -v ${PWD}:/home/jovyan/work　　作業フォルダの共有
# --name jr　　名前をjrにする（変更可）
# taroyabuki/test-p　　コンテナの名前
# start-notebook.sh　　ノートブックを起動するコマンド
# --NotebookApp.token=''　　トークンの入力を省略する（セキュリティ低下）
```

ホスト側で8888を使っているなら，`-p 8080:8888`などとして，別のポートを使う．

ブラウザでhttp://localhost:8888 を開く．（ポートを変えた場合は数値を変える．）

## 補足

図表作成環境の構築

```bash
docker exec -it jr bash
#bash -c "echo 'Acquire::http::Proxy \"http://10.100.192.4:3142/\";' >> /etc/apt/apt.conf.d/02proxy"
apt-get update && apt-get install -y texlive-extra-utils # for pdfcrop
```
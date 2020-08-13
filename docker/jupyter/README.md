# Jupyter notebook

https://hub.docker.com/r/taroyabuki/jupyter

## 使い方

```bash
docker run -d -p 8888:8888 -v ${PWD}:/home/jovyan/work --name jr taroyabuki/jupyter start-notebook.sh --NotebookApp.token=''
# -d                          バックグラウンドで動作させる．
# -p 8888:8888                ホストのポート8888をコンテナのポート8888に転送する．
# -v ${PWD}:/home/jovyan/work 作業フォルダの共有
# --name jr                   名前をjrにする（変更可）
# taroyabuki/jupyter          Docker Hubのリポジトリ
# start-notebook.sh           ノートブックを起動するコマンド
# --NotebookApp.token=''      トークンの入力を省略する（セキュリティ低下）
```

ホスト側で8888を使っているなら，`-p 8080:8888`などとして，別のポートを使う．

ブラウザでhttp://localhost:8888 を開く．（ポートを変えた場合は数値を変える．）
# flask_book
## テキスト
* [Python FlaskによるWebアプリ開発入門 物体検知アプリ&機械学習APIの作り方](https://www.shoeisha.co.jp/book/detail/9784798175164)

## 準備
### Flask のインストール
```
% pip install flask
```

### Flask のコマンド
* `flask --help`
  * オプションの確認に使う。
* `flask run`
  * Flask の組み込みサーバーを実行する。詳しくは `flask run --help` を実行すると確認できる。
  * このコマンドを実行すると `http://127.0.0.1:5000/` でWebサーバーが起動する。
* `flask rotues`
  * アプリのルーティング情報を出力する。
* `flask shell`
  * Flaskアプリの実行環境（コンテキスト）でPythonのインタラクティブシェルを使う場合に実行する。デバッグやテストのときに役に立つ。

### ライブラリのインストール
```
% pip install flake8 black isort mypy
```

| Library | Usage |
| ---- | ---- |
| flake8 | コードがPEP8の書き方に沿っているか自動チェック |
| black |  PEP8に沿った書き方にコードを自動整形 |
| isort | import文をPEP8に沿った書き方に自動で並び替える |
| mypy | タイプヒントの型チェック |

### VS Code の設定
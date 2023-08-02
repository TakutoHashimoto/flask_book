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

| Library | Usage                                          |
| ------- | ---------------------------------------------- |
| flake8  | コードがPEP8の書き方に沿っているか自動チェック |
| black   | PEP8に沿った書き方にコードを自動整形           |
| isort   | import文をPEP8に沿った書き方に自動で並び替える |
| mypy    | タイプヒントの型チェック                       |

### VS Code の設定
* VS Codeの **[Manage]** ボタンをクリックして **[Setting]** を選択する。設定画面が開くので、**[Workspace]** タブを選択する。このタブでは、このプロジェクトだけに適用される設定を行うことができる。このタブで以下のライブラリの設定を行う。
1. Lint機能を有効にする
   1. 検索ボックスに `Python > Linting: Enabled` と入力するとコードチェックを行うLint機能の設定項目が表示される。その項目が有効になっているかチェックする（有効になっていなかったらチェックを入れる）。
2. `flake8` を有効にする
   1. 検索ボックスに `Python > Linting: Flake8 Enabled` と入力して、設定項目にチェックを入れる。
3. 1行の最大文字数を変更する（-> 最大文字数のデフォルトが `flake8` は79文字、`black` は88文字なので `black` に合わせる）
   1. 検索ボックスに `Flake8 Args` と入力して「設定項目の追加」をクリックする。
   2. 入力欄に `--max-line-length=88` と入力する。
4. `black` の設定
   1. 検索ボックスに `Python > Formatting: Provider` と入力して設定項目を表示する。
   2. プルダウンから `black` を選択する。
   3. 検索ボックスに `Editor: Format On Save` と入力して、設定項目にチェックを入れる。
5. `isort` の設定
   1. 検索ボックスに `Editor: Code Action On Save` と入力して設定項目を表示して、**[setting.jsonで編集]** をクリックする。
   2. `editor.codeActionsOnSave` を次のように変更する。
      ```json
      "editor.codeActionOnSave": {
        "source.organizeImports": true
      }
      ```
6. `mypy` の設定
   1. 検索ボックスに `Python > Linting: Mypy Enabled` と入力して、設定項目にチェックを入れる。
* 以上の設定を行うと、プロジェクト内に `.vscode` というディレクトリが追加される。GitHub でソースコードを管理したいがこのディレクトは邪魔だと感じたときは、`.gitignore` ファイルを作成してそこに `.vscode` と入力するとトラッキングの対象から外すことができる。


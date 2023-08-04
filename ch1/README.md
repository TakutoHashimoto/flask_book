# 最小限のアプリを作る
## MVTモデル
Flaskはユーザーインターフェイスを持つアプリを実装するためのデザインパターンとして、**MVTモデル**(Model, View, Template)を採用している。

| インターフェイス | 責務                                      |
| ---------------- | ----------------------------------------- |
| Model            | ビジネスロジックを担当する                |
| View             | 入力を受け取り、ModelとTemplateを制御する |
| Template         | 入出力を担当する                          |

一般的にはMVCモデルが有名だが、MVTのViewはMVCのC(Controller)、MVTのTemplateはMVCのViewに相当する。

![mvt](https://github.com/TakutoHashimoto/flask_book/assets/125980270/21cd58c8-afe3-48de-bd35-32ba9ccdd16d) 


## 最小限のアプリを作成する
最小限の機能を持つアプリ `minimal_app` を作成する。

### 作業用として、`apps/minimal_app` ディレクトリを作成する
```shell
% mkdir -p apps/minimal_app
```

次のようなディレクトリ構成でアプリ作成を進める。
```shell
% tree
.
└── apps
       └── minimal_app
           └── app.py
```

### 環境変数を設定する
2つの環境変数を以下のように設定する。

| 環境変数  | 設定する値                                                                                         |
| --------- | -------------------------------------------------------------------------------------------------- |
| FLASK_APP | `app.py` のパス                                                                                    |
| FLASK_ENV | `development` または `production` を指定する。`development` を指定するとデバッグモードがONになる。 |

ターミナルで以下のように設定する。
```shell
% export FLASK_APP=app.py
% export FLASK_ENV=development
```

### `flask run` コマンドで実行する
`app/minimal_app` ディレクトリで `flask run` コマンドを実行する。実行すると以下のようなテキストがターミナルに出力される。

```shell
% flaks run
    * Serving Flask app 'app.py'
    * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

`Running on http://~~~` と表示されているところのURLにブラウザからアクセスする。`Hello, Flask book!` と表示されていれば問題ない。

### `.env` を使って環境変数を設定する
環境変数の設定には `export` を使っていたが、この方法だと、一度設定した環境変数はターミナルを終了させると消されてしまう。コンソールの環境変数を永続化させる方法もあるが、それだとアプリを切り替えるたびに環境変数を設定し直す必要がある。`.env` ファイルを使うと、アプリ単位で環境変数を設定することができる。そうすることで、アプリの実行時にそのアプリの環境変数を読み込むようにすることができる。


ここでは、`python-dotenv` というライブラリを使用するのでインストールする。
```shell
pip install python-dotenv
```

`minimal_app`　配下に `.env` ファイルを作成して環境変数を設定する。

### アプリケーションルート
アプリケーションルートはアプリを実行するディレクトリのことで、モジュールやパッケージ[^1]を読み込むパスはアプリケーションルートにより決まる。

[^1] モジュールは関数やクラスを集めた`.py`ファイル、パッケージはモジュールを集めたもののことを指す。
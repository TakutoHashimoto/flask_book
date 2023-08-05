from flask import Flask, render_template, url_for, current_app, g


app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Hello, Flask book!"


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
# app.get("/hello")と書くこともできる
def hello(name: str) -> str:
    return f"Hello, {name}!"


@app.route("/name/<name>")
def show_name(name: str) -> "html":
    return render_template("index.html", name=name)


# アプリケーションコンテキストを取得してスタックにpushする
app.app_context().push()

# current_appにアクセス可能になる
print(current_app.name)
# => apps.minimal_app.app

# グローバルなテンポラリ領域に値を設定する
g.connection = "connection"
print(g.connection)
# => connection


# ルーティング情報を出力する
with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro", page=1))


# ターミナル上でpython app.pyで実行する場合は以下のコードを書く必要がある。
# if __name__ == "__main__":
#     app.run(debug=True)

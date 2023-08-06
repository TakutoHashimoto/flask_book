import logging
from flask_debugtoolbar import DebugToolbarExtension
from email_validator import validate_email, EmailNotValidError
from flask import (
    Flask,
    render_template,
    url_for,
    current_app,
    g,
    request,
    redirect,
    flash,
)


app = Flask(__name__)

app.config["SECRET_KEY"]  # TODO: SECRET_KEYは環境変数から取得するように設定する
app.logger.setLevel(logging.DEBUG)
# リダイレクトを中断しないようにする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# DebugToolbarExtensionにアプリをセットする
toolbar = DebugToolbarExtension(app)


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


@app.route("/contact")
def contact() -> "html":
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        user_name = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not user_name:
            flash("ユーザー名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not is_valid:
            return redirect(url_for("cotntact"))

        # TODO: メール送信の処理を実装する

        # 問い合わせ完了エンドポイントにリダイレクトする
        flash("問い合わせ内容はメールで送信しました。問い合わせありがとうございました。")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


# ルーティング情報を出力する
# with app.test_request_context():
#     # /
#     print(url_for("index"))
#     # /hello/world
#     print(url_for("hello-endpoint", name="world"))
#     # /name/ichiro?page=1
#     print(url_for("show_name", name="ichiro", page=1))


with app.test_request_context("/users?update=true"):
    print(request.args.get("updated"))
    # => true


# ターミナル上でpython app.pyで実行する場合は以下のコードを書く必要がある。
# if __name__ == "__main__":
#     app.run(debug=True)

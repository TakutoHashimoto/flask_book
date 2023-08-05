from flask import Flask


app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Hello, Flask book!"


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
# app.get("/hello")と書くこともできる
def hello(name: str) -> str:
    return f"Hello, {name}!"


# ターミナル上でpython app.pyで実行する場合は以下のコードを書く必要がある。
# if __name__ == "__main__":
#     app.run(debug=True)

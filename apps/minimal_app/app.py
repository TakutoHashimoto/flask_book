from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Hello, Flask book!"


@app.route("/hello")
def hello() -> str:
    return "Hello, World!"


# ターミナル上でpython app.pyで実行する場合は以下のコードを書く必要がある。
# if __name__ == "__main__":
#     app.run(debug=True)

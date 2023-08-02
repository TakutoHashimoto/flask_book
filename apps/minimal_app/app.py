from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Flask book!"


# ターミナル上でpython app.pyで実行する場合は以下のコードを書く必要がある。
# if __name__ == "__main__":
#     app.run(debug=True)

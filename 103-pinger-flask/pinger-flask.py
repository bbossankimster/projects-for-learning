from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Simple ping"


if __name__ == "__main__":
    app.run(port=5010, debug=True)
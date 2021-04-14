from flask import Flask
from flask_restful import Api


from resources.index import Index
from resources.ping import Ping

app = Flask(__name__)
api = Api(app)

# @app.route("/")
# def index():
#    return "You can test API by "

api.add_resource(Index, '/')
api.add_resource(Ping, "/ping", "/ping/")
if __name__ == "__main__":
    app.run(port=5010, debug=True)

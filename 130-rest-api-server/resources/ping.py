from flask_restful import Resource
from pythonping import ping


class Ping(Resource):
    def get(self, id=0):
        return ping("8.8.8.8", verbose=True), 200

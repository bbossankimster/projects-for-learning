from flask_restful import Resource


class Index(Resource):
    def get(self, id=0):
        return "You can get http://127.0.0.1:5010/ping/ ", 200

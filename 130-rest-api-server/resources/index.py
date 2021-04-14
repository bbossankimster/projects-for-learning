from flask_restful import Resource


class Index(Resource):
    def get(self, id=0):
        return "You can ping 8.8.8.8", 200

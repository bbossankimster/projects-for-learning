from flask_restful import Resource
import subprocess


class Ping(Resource):
    def get(self, id=0):
        out = subprocess.run(['ping', '8.8.8.8'], capture_output=True)
        print(out.stdout.decode())
        return out.stdout.decode(), 200

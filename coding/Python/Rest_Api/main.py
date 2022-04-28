from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app )

class hello_world(Resource):
    def get(self):
        return {'Data': 'Hello world'}

api.add_resource(hello_world, '/helloworld')

if __name__ == '__main__':
    app.run(debug=True)

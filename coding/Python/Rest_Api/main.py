from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app )

names ={ 
'John':{'age':30 ,'gender':'male'}, 
'Paul':{'age':25 ,'gender':'male'} }


class hello_world(Resource):
    def get(self,name):
        return names[name]

api.add_resource(hello_world, '/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)

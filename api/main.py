from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.messages import messages1,messages2

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(messages1,"/messages1")
api.add_resource(messages2,"/messages2")

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
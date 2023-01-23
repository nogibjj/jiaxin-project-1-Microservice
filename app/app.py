from flask import Flask
from flask_restful import Api
from request import Request

app = Flask(__name__)
api = Api(app)

api.add_resource(Request, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
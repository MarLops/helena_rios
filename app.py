from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
from flask_cors import CORS
import json


class Mensagens(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_password', type=str)
        data = parser.parse_args()
        if (data["user_password"] != "guilherme_helena"):
            return ""
        print("passou")
        with open('data_teste.json') as f:
            t = json.load(f)
        t.append({"mensagem": "teste"})
        return t


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_password', type=str)
        parser.add_argument('new_mensagem', type=str)
        data = parser.parse_args()
        print(data)
        if (data["user_password"] != "guilherme_helena"):
            return ""
        print("passou")
        with open('data_teste.json') as f:
            t = json.load(f)
        t.append({"mensagen": str(data["new_mensagem"])})
        print("salvando")
        with open('data_teste.json','w') as f:
            json.dump(t, f)
        return "OK"

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Mensagens, '/mensagens')
if __name__ == "__main__":
    app.run(port=5050)

from flask import Flask, request
from flask_restful import Resource, Api

from pessoa_connection import retorna_pessoas, insere_pessoa, retorna_pessoa, remove_pessoa, atualiza_pessoa

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Bem-vinda ao curso mvcad!"

class Pessoa(Resource):
    def get(self):
        pessoas = retorna_pessoas()
        return pessoas

    def post(self):
        pessoa = request.json
        insere_pessoa(pessoa)
        return "Pessoa inserida com sucesso!"

    def put(self):
        pessoa = request.json
        atualiza_pessoa(pessoa)
        return "Pessoa atualizada com sucesso!"


class PessoaDetail(Resource):
    def get(self, id):
        pessoa = retorna_pessoa(id)
        return pessoa

    def delete(self, id):
        remove_pessoa(id)
        return "Pessoa removida com sucesso!"

api.add_resource(HelloWorld, "/")
api.add_resource(Pessoa, "/pessoas")
api.add_resource(PessoaDetail, "/pessoa/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)

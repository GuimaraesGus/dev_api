from flask import Flask, request
from flask_restful import Resource, Api
import json

import habilidades
from habilidades import Habilidades, Habilidade

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Galleani',
        'habilidades': ['Python', 'Django']
    }
]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe!'.format(id)
            response = {'status':'ERRO', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status': 'ERRO', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        if habilidades.existeHabilidade(dados['habilidades']):
            desenvolvedores[id] = dados
            return dados
        else:
            mensagem = 'Verifique se as habilidades informadas estão cadastradas!'
            response = {'status': 'ERRO', 'mensagem': mensagem}
            return response

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'Sucesso!', 'mensagem':'Registro excluído.'}

# lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        if habilidades.existeHabilidade(dados['habilidades']):
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        else:
            mensagem = 'Verifique se as habilidades informadas estão cadastradas!'
            response = {'status': 'ERRO', 'mensagem': mensagem}
            return response

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidade, '/habilidade/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
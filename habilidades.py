from flask_restful import Resource, request
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'Django', 'COBOL']

def existeHabilidade(dados):
    habilidades_novas = set(dados)
    habilidades_banco = set(lista_habilidades)
    if habilidades_novas.issubset(habilidades_banco):
        return True
    else:
        return False

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados['habilidade'])
        return lista_habilidades

class Habilidade(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados['habilidade']
        return lista_habilidades

    def delete(self, id):
        lista_habilidades.pop(id)
        return lista_habilidades
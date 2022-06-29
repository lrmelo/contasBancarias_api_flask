from util.conta import Conta
from util.responses import Responses
from operator import indexOf
from flask import Flask, jsonify, request
from flask_api import status
import json, requests

app = Flask(__name__)
list = []
f = open('util/messages.json')
message = json.load(f)

@app.route("/conta/listar", methods=['GET'])
def lista():
    if not list:
        return (Responses.response(message["NO_ACCOUNTS"])),status.HTTP_404_NOT_FOUND
    return jsonify(contas=[conta.serialize() for conta in list]),status.HTTP_200_OK

@app.route("/conta", methods=['GET'])
def consulta():
    data = request.form
    for i in list:
        if data['codigo'] == i.codigo:
            return (Responses.responseAccount(i.codigo, i.nomeProprietario, i.tipo, i.saldo)),status.HTTP_200_OK
    return (Responses.response(message["ACCOUNT_NOT_FOUND"])),status.HTTP_404_NOT_FOUND 
    
@app.route("/conta", methods=['POST'])
def cadastrar():
    data = request.form
    conta = Conta(data["nomeProprietario"],data['tipo'],data['saldo'])
    if data['tipo'] == 'c' or data['tipo'] == 'p':
        list.append(conta)
        return (Responses.response("Cadastrado efetuado com sucesso, codigo: " + str(Conta.aux))),status.HTTP_201_CREATED
    else:
        return (Responses.response(message["INVALID_TYPE"])),status.HTTP_400_BAD_REQUEST

@app.route("/conta", methods=['PUT'])
def atualizar():
    data = request.form
    for i in list:
        if data['codigo'] == i.codigo:
            if data['tipo'] == 'c' or data['tipo'] == 'p':
                nomeProprietarioTuple = data['nomeProprietario']
                tipoTuple = data['tipo']
                saldoTuple = data['saldo']

                i.nomeProprietario = ''.join(nomeProprietarioTuple)
                i.tipo = ''.join(tipoTuple)
                i.saldo = ''.join(saldoTuple)

                return (Responses.response("Conta de codigo " + data['codigo'] + " atualizada com sucesso!")),status.HTTP_200_OK
            return (Responses.response(message["INVALID_TYPE"])),status.HTTP_400_BAD_REQUEST
    return (Responses.response(message["ACCOUNT_NOT_FOUND"])),status.HTTP_404_NOT_FOUND

@app.route("/conta", methods=['DELETE'])
def deletar():
    for i in list:
        data = request.form
        if data['codigo'] == i.codigo:
            index = list.index(i)
            list.pop(index)
            return (Responses.response("Conta codigo " + data['codigo'] +  " deletada com sucesso!")),status.HTTP_200_OK
    return (Responses.response(message["ACCOUNT_NOT_FOUND"])),status.HTTP_404_NOT_FOUND






















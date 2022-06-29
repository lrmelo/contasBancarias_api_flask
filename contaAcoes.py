from util.conta import Conta
from util.responses import Responses
from flask import Flask,jsonify, request
from flask_api import status
import json, requests

HOST = "http://localhost:5000/conta"
f = open('util/messages.json')
message = json.load(f)
app = Flask(__name__)

@app.route("/lerSaldo", methods=['GET'])
def lerSaldo():
    data = request.form
    cod={"codigo":data['codigo']}
    req = requests.get(HOST, data=cod)
    resp = json.loads(req.content.decode())
    if(req.status_code == 404):
        return (jsonify(resp)),status.HTTP_404_NOT_FOUND
    else:
        return (Responses.responseSaldo(resp['saldo'])),status.HTTP_200_OK
    

@app.route("/deposito", methods=['PUT'])
def deposito():
    data = request.form
    cod={"codigo":data['codigo']}
    req = requests.get(HOST, data=cod)
    resp = json.loads(req.content.decode())
    if(req.status_code == 404):
        return (jsonify(resp)),status.HTTP_404_NOT_FOUND
    else:
        val = data['valor']
        newSaldo = int(resp["saldo"]) + int(val) 
        form={
                "codigo":data['codigo'],
                "nomeProprietario":resp["nomeProprietario"],
                "tipo":resp["tipo"],
                "saldo":str(newSaldo)
            }
        requests.put(HOST, data=form)
        return (Responses.response("Deposito efetuado com sucesso")),status.HTTP_202_ACCEPTED

@app.route("/retirada", methods=['PUT'])
def retirada():
    data = request.form
    cod={"codigo":data['codigo']}
    req = requests.get(HOST, data=cod)
    resp = json.loads(req.content.decode())
    if(req.status_code == 404):
        return (jsonify(resp)),status.HTTP_404_NOT_FOUND
    else:
        val = int(data['valor'])
        if int(resp["saldo"]) >= val:
            newSaldo = int(resp["saldo"]) - val
            form={
                    "codigo":data['codigo'],
                    "nomeProprietario":resp["nomeProprietario"],
                    "tipo":resp["tipo"],
                    "saldo":str(newSaldo)
                }
            requests.put(HOST, data=form)
            return (Responses.response("Retirada efetuada com sucesso")),status.HTTP_202_ACCEPTED
        return (Responses.response("Não é possivel realizar retirada pois o saldo é insuficiente")),status.HTTP_200_OK
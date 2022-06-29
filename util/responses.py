from flask import jsonify
class Responses:
    def response(resposta):
        return jsonify({
            'resposta': resposta
        })
        
    def responseSaldo(resposta):
        return jsonify({
            'Saldo': resposta
        })

    def responseAccount(codigo, nomeProprietario, tipo, saldo):
        return jsonify({
            'codigo': codigo,
            'nomeProprietario': nomeProprietario,
            'tipo': tipo,    
            'saldo': saldo
        })

class Conta:
    aux = 999
    def __init__(self, nomeProprietario, tipo, saldo): 
        Conta.aux += 1
        self.codigo = str(Conta.aux)
        self.nomeProprietario = nomeProprietario
        self.tipo = tipo
        self.saldo = saldo
    def serialize(self):
        return {
            'codigo': self.codigo, 
            'nomeProprietario': self.nomeProprietario,
            'tipo': self.tipo,
            'saldo': self.saldo
        }